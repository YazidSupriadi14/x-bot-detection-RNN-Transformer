import json
import sys

def clean_notebook(path_in, path_out=None):
    if path_out is None:
        path_out = path_in.replace(".ipynb", "_clean.ipynb")

    print(f"Cleaning notebook: {path_in}")

    with open(path_in, "r", encoding="utf-8") as f:
        nb = json.load(f)

    # Hapus metadata widgets tingkat notebook
    if "metadata" in nb and "widgets" in nb["metadata"]:
        print("Removing notebook-level widgets metadata...")
        del nb["metadata"]["widgets"]

    # Hapus metadata widgets pada cell
    for cell in nb.get("cells", []):
        if "metadata" in cell and "widgets" in cell["metadata"]:
            print("Removing cell-level widget metadata...")
            del cell["metadata"]["widgets"]

    # Simpan file baru
    with open(path_out, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)

    print(f"Done! Clean file saved as: {path_out}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_notebook.py your_notebook.ipynb")
    else:
        clean_notebook(sys.argv[1])
