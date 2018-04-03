from flask import Flask, Response, request
import json

import ipinfo, ipapi, witch


app = Flask(__name__)


@app.route('/', methods=['GET'])
def root_endpoint():
    return Response(mimetype='application/json',
                    status=200,
                    response=json.dumps({'message': 'Running!'}))


@app.route('/ipsoft/fetch', methods=['GET'])
def fetch_ipsoft_endpoint():
    args = request.args
    if 'ip' not in args:
        return Response(status=400,
                        mimetype='application/json',
                        response=json.dumps({'message': 'Bad Request!'}))
    res = ipinfo.fetch_info(args.get('ip'))
    resp = {'result': res, 'requestHeaders': dict(request.headers)}
    return Response(status=200,
                    mimetype='application/json',
                    response=json.dumps(resp))


@app.route('/ipapi/fetch', methods=['GET'])
def fetch_ipapi_endpoint():
    args = request.args
    if 'ip' not in args:
        return Response(status=400,
                        mimetype='application/json',
                        response=json.dumps({'message': 'Bad Request!'}))
    res = ipapi.fetch_info(args.get('ip'))
    resp = {'result': res, 'requestHeaders': dict(request.headers)}
    return Response(status=200,
                    mimetype='application/json',
                    response=json.dumps(resp))


@app.route('/witch/fetch', methods=['GET'])
def fetch_witch_endpoint():
    resp = {'result': witch.fetch_info()}
    return Response(status=200,
                    mimetype='application/json',
                    response=json.dumps(resp))

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
