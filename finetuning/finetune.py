from openai import OpenAI
import os
import json
import base64
import csv


client = OpenAI(api_key=os.getenv("ENV_VAR1"))

modelid='ft:gpt-4o-mini-2024-07-18:network-dynamics-lab::BIMvkIVN'

#client.files.create(
#  file=open("validation_SAFE.jsonl", "rb"),
#  purpose="fine-tune"
#)

#print(client.files.list())

#fileidtrain="file-EH45bvCiLArchrHG7Zmewt"
#fileidvalid="file-CsrYG5Ua8yG5rp5Gzacvic"

#client.fine_tuning.jobs.create(
#   training_file=fileidtrain,
#   model="gpt-4o-mini-2024-07-18",
#   validation_file=fileidvalid
#)

#print(client.fine_tuning.jobs.list(limit=10))

##jobid = "ftjob-MIEIKszEOXBlqPuMiNsvwrD2"
#print(client.fine_tuning.jobs.retrieve(jobid))


content = client.files.content('file-A9UGiGzkCbYfi3dezK6Kes')
content = content.read()
decoded_text = base64.b64decode(content).decode("utf-8")

with open("output.csv", "w", encoding="utf-8") as f:
    f.write(decoded_text)
