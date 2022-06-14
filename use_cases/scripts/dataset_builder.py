import os
import pandas as pd

from pathlib import Path

SRC =  "/home/vieirapcm/projetos/Fake.Br-Corpus-FK/full_texts/"
DST = "/home/vieirapcm/projetos/fake_news_detection_ptbr/use_cases/fn_classifier/datasets/large_datasets/"
FILES = ["fake", "true"]
METADATA = "-metadata-information"

# 1. Open the repository
# 2. Get the [fake|true] text
# 3. Get the correspondent information in the metadata repository
# 4. Add the information about  category (line 4) and publication_date (line 5)
# 5. Generate the dataset and save into fn_classifier/datasets/base directory

for dir in FILES:
    txt_files = os.listdir(Path(__file__).parent.parent)
    txt_files = sorted(txt_files)

    print(txt_files)
    # dataset = []

    # for txt_file in txt_files:
    #     full_path = SRC + dir + "/" + txt_file
    #     with open(full_path, 'r') as f:
    #         content = f.read()
    #         content.strip()
    #         dataset.append(content.replace('\t', '').replace('\r', '').replace('\n', ''))

    # df = pd.DataFrame(dataset)
    # target = 1
    # if dir == "true":
    #     target = 0

    # df["target"] = target
    # df.to_csv(DST + dir + '.csv', sep=',', index=False)