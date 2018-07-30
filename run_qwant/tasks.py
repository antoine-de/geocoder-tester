from invoke import task
import os


def _get_remaining_tests(ctx):
    selectors = [c['selector'] for c in ctx.categories if 'selector' in c]

    return ' and '.join([f'not {s}' for s in selectors])
        

def _init_output_dir(ctx, test_name):
    if 'output_dir' not in ctx:
        dir_name = f'{test_name}' # TODO add time
        # os.mkdir(dir_name)
        ctx.output_dir = dir_name
    return ctx.output_dir

@task
def run_pytest(ctx, url, name, country, category):
    _init_output_dir(ctx, name)
    directory = f'../geocoder_tester/world/{country}'
    category_name = category['name']

    print(f'cat = {category}')
    if category.get('remaining_tests'):
        selector = _get_remaining_tests(ctx)
    else:
        selector = category['selector']
    print(f'selector for {category} is {selector}')

    additional_args = ' '.join(ctx.additional_pytest_args)
    py_test = f'pytest {directory} --api-url {url} -k {selector} --loose-compare --save-report=$OUTPUT_DIR/$TEST_NAME.txt --tb=short {additional_args}'

    print(f'runnning {py_test}')
    with open(os.path.join(ctx.output_dir, f'{country}_{category_name}.log'), 'w') as log_file:
        ctx.run(py_test, out_stream=log_file)

@task(default=True)
def run_all(ctx, url, name):
    _init_output_dir(ctx, name)
    for country in ctx.countries:
        for category in ctx.categories:
            run_pytest(ctx, url, name, country, category)
