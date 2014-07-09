#!/usr/bin/env python

import sys, re, json


def main():
	for l in sys.stdin:
		try:
			j = json.loads(l)
		except Exception:
			continue

		if "blogId" in j and "activity" in j and "isPrivate" in j and "timestamp" in j and "data" in j:
			
			if j["activity"] != "CreatePost" or "reblogged_from_url" in j["data"]:
				continue

			try:
				post_type = j["data"]["type"]
				if post_type == "photo":
					content_url = j["data"]["original_size"]["url"]
				elif post_type == "video":
					content_url = j["data"]["permalink_url"]
				else:
					continue
				blog_id  = str(j["blogId"])
				post_id  = str(j["id"])
				post_url = j["data"]["post_url"]
				ts       = str(j["timestamp"])
				caption  = j["data"]["caption"]
			except Exception:
				continue	
			
			if type(caption) is not str and type(caption) is not unicode:
				caption = ""
			tokens = re.split("\s+", caption)
			num_tokens = str(len(tokens))
			
			out = "\t".join([blog_id, post_id, post_url, post_type, content_url, ts, num_tokens])
			print out


if __name__ == "__main__":
    main()
