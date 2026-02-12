"""
Example usage of the TextSummarizer module
Demonstrates basic and advanced usage patterns
"""

import asyncio
from the_grand_house_of_avneesh.summary import create_summarizer
from the_grand_house_of_avneesh.summary.utils.exceptions import NLPProcessingError, SummarizationError


async def basic_example():
    """Basic summarization example"""
    print("="*80)
    print("BASIC EXAMPLE")
    print("="*80)
    
    # Sample text
    text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, 
    in contrast to the natural intelligence displayed by humans and animals. 
    Leading AI textbooks define the field as the study of "intelligent agents": 
    any device that perceives its environment and takes actions that maximize 
    its chance of successfully achieving its goals.
    
    The term "artificial intelligence" is often used to describe machines 
    that mimic "cognitive" functions that humans associate with the human mind, 
    such as "learning" and "problem solving". As machines become increasingly 
    capable, tasks considered to require "intelligence" are often removed from 
    the definition of AI, a phenomenon known as the AI effect.
    
    Modern machine learning techniques have proven highly effective at many tasks, 
    leading to a resurgence of interest in AI research after several "AI winters" 
    in the late 20th century. The field has experienced rapid growth in the 21st 
    century, with major advances in deep learning driving progress in computer 
    vision, natural language processing, and other areas.
    """
    
    # Initialize summarizer
    summarizer = await create_summarizer(
        text=text,
        aws_access_key="",
        aws_secret_key=""
    )
    print(summarizer)
    

async def advanced_example():
    """Advanced usage with custom configuration"""
    print("\n\n" + "="*80)
    print("ADVANCED EXAMPLE - Custom Configuration")
    print("="*80)
    
    # Long text example
    text = """
    Climate change refers to long-term shifts in temperatures and weather patterns. 
    These shifts may be natural, such as through variations in the solar cycle. 
    But since the 1800s, human activities have been the main driver of climate change, 
    primarily due to burning fossil fuels like coal, oil and gas.
    
    Burning fossil fuels generates greenhouse gas emissions that act like a blanket 
    wrapped around the Earth, trapping the sun's heat and raising temperatures. 
    Examples of greenhouse gas emissions that are causing climate change include 
    carbon dioxide and methane. These come from using gasoline for driving a car 
    or coal for heating a building, for example.
    
    The consequences of climate change now include, among others, intense droughts, 
    water scarcity, severe fires, rising sea levels, flooding, melting polar ice, 
    catastrophic storms and declining biodiversity. People are experiencing climate 
    change in diverse ways. It affects our health, ability to grow food, housing, 
    safety and work.
    
    To avoid catastrophic future impacts, it is essential that the world urgently 
    cuts its greenhouse gas emissions. Countries are working together to address 
    climate change through international agreements like the Paris Agreement, which 
    aims to limit global warming to well below 2 degrees Celsius.
    """
    
    summarizer = await create_summarizer(
        text=text,
        aws_access_key="",
        aws_secret_key=""
    )
    print(summarizer)
    


async def main():
    """Run all examples"""
    await basic_example()
    await advanced_example()



if __name__ == "__main__":
    asyncio.run(main())
