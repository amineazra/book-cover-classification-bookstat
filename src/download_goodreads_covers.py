
from pathlib import Path
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from PIL import Image
import pandas as pd
import requests
import csv
import time

ROOT = Path(__file__).resolve().parents[1]

MANIFEST = ROOT / "data/processed/goodreads_all_download_manifest.csv"
IMAGE_DIR = ROOT / "data/goodreads_images"
LOG_FILE = ROOT / "data/processed/goodreads_download_errors.csv"

IMAGE_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(MANIFEST)

retry = Retry(
    total=3,
    backoff_factor=2,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"],
    respect_retry_after_header=True,
)

session = requests.Session()
session.headers.update({
    "User-Agent": "AcademicBookCoverResearch/1.0"
})
session.mount("https://", HTTPAdapter(max_retries=retry))
session.mount("http://", HTTPAdapter(max_retries=retry))

downloaded = 0
skipped = 0
failed = 0
MAX_BYTES = 12 * 1024 * 1024

print("Toplam aday:", len(df))

try:
    with LOG_FILE.open("a", newline="", encoding="utf-8") as log:
        writer = csv.writer(log)

        for i, row in enumerate(df.itertuples(index=False), 1):
            output = IMAGE_DIR / str(row.filename)
            temp = IMAGE_DIR / (str(row.filename) + ".part")
            converted = IMAGE_DIR / (str(row.filename) + ".tmp")

            if output.exists() and output.stat().st_size > 0:
                skipped += 1
                continue

            try:
                with session.get(
                    str(row.coverImg),
                    timeout=(10, 30),
                    stream=True,
                ) as response:

                    response.raise_for_status()

                    size = 0

                    with temp.open("wb") as file:
                        for chunk in response.iter_content(65536):
                            size += len(chunk)

                            if size > MAX_BYTES:
                                raise ValueError("Dosya çok büyük")

                            file.write(chunk)

                # Dosyanın görüntü olarak okunabildiğini doğrula
                with Image.open(temp) as image:
                    image.verify()

                with Image.open(temp) as image:
                    if image.width * image.height > 35_000_000:
                        raise ValueError("Görüntü boyutu çok büyük")

                    image.convert("RGB").save(
                        converted, format="JPEG", quality=90
                    )

                converted.replace(output)
                downloaded += 1

            except Exception as error:
                failed += 1
                writer.writerow([
                    row.filename,
                    str(error)[:200]
                ])
                log.flush()

            finally:
                temp.unlink(missing_ok=True)
                converted.unlink(missing_ok=True)

            if i % 100 == 0 or i == len(df):
                print(
                    f"{i}/{len(df)} | "
                    f"İndirilen: {downloaded} | "
                    f"Mevcut: {skipped} | "
                    f"Hata: {failed}",
                    flush=True
                )

            # Sunucuyu aşırı yüklememek için
            time.sleep(0.5)

finally:
    session.close()

print("\nİndirme işlemi sona erdi.")
print("Yeni indirilen:", downloaded)
print("Mevcut:", skipped)
print("Başarısız:", failed)
