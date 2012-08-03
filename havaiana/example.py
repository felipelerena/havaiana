from __init__ import run
from ojota import current_data_code

import msa.core.data as pkg

def candidato_list(field, item):
    required = field in item.required_fields
    lista_cand = getattr(item, field)
    value = ""
    for element in lista_cand:
        value += '<a href="/Candidatos/%s">%s</a> 1' % (element, element)

    related = False

    return (field, value, required, related)

if __name__ == '__main__':
    current_data_code("EJ01")
    renderers = [('Lista', 'cod_candidatos', candidato_list)]
    run(pkg, renderers)