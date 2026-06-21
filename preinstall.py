
template = "blueprint/custom_fedora_template.toml"
config_dir = "./config/"
output_file = "custom_fedora.toml"

with open(config_dir + "tmux.conf", encoding="utf-8") as f:
    tmux_config = f.read()
with open(config_dir + "vimrc", encoding="utf-8") as f:
    vim_config = f.read()
with open(template, encoding="utf-8") as f:
    blueprint = f.read()

blueprint = blueprint.replace("{{INSERT_TMUX_CONFIG}}", tmux_config)
blueprint = blueprint.replace("{{INSERT_VIM_CONFIG}}", vim_config)
with open(output_file, "w", encoding="utf-8") as f:
    f.write(blueprint)
