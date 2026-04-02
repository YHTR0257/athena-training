init:
	@echo "\033[1;34m========================================\033[0m"
	@echo "\033[1;36m🚀 Initializing project environment...\033[0m"
	@echo "\033[1;34m========================================\033[0m"
	@uv sync
	@uv run pre-commit install
	@echo "\033[1;32m✅ Initialization complete!\033[0m"
	@echo "\033[1;34m========================================\033[0m"

setup-claude-api-key:
	@echo "\033[1;34m========================================\033[0m"
	@echo "\033[1;36m🔑 Setting up Claude API key...\033[0m"
	@echo "\033[1;34m========================================\033[0m"
	@mkdir -p ~/.claude
	@read -s -p "Enter Claude API key: " API_KEY; echo; \
	if [ -f ~/.claude/settings.json ]; then \
		jq --arg key "$$API_KEY" '.env.ANTHROPIC_API_KEY = $$key' ~/.claude/settings.json > ~/.claude/settings.json.tmp; \
	else \
		echo '{}' > ~/.claude/settings.json.tmp; \
		jq --arg key "$$API_KEY" '.env.ANTHROPIC_API_KEY = $$key' ~/.claude/settings.json.tmp > ~/.claude/settings.json.tmp2; \
		mv ~/.claude/settings.json.tmp2 ~/.claude/settings.json.tmp; \
	fi; \
	mv ~/.claude/settings.json.tmp ~/.claude/settings.json
	@echo "\033[1;32m✅ Claude API key has been set successfully!\033[0m"
	@echo "\033[1;34m========================================\033[0m"

up:
	@echo "\033[1;34m========================================\033[0m"
	@echo "\033[1;36m🏗️  Building the project...\033[0m"
	@echo "\033[1;34m========================================\033[0m"
	@docker build -t athena-training:latest -f ./build/docker/Dockerfile .
	@echo "\033[1;32m✅ Build complete!\033[0m"
	@echo "\033[1;34m========================================\033[0m"

run:
	@echo "\033[1;34m========================================\033[0m"
	@echo "\033[1;36m🚀 Running the container...\033[0m"
	@echo "\033[1;34m========================================\033[0m"
	@docker run --rm -p 8000:8000 athena-training:latest
	@echo "\033[1;34m========================================\033[0m"
