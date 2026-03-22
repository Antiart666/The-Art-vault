import os

def generera_mappbild():
    # Sätt mappen till där skriptet ligger
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)
    
    output = []
    output.append(f"MAPPANALYS FÖR: {base_dir}\n")
    output.append("="*50 + "\n")

    # Lista alla filer i huvudmappen
    output.append("FILER I HUVUDMAPPEN:")
    for f in os.listdir(base_dir):
        if os.path.isfile(f):
            size = os.path.getsize(f)
            output.append(f"  [FIL] {f} ({size} bytes)")
    
    output.append("\nMAPPAR OCH UNDERMAPPAR:")
    # Gå igenom de relevanta målmapparna
    targets = ["Antiart_tavlor", "Suss_Miniatyrer", "Utställning_Wadköping"]
    for target in targets:
        if os.path.exists(target):
            output.append(f"\n[MAPP] {target}")
            for root, dirs, files in os.walk(target):
                level = root.replace(target, '').count(os.sep)
                indent = '  ' * (level + 1)
                subfolder = os.path.basename(root)
                if subfolder != target:
                    output.append(f"{indent}[SUB] {subfolder}")
                
                sub_indent = '  ' * (level + 2)
                for f in files:
                    if f.lower().endswith(('.jpg', '.png', '.jpeg')):
                        output.append(f"{sub_indent}{f}")
        else:
            output.append(f"\n[!] SAKNAS: {target}")

    # Skriv till fil
    with open("mappstruktur.txt", "w", encoding="utf-8") as f:
        f.writelines("\n".join(output))
    
    print("✅ Analysen är klar! Kopiera innehållet i filen 'mappstruktur.txt' och skicka till mig.")

if __name__ == "__main__":
    generera_mappbild()