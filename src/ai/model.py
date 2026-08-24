"""Core AI Model - Main reasoning and response generation engine"""

import logging
from typing import Dict, List, Optional
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

logger = logging.getLogger(__name__)


class AIModel:
    """Main AI model for generating responses"""

    def __init__(self, model_name: str = "distilbert-base-uncased"):
        """
        Initialize the AI model
        
        Args:
            model_name: HuggingFace model identifier
        """
        self.model_name = model_name
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)
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
            inputs = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)
            
            outputs = self.model.generate(
                inputs,
                max_length=max_length,
                temperature=temperature,
                top_p=top_p,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id,
            )
            
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return response
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return "I apologize, but I encountered an error generating a response."

    def encode_text(self, text: str) -> List[int]:
        """Encode text to token IDs"""
        return self.tokenizer.encode(text)

    def decode_tokens(self, tokens: List[int]) -> str:
        """Decode token IDs back to text"""
        return self.tokenizer.decode(tokens, skip_special_tokens=True)
