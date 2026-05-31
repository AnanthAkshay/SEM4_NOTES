import os
import win32com.client

def convert_pptx_to_pdf():
    mc_dir = r"a:\SEM4_Complete\MICROCONTROLLER"
    
    # Initialize PowerPoint
    try:
        powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    except Exception as e:
        print(f"Error starting PowerPoint: {e}")
        return
        
    for filename in os.listdir(mc_dir):
        if filename.endswith(".pptx"):
            ppt_path = os.path.join(mc_dir, filename)
            pdf_name = filename.replace(".pptx", ".pdf")
            pdf_path = os.path.join(mc_dir, pdf_name)
            
            if os.path.exists(pdf_path):
                print(f"PDF already exists for {filename}, skipping.")
                continue
                
            print(f"Converting {filename} to PDF...")
            try:
                # Open presentation without opening a window (WithWindow=False/0)
                deck = powerpoint.Presentations.Open(ppt_path, WithWindow=0)
                # Save as PDF (Format type 32 is PDF)
                deck.SaveAs(pdf_path, 32)
                deck.Close()
                print(f"Successfully converted {filename} to {pdf_name}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")
                
    powerpoint.Quit()
    print("All conversions completed!")

if __name__ == "__main__":
    convert_pptx_to_pdf()
