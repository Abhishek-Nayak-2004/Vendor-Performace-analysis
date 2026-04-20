{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e80046c2-7ed6-4585-8a9c-6874bbfe089f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(206529, 9)\n",
      "(224489, 9)\n",
      "(2372474, 16)\n",
      "(12261, 9)\n",
      "(12825363, 14)\n",
      "(5543, 10)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd \n",
    "import os \n",
    "from sqlalchemy import create_engine\n",
    "import logging\n",
    "import time\n",
    "logging.basicConfig(\n",
    "    filename= \"logs/ingestion_db.log\",\n",
    "    level= logging.DEBUG, \n",
    "    format=\"%(asctime)s - %(levelname)s - %(message)s\", \n",
    "    filemode=\"a\"\n",
    ")\n",
    "engine = create_engine('sqlite:///inventory.db') \n",
    "def ingest_db(df, table_name, engine):\n",
    "    df.to_sql(table_name,con = engine, if_exists = 'replace',index = False)\n",
    "def load_raw_data():\n",
    "    start = time.time()\n",
    "    for file in os.listdir('data'):\n",
    "        df = pd.read_csv('data/'+file)\n",
    "        print(df.shape) \n",
    "        logging.info(f'Ingesting {file} in db')\n",
    "        ingest_db(df,file[:-4], engine)\n",
    "    end = time.time()\n",
    "    total_time = (end-start)/60\n",
    "    logging.info('---------Ingestion Complete-----------')\n",
    "    logging.info(f'\\n Total time taken: {total_time} minutes')\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    load_raw_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "109d469e-77f7-4f62-a69c-173b616210d3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
