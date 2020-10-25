# test script for scm
mkdir -p scm_test
cd scm_test

if [[ ! -f RS2_OK76385_PK678063_DK606752_FQ2_20080415_143807_HH_VV_HV_VH_SLC.zip ]]
then
  wget https://mdacorporation.com/geospatial/international/satellites/RADARSAT-2/sample-data/RS2_OK76385_PK678063_DK606752_FQ2_20080415_143807_HH_VV_HV_VH_SLC.zip 
fi

unzip RS2_OK76385_PK678063_DK606752_FQ2_20080415_143807_HH_VV_HV_VH_SLC.zip

mkdir -p s2
ers RS2_OK76385_PK678063_DK606752_FQ2_20080415_143807_HH_VV_HV_VH_SLC.zip s2
rm -rf RS2_OK76385_PK678063_DK606752_FQ2_20080415_143807_HH_VV_HV_VH_SLC*

mkdir -p scm
scm ./s2/ ./scm/ box 7 yes 3 4
