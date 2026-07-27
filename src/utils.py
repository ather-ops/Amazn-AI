import os
def print_heading(title: str):
    """
    Print a formatted heading.
    """
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

def print_product(doc):
    """
    Pretty print a retrieved product.
    """
    meta = doc.metadata
    print(f"Product : {meta.get('product_name', 'N/A')}")
    print(f"Price   : ₹{meta.get('discounted_price', 'N/A')}")
    print(f"Rating  : {meta.get('rating', 'N/A')}")
    print(f"Category: {meta.get('category', 'N/A')}")
    print(f"Link    : {meta.get('product_link', 'N/A')}")
    print(f"Image   : {meta.get('img_link', 'N/A')}")
    print("-" * 70)

def print_search_results(results):
    """
    Print all retrieved products.
    """
    if not results:
        print("No products found.")
        return
    for i, doc in enumerate(results, 1):
        print(f"\nResult {i}")
        print_product(doc)

def ensure_directory(path):
    """
    Create directory if it doesn't exist.
    """
    os.makedirs(path, exist_ok=True)

def file_exists(path):
    """
    Check if a file exists.
    """
    return os.path.exists(path)