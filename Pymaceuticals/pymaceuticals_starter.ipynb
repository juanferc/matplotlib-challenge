{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Observations and Insights "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Observations\n",
    "\n",
    "#Based on the bar charts, Capomulin and Ramican are the regimens used the most to treat mice\n",
    "#Looking at the pie charts, it seems the mice population is equally divided between female and male mice\n",
    "#In the scatter plot, one can see a strong positive relation between a mouse's weight and the average tumor weight "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mouse ID</th>\n",
       "      <th>Timepoint</th>\n",
       "      <th>Tumor Volume (mm3)</th>\n",
       "      <th>Metastatic Sites</th>\n",
       "      <th>Drug Regimen</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age_months</th>\n",
       "      <th>Weight (g)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>b128</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Capomulin</td>\n",
       "      <td>Female</td>\n",
       "      <td>9</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>f932</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Ketapril</td>\n",
       "      <td>Male</td>\n",
       "      <td>15</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>g107</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Ketapril</td>\n",
       "      <td>Female</td>\n",
       "      <td>2</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>a457</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Ketapril</td>\n",
       "      <td>Female</td>\n",
       "      <td>11</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>c819</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Ketapril</td>\n",
       "      <td>Male</td>\n",
       "      <td>21</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Mouse ID  Timepoint  Tumor Volume (mm3)  Metastatic Sites Drug Regimen  \\\n",
       "0     b128          0                45.0                 0    Capomulin   \n",
       "1     f932          0                45.0                 0     Ketapril   \n",
       "2     g107          0                45.0                 0     Ketapril   \n",
       "3     a457          0                45.0                 0     Ketapril   \n",
       "4     c819          0                45.0                 0     Ketapril   \n",
       "\n",
       "      Sex  Age_months  Weight (g)  \n",
       "0  Female           9          22  \n",
       "1    Male          15          29  \n",
       "2  Female           2          29  \n",
       "3  Female          11          30  \n",
       "4    Male          21          25  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Dependencies and Setup\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import scipy.stats as st\n",
    "\n",
    "# Study data files\n",
    "mouse_metadata_path = \"data/Mouse_metadata.csv\"\n",
    "study_results_path = \"data/Study_results.csv\"\n",
    "\n",
    "# Read the mouse data and the study results\n",
    "mouse_metadata = pd.read_csv(mouse_metadata_path)\n",
    "study_results = pd.read_csv(study_results_path)\n",
    "\n",
    "# Combine the data into a single dataset\n",
    "combined_df = pd.merge(study_results,mouse_metadata, how=\"left\",on=\"Mouse ID\")\n",
    "\n",
    "# Display the data table for preview\n",
    "combined_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "249"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Checking the number of mice.\n",
    "len(combined_df[\"Mouse ID\"].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['g989'], dtype=object)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Getting the duplicate mice by ID number that shows up for Mouse ID and Timepoint. \n",
    "duplicate_mice = combined_df.loc[combined_df.duplicated(subset=['Mouse ID', 'Timepoint']),'Mouse ID'].unique()\n",
    "duplicate_mice"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mouse ID</th>\n",
       "      <th>Timepoint</th>\n",
       "      <th>Tumor Volume (mm3)</th>\n",
       "      <th>Metastatic Sites</th>\n",
       "      <th>Drug Regimen</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age_months</th>\n",
       "      <th>Weight (g)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>107</th>\n",
       "      <td>g989</td>\n",
       "      <td>0</td>\n",
       "      <td>45.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>137</th>\n",
       "      <td>g989</td>\n",
       "      <td>0</td>\n",
       "      <td>45.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>329</th>\n",
       "      <td>g989</td>\n",
       "      <td>5</td>\n",
       "      <td>48.786801</td>\n",
       "      <td>0</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>360</th>\n",
       "      <td>g989</td>\n",
       "      <td>5</td>\n",
       "      <td>47.570392</td>\n",
       "      <td>0</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>620</th>\n",
       "      <td>g989</td>\n",
       "      <td>10</td>\n",
       "      <td>51.745156</td>\n",
       "      <td>0</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>681</th>\n",
       "      <td>g989</td>\n",
       "      <td>10</td>\n",
       "      <td>49.880528</td>\n",
       "      <td>0</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>815</th>\n",
       "      <td>g989</td>\n",
       "      <td>15</td>\n",
       "      <td>51.325852</td>\n",
       "      <td>1</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>869</th>\n",
       "      <td>g989</td>\n",
       "      <td>15</td>\n",
       "      <td>53.442020</td>\n",
       "      <td>0</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>950</th>\n",
       "      <td>g989</td>\n",
       "      <td>20</td>\n",
       "      <td>55.326122</td>\n",
       "      <td>1</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1111</th>\n",
       "      <td>g989</td>\n",
       "      <td>20</td>\n",
       "      <td>54.657650</td>\n",
       "      <td>1</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1195</th>\n",
       "      <td>g989</td>\n",
       "      <td>25</td>\n",
       "      <td>56.045564</td>\n",
       "      <td>1</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1380</th>\n",
       "      <td>g989</td>\n",
       "      <td>30</td>\n",
       "      <td>59.082294</td>\n",
       "      <td>1</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1592</th>\n",
       "      <td>g989</td>\n",
       "      <td>35</td>\n",
       "      <td>62.570880</td>\n",
       "      <td>2</td>\n",
       "      <td>Propriva</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Mouse ID  Timepoint  Tumor Volume (mm3)  Metastatic Sites Drug Regimen  \\\n",
       "107      g989          0           45.000000                 0     Propriva   \n",
       "137      g989          0           45.000000                 0     Propriva   \n",
       "329      g989          5           48.786801                 0     Propriva   \n",
       "360      g989          5           47.570392                 0     Propriva   \n",
       "620      g989         10           51.745156                 0     Propriva   \n",
       "681      g989         10           49.880528                 0     Propriva   \n",
       "815      g989         15           51.325852                 1     Propriva   \n",
       "869      g989         15           53.442020                 0     Propriva   \n",
       "950      g989         20           55.326122                 1     Propriva   \n",
       "1111     g989         20           54.657650                 1     Propriva   \n",
       "1195     g989         25           56.045564                 1     Propriva   \n",
       "1380     g989         30           59.082294                 1     Propriva   \n",
       "1592     g989         35           62.570880                 2     Propriva   \n",
       "\n",
       "         Sex  Age_months  Weight (g)  \n",
       "107   Female          21          26  \n",
       "137   Female          21          26  \n",
       "329   Female          21          26  \n",
       "360   Female          21          26  \n",
       "620   Female          21          26  \n",
       "681   Female          21          26  \n",
       "815   Female          21          26  \n",
       "869   Female          21          26  \n",
       "950   Female          21          26  \n",
       "1111  Female          21          26  \n",
       "1195  Female          21          26  \n",
       "1380  Female          21          26  \n",
       "1592  Female          21          26  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Optional: Get all the data for the duplicate mouse ID. \n",
    "duplicate_data = combined_df.loc[combined_df[\"Mouse ID\"] == \"g989\"]\n",
    "duplicate_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mouse ID</th>\n",
       "      <th>Timepoint</th>\n",
       "      <th>Tumor Volume (mm3)</th>\n",
       "      <th>Metastatic Sites</th>\n",
       "      <th>Drug Regimen</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age_months</th>\n",
       "      <th>Weight (g)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>b128</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Capomulin</td>\n",
       "      <td>Female</td>\n",
       "      <td>9</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>f932</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Ketapril</td>\n",
       "      <td>Male</td>\n",
       "      <td>15</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>g107</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Ketapril</td>\n",
       "      <td>Female</td>\n",
       "      <td>2</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>a457</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Ketapril</td>\n",
       "      <td>Female</td>\n",
       "      <td>11</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>c819</td>\n",
       "      <td>0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>0</td>\n",
       "      <td>Ketapril</td>\n",
       "      <td>Male</td>\n",
       "      <td>21</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Mouse ID  Timepoint  Tumor Volume (mm3)  Metastatic Sites Drug Regimen  \\\n",
       "0     b128          0                45.0                 0    Capomulin   \n",
       "1     f932          0                45.0                 0     Ketapril   \n",
       "2     g107          0                45.0                 0     Ketapril   \n",
       "3     a457          0                45.0                 0     Ketapril   \n",
       "4     c819          0                45.0                 0     Ketapril   \n",
       "\n",
       "      Sex  Age_months  Weight (g)  \n",
       "0  Female           9          22  \n",
       "1    Male          15          29  \n",
       "2  Female           2          29  \n",
       "3  Female          11          30  \n",
       "4    Male          21          25  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a clean DataFrame by dropping the duplicate mouse by its ID.\n",
    "cleaned_df = combined_df[combined_df['Mouse ID'].isin(duplicate_mice)==False]\n",
    "cleaned_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "248"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Checking the number of mice in the clean DataFrame.\n",
    "len(cleaned_df[\"Mouse ID\"].unique())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Summary Statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mean</th>\n",
       "      <th>Median</th>\n",
       "      <th>Variance</th>\n",
       "      <th>Standard Deviation</th>\n",
       "      <th>SEM</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Drug Regimen</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Capomulin</th>\n",
       "      <td>40.675741</td>\n",
       "      <td>41.557809</td>\n",
       "      <td>24.947764</td>\n",
       "      <td>4.994774</td>\n",
       "      <td>0.329346</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ceftamin</th>\n",
       "      <td>52.591172</td>\n",
       "      <td>51.776157</td>\n",
       "      <td>39.290177</td>\n",
       "      <td>6.268188</td>\n",
       "      <td>0.469821</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Infubinol</th>\n",
       "      <td>52.884795</td>\n",
       "      <td>51.820584</td>\n",
       "      <td>43.128684</td>\n",
       "      <td>6.567243</td>\n",
       "      <td>0.492236</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ketapril</th>\n",
       "      <td>55.235638</td>\n",
       "      <td>53.698743</td>\n",
       "      <td>68.553577</td>\n",
       "      <td>8.279709</td>\n",
       "      <td>0.603860</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Naftisol</th>\n",
       "      <td>54.331565</td>\n",
       "      <td>52.509285</td>\n",
       "      <td>66.173479</td>\n",
       "      <td>8.134708</td>\n",
       "      <td>0.596466</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Placebo</th>\n",
       "      <td>54.033581</td>\n",
       "      <td>52.288934</td>\n",
       "      <td>61.168083</td>\n",
       "      <td>7.821003</td>\n",
       "      <td>0.581331</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Propriva</th>\n",
       "      <td>52.320930</td>\n",
       "      <td>50.446266</td>\n",
       "      <td>43.852013</td>\n",
       "      <td>6.622085</td>\n",
       "      <td>0.544332</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ramicane</th>\n",
       "      <td>40.216745</td>\n",
       "      <td>40.673236</td>\n",
       "      <td>23.486704</td>\n",
       "      <td>4.846308</td>\n",
       "      <td>0.320955</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Stelasyn</th>\n",
       "      <td>54.233149</td>\n",
       "      <td>52.431737</td>\n",
       "      <td>59.450562</td>\n",
       "      <td>7.710419</td>\n",
       "      <td>0.573111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Zoniferol</th>\n",
       "      <td>53.236507</td>\n",
       "      <td>51.818479</td>\n",
       "      <td>48.533355</td>\n",
       "      <td>6.966589</td>\n",
       "      <td>0.516398</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   Mean     Median   Variance  Standard Deviation       SEM\n",
       "Drug Regimen                                                               \n",
       "Capomulin     40.675741  41.557809  24.947764            4.994774  0.329346\n",
       "Ceftamin      52.591172  51.776157  39.290177            6.268188  0.469821\n",
       "Infubinol     52.884795  51.820584  43.128684            6.567243  0.492236\n",
       "Ketapril      55.235638  53.698743  68.553577            8.279709  0.603860\n",
       "Naftisol      54.331565  52.509285  66.173479            8.134708  0.596466\n",
       "Placebo       54.033581  52.288934  61.168083            7.821003  0.581331\n",
       "Propriva      52.320930  50.446266  43.852013            6.622085  0.544332\n",
       "Ramicane      40.216745  40.673236  23.486704            4.846308  0.320955\n",
       "Stelasyn      54.233149  52.431737  59.450562            7.710419  0.573111\n",
       "Zoniferol     53.236507  51.818479  48.533355            6.966589  0.516398"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen\n",
    "new_data = cleaned_df.groupby(\"Drug Regimen\")[\"Tumor Volume (mm3)\"]\n",
    "Mean = new_data.mean()\n",
    "Median = new_data.median()\n",
    "Variance = new_data.var()\n",
    "STD = new_data.std()\n",
    "SEM = new_data.sem()\n",
    "# This method is the most straighforward, creating multiple series and putting them all together at the end.\n",
    "\n",
    "statistics_df = pd.DataFrame({\"Mean\": Mean,\n",
    "                             \"Median\": Median,\n",
    "                             \"Variance\": Variance,\n",
    "                             \"Standard Deviation\": STD,\n",
    "                             \"SEM\": SEM})\n",
    "statistics_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mean</th>\n",
       "      <th>Median</th>\n",
       "      <th>Variance</th>\n",
       "      <th>Standard Deviation</th>\n",
       "      <th>SEM</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>10.000000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>10.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>50.975982</td>\n",
       "      <td>49.902123</td>\n",
       "      <td>47.858440</td>\n",
       "      <td>6.821103</td>\n",
       "      <td>0.502785</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>5.621289</td>\n",
       "      <td>4.705415</td>\n",
       "      <td>16.008423</td>\n",
       "      <td>1.216096</td>\n",
       "      <td>0.103473</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>40.216745</td>\n",
       "      <td>40.673236</td>\n",
       "      <td>23.486704</td>\n",
       "      <td>4.846308</td>\n",
       "      <td>0.320955</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>52.388490</td>\n",
       "      <td>50.778739</td>\n",
       "      <td>40.249804</td>\n",
       "      <td>6.342952</td>\n",
       "      <td>0.475424</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>53.060651</td>\n",
       "      <td>51.819532</td>\n",
       "      <td>46.192684</td>\n",
       "      <td>6.794337</td>\n",
       "      <td>0.530365</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>54.183257</td>\n",
       "      <td>52.396036</td>\n",
       "      <td>60.738703</td>\n",
       "      <td>7.793357</td>\n",
       "      <td>0.579276</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>55.235638</td>\n",
       "      <td>53.698743</td>\n",
       "      <td>68.553577</td>\n",
       "      <td>8.279709</td>\n",
       "      <td>0.603860</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Mean     Median   Variance  Standard Deviation        SEM\n",
       "count  10.000000  10.000000  10.000000           10.000000  10.000000\n",
       "mean   50.975982  49.902123  47.858440            6.821103   0.502785\n",
       "std     5.621289   4.705415  16.008423            1.216096   0.103473\n",
       "min    40.216745  40.673236  23.486704            4.846308   0.320955\n",
       "25%    52.388490  50.778739  40.249804            6.342952   0.475424\n",
       "50%    53.060651  51.819532  46.192684            6.794337   0.530365\n",
       "75%    54.183257  52.396036  60.738703            7.793357   0.579276\n",
       "max    55.235638  53.698743  68.553577            8.279709   0.603860"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen\n",
    "# This method produces everything in a single groupby function\n",
    "new_stats_df = statistics_df.describe()\n",
    "new_stats_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Bar and Pie Charts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a bar plot showing the total number of mice for each treatment throughout the course of the study using pandas. \n",
    "mice_treatment = cleaned_df.groupby(\"Drug Regimen\")[\"Timepoint\"].count()\n",
    "mice_treatment.plot(kind=\"bar\",color=\"red\")\n",
    "plt.xlabel(\"Drug Regimen\")\n",
    "plt.ylabel(\"Number of Mice\")\n",
    "plt.title(\"Number of Mice Per Treatment\")\n",
    "plt.xticks(rotation=45)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], <a list of 10 Text xticklabel objects>)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a bar plot showing the total number of mice for each treatment throughout the course of the study using pyplot.\n",
    "new_x_axis = mice_treatment.index.tolist()\n",
    "x_axis = new_x_axis\n",
    "y_axis = mice_treatment \n",
    "plt.bar(x_axis,y_axis,color=\"red\",align=\"center\")\n",
    "plt.ylabel(\"Number of mice\")\n",
    "plt.xlabel(\"Drug Regimen\")\n",
    "plt.title(\"Number of Mice Per Treatment\")\n",
    "plt.xticks(rotation=45)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a pie plot showing the distribution of female versus male mice using pandas\n",
    "gender_df = cleaned_df.groupby(\"Sex\").count()\n",
    "grouped_by_gender = gender_df[[\"Mouse ID\"]]\n",
    "grouped_by_gender = grouped_by_gender.rename(columns={\"Mouse ID\": \"Percentage\"})\n",
    "grouped_by_gender\n",
    "colors = [\"lightblue\",\"orange\"]\n",
    "grouped_by_gender.plot.pie(y=\"Percentage\",colors=colors,startangle=50\n",
    "                           ,shadow=True,autopct=\"%1.1f%%\")\n",
    "plt.title(\"Distribution of Mice Based on Gender\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/juanferc/opt/anaconda3/envs/PythonData/lib/python3.6/site-packages/ipykernel_launcher.py:5: MatplotlibDeprecationWarning: Non-1D inputs to pie() are currently squeeze()d, but this behavior is deprecated since 3.1 and will be removed in 3.3; pass a 1D array instead.\n",
      "  \"\"\"\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a pie plot showing the distribution of female versus male mice using pyplot\n",
    "labels = [\"Female\", \"Male\"]\n",
    "new_count_df = grouped_by_gender\n",
    "plt.pie(new_count_df,labels=labels,colors=colors,startangle=50\n",
    "                           ,shadow=True,autopct=\"%1.1f%%\")\n",
    "plt.legend(labels,loc=\"upper right\")\n",
    "plt.title(\"Distribution of Mice Based on Gender\")\n",
    "plt.ylabel(\"Percentage\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Quartiles, Outliers and Boxplots"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mouse ID</th>\n",
       "      <th>Timepoint</th>\n",
       "      <th>Tumor Volume (mm3)</th>\n",
       "      <th>Metastatic Sites</th>\n",
       "      <th>Drug Regimen</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age_months</th>\n",
       "      <th>Weight (g)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a203</td>\n",
       "      <td>45</td>\n",
       "      <td>67.973419</td>\n",
       "      <td>2</td>\n",
       "      <td>Infubinol</td>\n",
       "      <td>Female</td>\n",
       "      <td>20</td>\n",
       "      <td>23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>a251</td>\n",
       "      <td>45</td>\n",
       "      <td>65.525743</td>\n",
       "      <td>1</td>\n",
       "      <td>Infubinol</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>a275</td>\n",
       "      <td>45</td>\n",
       "      <td>62.999356</td>\n",
       "      <td>3</td>\n",
       "      <td>Ceftamin</td>\n",
       "      <td>Female</td>\n",
       "      <td>20</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>a411</td>\n",
       "      <td>45</td>\n",
       "      <td>38.407618</td>\n",
       "      <td>1</td>\n",
       "      <td>Ramicane</td>\n",
       "      <td>Male</td>\n",
       "      <td>3</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>a444</td>\n",
       "      <td>45</td>\n",
       "      <td>43.047543</td>\n",
       "      <td>0</td>\n",
       "      <td>Ramicane</td>\n",
       "      <td>Female</td>\n",
       "      <td>10</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>y769</td>\n",
       "      <td>45</td>\n",
       "      <td>68.594745</td>\n",
       "      <td>4</td>\n",
       "      <td>Ceftamin</td>\n",
       "      <td>Female</td>\n",
       "      <td>6</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96</th>\n",
       "      <td>y793</td>\n",
       "      <td>45</td>\n",
       "      <td>31.896238</td>\n",
       "      <td>2</td>\n",
       "      <td>Capomulin</td>\n",
       "      <td>Male</td>\n",
       "      <td>17</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>97</th>\n",
       "      <td>y865</td>\n",
       "      <td>45</td>\n",
       "      <td>64.729837</td>\n",
       "      <td>3</td>\n",
       "      <td>Ceftamin</td>\n",
       "      <td>Male</td>\n",
       "      <td>23</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>z578</td>\n",
       "      <td>45</td>\n",
       "      <td>30.638696</td>\n",
       "      <td>0</td>\n",
       "      <td>Ramicane</td>\n",
       "      <td>Male</td>\n",
       "      <td>11</td>\n",
       "      <td>16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>z581</td>\n",
       "      <td>45</td>\n",
       "      <td>62.754451</td>\n",
       "      <td>3</td>\n",
       "      <td>Infubinol</td>\n",
       "      <td>Female</td>\n",
       "      <td>24</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   Mouse ID  Timepoint  Tumor Volume (mm3)  Metastatic Sites Drug Regimen  \\\n",
       "0      a203         45           67.973419                 2    Infubinol   \n",
       "1      a251         45           65.525743                 1    Infubinol   \n",
       "2      a275         45           62.999356                 3     Ceftamin   \n",
       "3      a411         45           38.407618                 1     Ramicane   \n",
       "4      a444         45           43.047543                 0     Ramicane   \n",
       "..      ...        ...                 ...               ...          ...   \n",
       "95     y769         45           68.594745                 4     Ceftamin   \n",
       "96     y793         45           31.896238                 2    Capomulin   \n",
       "97     y865         45           64.729837                 3     Ceftamin   \n",
       "98     z578         45           30.638696                 0     Ramicane   \n",
       "99     z581         45           62.754451                 3    Infubinol   \n",
       "\n",
       "       Sex  Age_months  Weight (g)  \n",
       "0   Female          20          23  \n",
       "1   Female          21          25  \n",
       "2   Female          20          28  \n",
       "3     Male           3          22  \n",
       "4   Female          10          25  \n",
       "..     ...         ...         ...  \n",
       "95  Female           6          27  \n",
       "96    Male          17          17  \n",
       "97    Male          23          26  \n",
       "98    Male          11          16  \n",
       "99  Female          24          25  \n",
       "\n",
       "[100 rows x 8 columns]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate the final tumor volume of each mouse across four of the treatment regimens:  \n",
    "# Capomulin, Ramicane, Infubinol, and Ceftamin\n",
    "treatments = [\"Capomulin\", \"Ramicane\", \"Infubinol\", \"Ceftamin\"]\n",
    "\n",
    "# Start by getting the last (greatest) timepoint for each mouse\n",
    "timepoint_df = cleaned_df[[\"Mouse ID\",\"Timepoint\",\"Drug Regimen\"]]\n",
    "new_cleaned_df = timepoint_df[timepoint_df[\"Drug Regimen\"].isin(treatments)]\n",
    "group_df = new_cleaned_df.groupby(\"Mouse ID\")[\"Timepoint\"].max()\n",
    "\n",
    "# Merge this group df with the original dataframe to get the tumor volume at the last timepoint\n",
    "merged_df = pd.merge(group_df,cleaned_df,on=[\"Mouse ID\",\"Timepoint\"],how=\"left\")\n",
    "merged_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Capomulin outliers could be values below 20.704562 and above 51.832015 could be outliers\n"
     ]
    }
   ],
   "source": [
    "cap_df = merged_df.loc[merged_df[\"Drug Regimen\"] == \"Capomulin\",:]\n",
    "ram_df = merged_df.loc[merged_df[\"Drug Regimen\"] == \"Ramicane\", :]\n",
    "inf_df = merged_df.loc[merged_df[\"Drug Regimen\"] == \"Infubinol\", :]\n",
    "ceft_df = merged_df.loc[merged_df[\"Drug Regimen\"] == \"Ceftamin\", :]\n",
    "\n",
    "new_cap_df = cap_df.groupby('Mouse ID').max()['Timepoint']\n",
    "cap_vol = pd.DataFrame(new_cap_df)\n",
    "cap_merged = pd.merge(cap_vol, merged_df, on=(\"Mouse ID\",\"Timepoint\"),how=\"left\")\n",
    "\n",
    "volume = cap_merged[\"Tumor Volume (mm3)\"]\n",
    "quartiles = volume.quantile([.25,.5,.75])\n",
    "\n",
    "lower_q = quartiles[0.25]\n",
    "upper_q = quartiles[0.75]\n",
    "median = quartiles[0.5]\n",
    "iqr = upper_q - lower_q\n",
    "\n",
    "new_lower = round(lower_q,6)\n",
    "new_upper = round(upper_q,6)\n",
    "new_iqr = round(iqr,6)\n",
    "\n",
    "lower_limit = lower_q - (1.5*iqr)\n",
    "upper_limit = upper_q + (1.5*iqr)\n",
    "new_lowerl = round(lower_limit,6)\n",
    "new_upperl = round(upper_limit,6)\n",
    "\n",
    "print(\"Capomulin outliers could be values below \" + str(new_lowerl) + \" and above \" + str(new_upperl) + \" could be outliers\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ramicane outliers could be values below 17.912664 and above 54.306811 could be outliers\n"
     ]
    }
   ],
   "source": [
    "new_ram_df = ram_df.groupby(\"Mouse ID\").max()[\"Timepoint\"]\n",
    "ram_vol = pd.DataFrame(new_ram_df)\n",
    "ram_merged = pd.merge(ram_vol, merged_df, on=(\"Mouse ID\",\"Timepoint\"),how=\"left\")\n",
    "\n",
    "volume2 = ram_merged[\"Tumor Volume (mm3)\"]\n",
    "quartiles = volume2.quantile([.25,.5,.75])\n",
    "\n",
    "lower_q = quartiles[0.25]\n",
    "upper_q = quartiles[0.75]\n",
    "median = quartiles[0.5]\n",
    "iqr = upper_q - lower_q\n",
    "\n",
    "new_lower = round(lower_q,6)\n",
    "new_upper = round(upper_q,6)\n",
    "new_iqr = round(iqr,6)\n",
    "\n",
    "lower_limit = lower_q - (1.5*iqr)\n",
    "upper_limit = upper_q + (1.5*iqr)\n",
    "new_lowerl = round(lower_limit,6)\n",
    "new_upperl = round(upper_limit,6)\n",
    "\n",
    "print(\"Ramicane outliers could be values below \" + str(new_lowerl) + \" and above \" + str(new_upperl) + \" could be outliers\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Infubinol outliers could be values below 36.832905 and above 82.741446 could be outliers\n"
     ]
    }
   ],
   "source": [
    "new_inf_df = inf_df.groupby(\"Mouse ID\").max()[\"Timepoint\"]\n",
    "inf_vol = pd.DataFrame(new_inf_df)\n",
    "inf_merged = pd.merge(inf_vol, merged_df, on=(\"Mouse ID\",\"Timepoint\"),how=\"left\")\n",
    "\n",
    "volume3 = inf_merged[\"Tumor Volume (mm3)\"]\n",
    "quartiles = volume3.quantile([.25,.5,.75])\n",
    "\n",
    "lower_q = quartiles[0.25]\n",
    "upper_q = quartiles[0.75]\n",
    "median = quartiles[0.5]\n",
    "iqr = upper_q - lower_q\n",
    "\n",
    "new_lower = round(lower_q,6)\n",
    "new_upper = round(upper_q,6)\n",
    "new_iqr = round(iqr,6)\n",
    "\n",
    "lower_limit = lower_q - (1.5*iqr)\n",
    "upper_limit = upper_q + (1.5*iqr)\n",
    "new_lowerl = round(lower_limit,6)\n",
    "new_upperl = round(upper_limit,6)\n",
    "\n",
    "print(\"Infubinol outliers could be values below \" + str(new_lowerl) + \" and above \" + str(new_upperl) + \" could be outliers\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ceftamin outliers could be values below 25.35545 and above 87.666458 could be outliers\n"
     ]
    }
   ],
   "source": [
    "new_ceft_df = ceft_df.groupby('Mouse ID').max()['Timepoint']\n",
    "ceft_vol = pd.DataFrame(new_ceft_df)\n",
    "ceft_merged = pd.merge(ceft_vol, merged_df, on=(\"Mouse ID\",\"Timepoint\"),how=\"left\")\n",
    "\n",
    "volume4 = ceft_merged[\"Tumor Volume (mm3)\"]\n",
    "quartiles = volume4.quantile([.25,.5,.75])\n",
    "\n",
    "lower_q = quartiles[0.25]\n",
    "upper_q = quartiles[0.75]\n",
    "median = quartiles[0.5]\n",
    "iqr = upper_q - lower_q\n",
    "\n",
    "new_lower = round(lower_q,6)\n",
    "new_upper = round(upper_q,6)\n",
    "new_iqr = round(iqr,6)\n",
    "\n",
    "lower_limit = lower_q - (1.5*iqr)\n",
    "upper_limit = upper_q + (1.5*iqr)\n",
    "new_lowerl = round(lower_limit,6)\n",
    "new_upperl = round(upper_limit,6)\n",
    "\n",
    "print(\"Ceftamin outliers could be values below \" + str(new_lowerl) + \" and above \" + str(new_upperl) + \" could be outliers\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a box plot of the final tumor volume of each mouse across four regimens of interest\n",
    "boxplot_data = [volume,volume2,volume3,volume4]\n",
    "\n",
    "fig, plot = plt.subplots()\n",
    "plot.set_title(\"Tumors Volume Across Regimens\")\n",
    "plot.set_ylabel(\"Tumor Volume (mm3)\")\n",
    "plot.set_xlabel(\"Drug Regimen\")\n",
    "\n",
    "plot.boxplot(boxplot_data, labels=[\"Capomulin\",\"Ramicane\",\"Infubinol\",\"Ceftamin\"])\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Line and Scatter Plots"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Tumor Volume (mm3)')"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a line plot of time point versus tumor volume for a mouse treated with Capomulin\n",
    "capomulin_df = combined_df.loc[combined_df[\"Drug Regimen\"]==\"Capomulin\"]\n",
    "mouse_id = capomulin_df.loc[capomulin_df[\"Mouse ID\"] == \"r944\"]\n",
    "\n",
    "line_df = mouse_id[[\"Timepoint\", \"Tumor Volume (mm3)\"]]\n",
    "line_plot = line_df.plot(kind=\"line\",x=\"Timepoint\",y=\"Tumor Volume (mm3)\",legend=False,title=\"Timepoint vs. Tumor Volume (mm3)\",marker=\"o\",color=\"r\")\n",
    "line_plot.set_xlabel(\"Timepoint\")\n",
    "line_plot.set_ylabel(\"Tumor Volume (mm3)\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a scatter plot of mouse weight versus average tumor volume for the Capomulin regimen\n",
    "plot_df = cap_df.groupby([\"Mouse ID\"]).mean()\n",
    "plt.scatter(plot_df[\"Weight (g)\"],plot_df[\"Tumor Volume (mm3)\"],color=\"r\")\n",
    "plt.title(\"Mouse Weight vs. Average Tumor Volume (Capomulin)\")\n",
    "plt.xlabel(\"Weight (g)\")\n",
    "plt.ylabel(\"Average Tumor Volume (mm3)\")\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Correlation and Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The correlation between mouse weight and average tumor volume is: 0.88\n"
     ]
    }
   ],
   "source": [
    "# Calculate the correlation coefficient and linear regression model \n",
    "# for mouse weight and average tumor volume for the Capomulin regimen\n",
    "correlation = round(st.pearsonr(plot_df[\"Weight (g)\"],plot_df[\"Tumor Volume (mm3)\"])[0],2)\n",
    "print(\"The correlation between mouse weight and average tumor volume is: \" + str(correlation))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinregressResult(slope=1.750468228958504, intercept=1.4481469525549002, rvalue=0.8767060403658119, pvalue=9.0844290886732e-09, stderr=0.20026513236453639)"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = st.linregress(plot_df[\"Weight (g)\"],plot_df[\"Tumor Volume (mm3)\"])\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "slope = 1.750468228958504\n",
    "intercept = 1.4481469525549002"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "y_values = plot_df[\"Weight (g)\"] * slope + intercept\n",
    "plt.scatter(plot_df[\"Weight (g)\"],plot_df[\"Tumor Volume (mm3)\"])\n",
    "plt.plot(plot_df[\"Weight (g)\"], y_values, color=\"r\")\n",
    "plt.xlabel(\"Weight(g)\")\n",
    "plt.ylabel(\"Average Tumore Volume (mm3)\")\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
