"""Main entry point for Personal AI Assistant"""

import logging
from src.utils.logger import setup_logger
from src.utils.config import Config
from src.ai.model import AIModel
from src.memory.conversation import ConversationMemory

# Setup logging
logger = setup_logger(__name__)


def main():
    """Main application entry point"""
    
    logger.info("Starting Personal AI Assistant")
    logger.info(f"Configuration: {Config.to_dict()}")
    
    # Initialize components
    try:
        ai_model = AIModel(model_name=Config.MODEL_NAME)
        memory = ConversationMemory(max_messages=Config.CONVERSATION_MEMORY_SIZE)
        
        logger.info("AI model and memory initialized successfully")
        
        # Interactive chat loop
        print("\n" + "="*60)
        print("Personal AI Assistant")
        print("Type 'exit' to quit, 'clear' to reset conversation")
        print("="*60 + "\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            
            if user_input.lower() == "clear":
                memory.clear()
                print("[Conversation cleared]\n")
                continue
            
            if not user_input:
                continue
            
            # Add user message to memory
            memory.add_message("user", user_input)
            
            # Generate response
            context = memory.get_context(num_messages=5)
            prompt = f"{context}assistant:"
            
            response = ai_model.generate_response(
                prompt,
                max_length=Config.MAX_TOKENS,
                temperature=Config.TEMPERATURE
            )
            
            # Extract just the new response (remove prompt)
            response_text = response.replace(prompt, "").strip()
            
            # Add assistant response to memory
            memory.add_message("assistant", response_text)
            
            print(f"\nAssistant: {response_text}\n")
            
    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
        print("\n\nShutting down gracefully...")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    main()
