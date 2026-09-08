import os
from pathlib import Path
from PIL import Image
try:
    from tqdm import tqdm
except ImportError:
    tqdm = lambda x, **kwargs: x

CLASSES = {
    "0": "Bread",
    "1": "Dairy product",
    "2": "Dessert",
    "3": "Egg",
    "4": "Fried food",
    "5": "Meat",
    "6": "Noodles-Pasta",
    "7": "Rice",
    "8": "Seafood",
    "9": "Soup",
    "10": "Vegetable-Fruit"
}

def process_dataset(src_dir: Path, dest_dir: Path, mini: bool = False):
    """Processes the dataset by resizing and categorizing images."""
    splits = ["training", "validation", "evaluation"]
    
    for split in splits:
        split_src = src_dir / split
        if not split_src.exists():
            continue
            
        print(f"Processing {split} -> {dest_dir.name}")
        
        # Keep track of counts for the mini dataset
        category_counts = {c: 0 for c in CLASSES.values()}
        files = list(split_src.glob("*.jpg"))
        
        for file in tqdm(files, desc=split):
            # Filename format: {class_id}_{id}.jpg
            prefix = file.name.split('_')[0]
            if prefix not in CLASSES:
                continue
                
            category = CLASSES[prefix]
            
            # Enforce the 100 image limit for mini dataset
            if mini and category_counts[category] >= 100:
                continue
                
            # Create the category directory if it doesn't exist
            category_dir = dest_dir / split / category
            category_dir.mkdir(parents=True, exist_ok=True)
            
            # Open, resize, and save the image
            try:
                img = Image.open(file)
                # Resize to 128x128 as requested
                img = img.resize((128, 128), Image.Resampling.LANCZOS)
                
                # Convert to RGB to ensure uniform format
                if img.mode != "RGB":
                    img = img.convert("RGB")
                    
                img.save(category_dir / file.name)
                category_counts[category] += 1
            except Exception as e:
                print(f"Failed to process {file.name}: {e}")

def main():
    # Resolve paths relative to this script
    base_dir = Path(__file__).parent.parent.parent / "data"
    raw_dir = base_dir / "food11_raw"
    processed_dir = base_dir / "food11_processed"
    processed_mini_dir = base_dir / "food11_processed_mini"
    
    print("--- Creating food11_processed ---")
    process_dataset(raw_dir, processed_dir, mini=False)
    
    print("\n--- Creating food11_processed_mini ---")
    process_dataset(raw_dir, processed_mini_dir, mini=True)
    
    print("\nFinished processing datasets!")

if __name__ == "__main__":
    main()
