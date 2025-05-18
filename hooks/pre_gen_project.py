package_name = "{{ cookiecutter.package_name }}"
assert len(package_name) > 1
assert package_name[0].islower()
assert package_name[-1].islower()
for i in package_name[1:-1]:
    assert i.islower() or i.isdigit() or (i == "_")
