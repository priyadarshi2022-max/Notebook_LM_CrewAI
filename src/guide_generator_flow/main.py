#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from guide_generator_flow.crews.research_crew import ResearchCrew 
from guide_generator_flow.crews.writing_crew import WritingCrew

from typing import Optional

# define a structured state for our flow
class ResearchFlowState(BaseModel):
  
  # user inputs (sources)
  youtube_links: Optional[str] = ""
  document_paths: Optional[str] = ""
  webpage_links: Optional[str] = ""
  research_paper_links: Optional[str] = ""

  # outputs from nodes
  research_report: str | None = None
  final_guide: str | None = None


# defining our flow
class GuideGeneratorFlow(Flow[ResearchFlowState]):
  
  """
  Main flow that orchestrates the complete guide generation process.
  Flow steps:
  1. recieve_user_inputs - Accept and validate user inputs
  2. run_research_crew - execute crew 1 (hierarchical research)
  3. run_writing_crew - Execute crew 2 (sequenital writing)
  """

  # define the start node
  @start
  def receive_user_inputs(self) -> str:
    print("=" * 70)
    print("GUIDE GENERATOR FLOW STARTED")
    print("=" * 70)

    # log which sources were provided
    sources_provided = []
    if self.state.youtube_links:
      sources_provided.append("YouTube")

    if self.state.webpage_links:
      sources_provided.append("Web Pages")

    if self.state.document_paths:
      sources_provided.append("Documents")

    if self.state.research_paper_links:
      sources_provided.append("Research Papers")

    if not sources_provided:
      print("\nWARNING: No sources provided!")
      print("Please provide at least one source type.")
      return "no_sources"
    
    print(f"\nSources provided: {', '.join(sources_provided)}")
    print("\n" + "=" * 70)

    return "inputs_received"
  
  # define the node to run crew 1
  @listen(receive_user_inputs)
  def run_research_crew(self, prev_output) -> str:
    """
    Executes Crew 1: Research Crew
    The research crew uses a manager agent to coordinate 4 specialists
    who gather information from different source types. The manager then
    compiles everything into a comprehensive research report.
    """

    if prev_output == "no_sources":
      print("\nSkipping Research Crew - No Sources Provided.")
      return "research_skiped"
    elif prev_output == "inputs_received":
      print("\n" + "=" * 70)
      print("CREW 1: RESEARCH CREW (Hierarchical)")
      print("=" * 70)
      print("\nInitializing research crew with manager + 4 specialists...")
      print("- YouTube Specialist")
      print("- Web Content Specialist")
      print("- Academic Paper Specialist")
      print("- Document Specialist")

      try:
        # initialize my research crew
        research_crew = ResearchCrew().crew()
        print("\nDelegating research tasks to specialists...\n")

        # execute the crew with provided links
        result = research_crew.kickoff(inputs={
          "youtube_links": self.state.youtube_links or "Not Provided",
          "webpage_links": self.state.webpage_links or "Not Provided",
          "research_paper_links": self.state.research_paper_links or "Not Provided",
          "document_paths": self.state.document_paths or "Not Provided"
        })

        # store the report into state
        self.state.research_report = result.raw

        print("\n" + "=" * 70)
        print("RESEARCH CREW COMPLETED")
        print("=" * 70)
        print(f"Research Report Generated:")
        return "research_complete"
      except Exception as e:
        print(f"ERROR in Research Crew: {str(e)}")
        return "research_failed"
      
  
  @listen(run_research_crew)
  def run_writing_crew(self, prev_output) -> str:
    """
    Execute Crew 2: Writing Crew (Sequential Process)
    The writing crew uses a sequential process where:
    1. Technical writer transforms research into beginner-friendly guide
    2. Content Editor reviews and polishes the guide
    """

    if prev_output == "research_skipped":
      print("\nSkipping writing crew - research was skipped")
      return "writing_skipped"
    
    if prev_output == "research_failed":
      print("\nSkipping writing crew - research was skipped")
      return "writing_skipped"
    
    print("\n" + "=" * 70)
    print("CREW 2: WRITING CREW (Sequential)")
    print("=" * 70)
    print("\nInitializing writing crew...")
    print("- Technical Writer (Step 1)")
    print("- Content Editor (Step 2)")

    try:
      # Initialize the writing crew
      writing_crew = WritingCrew().crew()
      print("\nTransforming research into beginner-friendly guide...\n")
      # execute writing crew with research report generated in previous node
      result = writing_crew.kickoff(inputs={
        "research_report": self.state.research_report
      })
      # store the generatd guide into state
      self.state.final_guide = result.raw

      print("\n" + "=" * 70)
      print("WRITING CREW COMPLETED")
      print("=" * 70)
      print(f"Getting Started Guide Generated:")
      print("\n" + "=" * 70)
      return "guide_complete"
    except Exception as e:
      print(f"ERROR in writing crew: {str(e)}")
      return "writing_failed"
    
