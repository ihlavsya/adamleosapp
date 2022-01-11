import re 

blue_diamond_unicode = "\U0001F539";
telegram_link_reg =r"\((https:\/\/t\.me\/adamleos\/[\d]*)\)"
ordinary_link_reg = r"(\[\d\])\(((?:http|ftp|https):\/\/(?:[\w\-_]+(?:(?:\.[\w\(\)\-_]+)+))(?:[\w\(\)\-\.,@?^=%&amp;:\/~\+#]*[\w\(\)\-\@?^=%&amp;\/~\+#])?)\)"
scihub_link_reg = r"(\[\d\])\((sci-hub\.(?:st|se|ru)\/(?:[\w\-_]+(?:(?:\.[\w\(\)\-_]+)+))(?:[\w\(\)\-\.,@?^=%&amp;:\/~\+#]*[\w\(\)\-\@?^=%&amp;\/~\+#])?)\)"
all_links_reg = ordinary_link_reg + "|" + scihub_link_reg

def remove_telegram_links(text):
    formatted_text = re.sub(telegram_link_reg, "", text)
    return formatted_text

def extract_links_from_post(text):
    links = re.findall(all_links_reg, text)
    return links

def remove_links(text):
    formatted_text = re.sub(r"(\[[\d]*\])\(.*\)", r"\1", text)
    return formatted_text

def get_all_refs(refs):
    all_refs = []
    ref_dict = {}
    for ref in refs:
        number = ref[0]
        link = ref[1]
        if number in ref_dict:
            continue
        ref_dict[number] = link
        new_ref = number + " " + link
        all_refs.append(new_ref)
    
    return all_refs

def format_text_for_fb(text, raw_text):
    splitters = raw_text.split("\n")
    header = splitters[0]
    raw_text = "\n".join(splitters[2:])
    header = "{} {} {}".format(blue_diamond_unicode, header.replace("\n", ""), blue_diamond_unicode)
    references = extract_links_from_post(text)

    raw_text = re.sub(r"\n\n", r"\n", raw_text)
    
    all_refs_string = "\n".join(get_all_refs(references))
    raw_text = raw_text + "\n\n" + all_refs_string
    formatted_text = header + "\n" + raw_text
    return formatted_text

if __name__ == "__main__":
    format_text_for_fb("sm", "sm")