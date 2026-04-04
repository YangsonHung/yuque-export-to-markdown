from lake.lake_setup import LakeToMd, normalize_markdown


def test_extract_body_strips_lake_prefix_before_html():
    file_json = {
        "doc": {
            "body_draft_asl": "lake<h2>标题</h2><p>正文</p>",
            "body": "<p>fallback</p>",
        }
    }

    result = LakeToMd._extract_body(file_json)

    assert result == "<h2>标题</h2><p>正文</p>"


def test_extract_body_keeps_plain_text_that_starts_with_lake():
    file_json = {
        "doc": {
            "body_draft_asl": "lake view is beautiful",
        }
    }

    result = LakeToMd._extract_body(file_json)

    assert result == "lake view is beautiful"


def test_normalize_markdown_strips_lake_prefix_before_heading():
    text = "lake## 标题\n\n正文\n"

    result = normalize_markdown(text)

    assert result == "## 标题\n\n正文\n"


def test_normalize_markdown_keeps_normal_lake_text():
    text = "lake view is beautiful\n"

    result = normalize_markdown(text)

    assert result == "lake view is beautiful\n"