def get_inputs():
  """
  Interactive terminal interface to collect user inputs.
  All inputs are optional
  """

  print("\n" + "=" * 70)
  print("GUIDE GENERATOR - INPUT COLLECTION")
  print("=" *  70)
  print("\nWELCOME! Let's create a getting-started guide for your framework/tool.")
  print("\nAll source inputs are OPTIONAL. You can skip any be pressing Enter.")
  print("=" * 70)

  # YouTube Links (Optional)
  print("\n" + "=" * 70)
  print("\nYOUTUBE VIDEOS/CHANNELS")
  print("   You can provide:")
  print("   - Individual video URLs (e.g., https://youtube.com/watch?v=abc123)")
  print("   - Channel URLs (e.g., https://youtube.com/@channelname)")
  print("   - Multiple links separated by commas")
  youtube_links = input("\n Enter YouTube links (or press Enter to skip): ").strip()

  if youtube_links:
    # Clean up the input
    youtube_links = ", ".join([link.strip() for link in youtube_links.split(",")])
    print(f"    Added {len(youtube_links.split(','))} YouTube source(s)")
  else:
    print(" Skipped")

  # Web Page Links (Optional)
  print("\n" + "=" * 70)
  print("\nWEB PAGES/ARTICLES")
  print("   You can provide:")
  print("   - Documentation URLs")
  print("   - Blog posts or tutorials")
  print("   - Multiple links separated by commas")
  webpage_links = input("\n Enter web page URLs (or press Enter to skip: )").strip()

  # Research Papers (Optional)
  print("\n" + "=" * 70)
  print("\n RESEARCH PAPERS (arXiv)")
  print("   You can provide:")
  print("   - arXiv URLs (e.g., https://arxiv.org/abs/2103.xxxxx)")
  print("   - Paper titles or arXiv IDs")
  print("   - Multiple entries separated by commas")
  research_paper_links = input("\n Enter research paper links/queries (or press Enter to skip: )").strip()

  # Documents (optional)
  print("\n" + "=" * 70)
  print("\nDOCUMENTS (PDF/TEXT/Markdown)")
  print("   You can provide:")
  print("   - Local file paths to PDFs")
  print("   - Text file paths (.txt)")
  print("   - Markdown file paths (.md, .mdx)")
  print("   - Multiple paths separated by commas")
  document_paths = input("\n Enter document paths(or press Enter to skip: )").strip()

  return {
    'youtube_links': youtube_links,
    'webpage_links': webpage_links,
    'research_paper_links': research_paper_links,
    'document_paths': document_paths
  }
    
def kickoff():
  """Execute the flow"""
  # get the inputs
  inputs = get_inputs()

  # define the flow
  flow = GuideGeneratorFlow()

  # run the flow with inputs
  flow_result = flow.kickoff(inputs=inputs)

  print("\n"+"="*70)
  print("FINAL RESULT")
  print("=" * 70)
  print(f"\n{flow_result}")


if __name__ == "__main__":
  kickoff()

   
  

      
      