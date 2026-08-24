"""Core AI Model - Main reasoning and response generation engine"""

import logging
from typing import Dict, List, Optional
from transformers import AutoTokenizer, pipeline
import torch

logger = logging.getLogger(__name__)


class AIModel:
    """Main AI model for generating responses"""

    def __init__(self, model_name: str = "gpt2"):
        """
        Initialize the AI model
        
        Args:
            model_name: HuggingFace model identifier
        """
        self.model_name = model_name
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        try:
            # Use text-generation pipeline instead of raw model loading
            self.generator = pipeline(
                "text-generation",
                model=model_name,
                device=0 if self.device.type == "cuda" else -1
            )
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            
            # Set pad token for GPT2 (doesn't have one by default)
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            
            logger.info(f"Loaded model {model_name} on {self.device}")
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            raise

    def generate_response(
        self,
        prompt: str,
        max_length: int = 150,
        temperature: float = 0.7,
        top_p: float = 0.9,
    ) -> str:
        """
        Generate a response based on the prompt
        
        Args:
            prompt: Input text to generate response for
            max_length: Maximum length of generated response
            temperature: Controls randomness (0-1)
            top_p: Nucleus sampling parameter
            
        Returns:
            Generated response text
        """
        try:
            # Clean the prompt to avoid repetition
            clean_prompt = prompt.strip()
            if len(clean_prompt) == 0:
                return "I'm ready to chat. What would you like to talk about?"
            
            outputs = self.generator(
                clean_prompt,
                max_length=max_length,
                temperature=temperature,
                top_p=top_p,
                do_sample=True,
                num_return_sequences=1,
            )
            
            response = outputs[0]["generated_text"]
            
            # Remove the prompt from the response
            if response.startswith(clean_prompt):
                response = response[len(clean_prompt):].strip()
            
            return response if response else "I'm thinking about that..."
            
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return "I apologize, but I encountered an error generating a response."

    def encode_text(self, text: str) -> List[int]:
        """Encode text to token IDs"""
        return self.tokenizer.encode(text)

    def decode_tokens(self, tokens: List[int]) -> str:
        """Decode token IDs back to text"""
        return self.tokenizer.decode(tokens, skip_special_tokens=True)
