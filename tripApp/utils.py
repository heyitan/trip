from django.shortcuts import render as base_render, render_to_response

def render(req, template_name, template_param):
    print isinstance(template_param, dict)
    if not isinstance(template_param, dict):
        raise Exception, "the third argument must be a instance of dict"
    if 'body_template' in template_name:
        raise Exception, "body_template must not be a key of the third argument"
    template_param.update({'body_template': template_name})
    response = base_render(
            req,
            'trip/index.html',
            template_param
    )
    return response
