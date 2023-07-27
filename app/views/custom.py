def custom_entry_style():
    return {
        "Custom.TEntry": {
            "configure": {
                "padding": 5,
                "font": ("Helvetica", 12)
            },
            "map": {
                "background": [("active", "white"), ("focus", "white")],
                "fieldbackground": [("readonly", "gray90")]
            }
        }
    }