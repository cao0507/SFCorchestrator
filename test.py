import api.tacker_api as tacker

tacker_vim = tacker.vim()
default_vim = tacker_vim.get_default_vim()
print default_vim
tacker_vim.register_vim("vim.json")
#tacker_vim.delete_vim("openstack-vim")
