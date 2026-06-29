import customtkinter as ctk
from tkinter import filedialog
import os
import winsound

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class YuMusicMobile(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Phone screen proportions layout frame
        self.title("YuMusic Mobile")
        self.geometry("390x750")
        self.resizable(False, False)
        
        # Audio Engine Variables
        self.current_file = None
        self.is_playing = False
        
        # Premium Design Palette Assets
        self.bg_color = "#FFFFFF"
        self.card_color = "#F5F5F7"
        self.accent_color = "#FA243C"  # Signature Apple Red
        self.text_main = "#111111"
        self.text_sub = "#8E8E93"
        
        self.configure(fg_color=self.bg_color)
        self.setup_ui()

    def setup_ui(self):
        # 1. Top Action Header Row
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(fill="x", padx=25, pady=(25, 10))
        
        self.title_label = ctk.CTkLabel(self.header_frame, text="YuMusic", font=("Helvetica", 22, "bold"), text_color=self.text_main)
        self.title_label.pack(side="left")
        
        # Right Control Icons Block
        self.right_icons = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        self.right_icons.pack(side="right")
        
        self.load_btn = ctk.CTkButton(self.right_icons, text="📂", font=("Helvetica", 16), width=35, height=35,
                                       fg_color="transparent", text_color=self.text_sub, hover=False, command=self.load_music)
        self.load_btn.pack(side="left", padx=5)
        
        self.theme_btn = ctk.CTkButton(self.right_icons, text="🌙", font=("Helvetica", 16), width=35, height=35,
                                        fg_color="transparent", text_color=self.text_sub, hover=False, command=self.toggle_theme)
        self.theme_btn.pack(side="left")

        # 2. Main Album Art Container Card
        self.art_card = ctk.CTkFrame(self, width=280, height=280, corner_radius=32, fg_color=self.card_color)
        self.art_card.pack(pady=20)
        self.art_card.pack_propagate(False)
        
        self.art_icon = ctk.CTkLabel(self.art_card, text="🎵", font=("Helvetica", 80), text_color=self.accent_color)
        self.art_icon.place(relx=0.5, rely=0.5, anchor="center")

        # 3. Track Typography Metadata Display
        self.track_name = ctk.CTkLabel(self, text="No Track Selected", font=("Helvetica", 20, "bold"), text_color=self.text_main, wraplength=320)
        self.track_name.pack(pady=(15, 2))
        
        self.artist_name = ctk.CTkLabel(self, text="Local Device Library", font=("Helvetica", 15), text_color=self.text_sub)
        self.artist_name.pack()

        # 4. Playback Mechanical Controls Deck
        self.controls_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.controls_frame.pack(pady=30)
        
        self.prev_btn = ctk.CTkButton(self.controls_frame, text="⏮", font=("Helvetica", 24), width=50, fg_color="transparent", text_color=self.text_main, hover=False)
        self.prev_btn.grid(row=0, column=0, padx=20)
        
        # Central Main Play/Pause State Button
        self.play_btn = ctk.CTkButton(self.controls_frame, text="▶", font=("Helvetica", 22, "bold"), width=64, height=64, corner_radius=32,
                                      fg_color=self.accent_color, text_color="#FFFFFF", hover_color="#D01F33", command=self.toggle_playback)
        self.play_btn.grid(row=0, column=1, padx=20)
        
        self.next_btn = ctk.CTkButton(self.controls_frame, text="⏭", font=("Helvetica", 24), width=50, fg_color="transparent", text_color=self.text_main, hover=False)
        self.next_btn.grid(row=0, column=2, padx=20)

        # 5. Volume Bar Slider System
        self.vol_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.vol_frame.pack(fill="x", padx=40, pady=10)
        
        self.vol_low = ctk.CTkLabel(self.vol_frame, text="🔈", font=("Helvetica", 14), text_color=self.text_sub)
        self.vol_low.pack(side="left", padx=(0, 10))
        
        self.slider = ctk.CTkSlider(self.vol_frame, from_=0, to=100, number_of_steps=100, button_color=self.accent_color, button_hover_color="#D01F33", progress_color=self.accent_color)
        self.slider.set(70)
        self.slider.pack(side="left", fill="x", expand=True)
        
        self.vol_high = ctk.CTkLabel(self.vol_frame, text="🔊", font=("Helvetica", 14), text_color=self.text_sub)
        self.vol_high.pack(side="right", padx=(10, 0))

    def load_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("Wave Audio Files", "*.wav")])
        if file_path:
            self.current_file = file_path
            clean_name = os.path.basename(file_path).replace(".wav", "")
            self.track_name.configure(text=clean_name)
            self.artist_name.configure(text="Offline Audio Archive")
            self.stop_music()

    def toggle_playback(self):
        if not self.current_file:
            self.load_music()
            return
            
        if not self.is_playing:
            # SND_ASYNC streams audio dynamically in background loops
            winsound.PlaySound(self.current_file, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
            self.play_btn.configure(text="⏸")
            self.is_playing = True
        else:
            self.stop_music()

    def stop_music(self):
        winsound.PlaySound(None, winsound.SND_PURGE)
        self.play_btn.configure(text="▶")
        self.is_playing = False

    def toggle_theme(self):
        if ctk.get_appearance_mode() == "Light":
            ctk.set_appearance_mode("Dark")
            self.bg_color = "#1C1C1E"
            self.card_color = "#2C2C2E"
            self.text_main = "#FFFFFF"
            self.theme_btn.configure(text="☀️")
        else:
            ctk.set_appearance_mode("Light")
            self.bg_color = "#FFFFFF"
            self.card_color = "#F5F5F7"
            self.text_main = "#111111"
            self.theme_btn.configure(text="🌙")
            
        self.configure(fg_color=self.bg_color)
        self.title_label.configure(text_color=self.text_main)
        self.track_name.configure(text_color=self.text_main)
        self.prev_btn.configure(text_color=self.text_main)
        self.next_btn.configure(text_color=self.text_main)
        self.art_card.configure(fg_color=self.card_color)

if __name__ == "__main__":
    app = YuMusicMobile()
    app.mainloop()