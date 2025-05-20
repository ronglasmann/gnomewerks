set -e

. dev-cycle-env.sh

python -m pip config unset global.index-url  || true

# get the latest pip and build modules
python -m pip install --upgrade pip
python -m pip install --upgrade build

mkdir -p ./build

# temporary until these libs are published
#python -m build ../../Glasmann.net/gwerks
#cp ../../Glasmann.net/gwerks/dist/gwerks-25.2.13.tar.gz ./build
#python -m pip install ./build/gwerks-25.2.13.tar.gz
#python -m build ../../Glasmann.net/fwq
#cp ../../Glasmann.net/fwq/dist/fwq-0.0.0.tar.gz ./build
#python -m pip install ./build/fwq-0.0.0.tar.gz

python -m pip install .

#python ./app_deploy.py -a install
#
#python ./app_deploy.py -a stop
#
#python ./app_deploy.py -a start

#fwq --action nq --for surveys_platform --broker 127.0.0.1 --job_type asp.api.jobs.dyndb.create_indexes_job --ttr 600

#docker logs -f surveys_worker_1
#docker ps

cnc --make box --debug True \
    --spec '{"int_length": 6, "int_width": 9, "int_height": 1.5, "units": "in"}' \
    --export_filepath ./build/box.svg
