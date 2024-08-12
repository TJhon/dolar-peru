import re


def extract_domain(url):
    # match = re.search(r"https?://(www\.)?([^/]+)", url)
    match = re.search(r"https?://(?:www\.|web\.)?([^./]+)", url)
    # match = re.search(r"https?://(?:www|web)\.?([^/]+)", url)
    if match:
        # domain = match.group(2).split(".")[0]
        domain = match.group(1)
        return domain
    return None
