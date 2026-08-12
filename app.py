def format_widget(w):
    """Return a display string for a widget record."""
    return f"{w['name']} (#{w['id']})"

if __name__ == "__main__":
    print(format_widget({"id": 7, "name": "sprocket"}))
