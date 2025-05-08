def styled_text(text, line_height=1.5):
    return f"""
        <div style='line-height: {line_height}; font-size: 16px;'>
            {text}
        </div>
    """