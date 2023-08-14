#### Принцип написания API
1. api может приниматьт GET POST папрамеры, 
overwrite = request.args.get('overwrite', '0')
background = request.args.get('background', '1')

#### Простейший api
@mod.route('/footages/<int:footage_id>/passways/calc', methods=('POST', ))
def recalc_passways(footage_id):
    result = {'HELLO': 'world'}
    return api_response(result)
