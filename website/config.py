from website.intros import intro


index_config = dict(
    title="Blake Smith",
    section_names=["Home", "Placeholder1", "Placeholder2"],
    show_intro=True,
    intro=intro.parse_intros_from_content_directory(),
    logo="Blake Anthony Smith",
)
