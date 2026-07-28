from pipeline.loader import discover_pdfs, load_metadata

pdfs = discover_pdfs()

print("=" * 50)
print("PDF FILES")
print("=" * 50)

for pdf in pdfs:
    print(pdf.name)

print()
print("=" * 50)
print("METADATA")
print("=" * 50)

metadata = load_metadata()

print(metadata.head())