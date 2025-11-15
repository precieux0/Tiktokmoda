import requests
import re
import json
import time
import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich import print as printf

class TikTokBot:
    def __init__(self):
        self.sukses = []
        self.gagal = []
        self.followers_count = 0
        self.console = Console()
        
    def logo(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        printf(Panel(r"""[bold cyan] _______ _ _  _   _        
|__   __(_) | | | | |       
   | |   _| |_| | | | _____ 
   | |  | | __| | | |/ / _ \
   | |  | | |_| | |   | |_| |
   |_|  |_|\__|_|_|_|\_\___/

[bold magenta]  TikTok Followers Bot
   [underline green]Simple & Efficient""", width=70, style="bold bright_black"))
    
    def get_tiktok_info(self, username):
        """Récupère les infos du compte TikTok"""
        try:
            session = requests.Session()
            session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            
            # Simulation - en réalité vous auriez besoin d'une API
            printf(f"[bold bright_black]   ──>[bold white] Vérification du compte: [bold cyan]@{username}")
            time.sleep(2)
            return True
            
        except Exception as e:
            printf(f"[bold bright_black]   ──>[bold red] Erreur: {str(e)}")
            return False
    
    def send_followers(self, service, username, password, target):
        """Envoie des followers via un service"""
        try:
            printf(f"[bold bright_black]   ──>[bold white] Tentative sur: [bold yellow]{service}")
            
            # Simulation de connexion
            session = requests.Session()
            session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            
            # Simulation de délai
            time.sleep(3)
            
            # Simulation de réponse réussie
            if username and password:
                self.sukses.append(service)
                printf(f"[bold bright_black]   ──>[bold green] Succès sur {service}!")
                return True
            else:
                self.gagal.append(service)
                printf(f"[bold bright_black]   ──>[bold red] Échec sur {service}")
                return False
                
        except Exception as e:
            printf(f"[bold bright_black]   ──>[bold red] Erreur: {str(e)}")
            self.gagal.append(service)
            return False
    
    def delay_counter(self, seconds, target):
        """Compte à rebours"""
        while seconds:
            mins, secs = divmod(seconds, 60)
            printf(f"[bold bright_black]   ──>[bold cyan] @{target}[bold white] - Prochain essai dans: [bold yellow]{mins:02d}:{secs:02d}", end='\r')
            time.sleep(1)
            seconds -= 1
        printf(" " * 70, end='\r')
    
    def run(self):
        """Lance le bot"""
        try:
            self.logo()
            
            # Demander les identifiants
            printf(Panel("[bold white]Entrez vos identifiants de service (format: username:password)", 
                        width=70, style="bold bright_black", title="[bold bright_black][Connexion]"))
            account_input = self.console.input("[bold bright_black]   ╰─> ")
            
            if ':' not in account_input:
                printf(Panel("[bold red]Format incorrect! Utilisez: username:password", 
                           width=70, style="bold bright_black"))
                return
            
            username, password = account_input.split(':', 1)
            
            # Demander la cible TikTok
            printf(Panel("[bold white]Entrez le nom d'utilisateur TikTok cible (sans @)", 
                        width=70, style="bold bright_black", title="[bold bright_black][Cible]"))
            target = self.console.input("[bold bright_black]   ╰─> ").replace('@', '')
            
            if not target:
                printf(Panel("[bold red]Nom d'utilisateur invalide!", 
                           width=70, style="bold bright_black"))
                return
            
            # Vérifier le compte
            if not self.get_tiktok_info(target):
                printf(Panel("[bold red]Compte TikTok non trouvé ou inaccessible!", 
                           width=70, style="bold bright_black"))
                return
            
            printf(Panel("[bold green]Compte TikTok trouvé! Démarrage de l'envoi...", 
                       width=70, style="bold bright_black"))
            
            # Services disponibles
            services = [
                "tiktok-service1.com",
                "tiktok-service2.net", 
                "tiktok-service3.org",
                "tiktok-service4.io"
            ]
            
            # Boucle principale
            while True:
                try:
                    for service in services:
                        self.send_followers(service, username, password, target)
                        
                        # Statistiques
                        printf(Panel(f"""
[bold white]Statistiques:
[bold green]Succès: {len(self.sukses)}
[bold red]Échecs: {len(self.gagal)}
[bold yellow]Prochain service dans: 10 minutes
                        """, width=70, style="bold bright_black"))
                        
                        # Attendre 10 minutes entre les services
                        self.delay_counter(600, target)
                        
                except KeyboardInterrupt:
                    printf("\n[bold yellow]Interruption par l'utilisateur. Arrêt...")
                    break
                except Exception as e:
                    printf(f"[bold red]Erreur: {str(e)}")
                    time.sleep(5)
                    continue
                    
        except Exception as e:
            printf(Panel(f"[bold red]Erreur critique: {str(e)}", 
                       width=70, style="bold bright_black"))

def main():
    """Fonction principale"""
    try:
        # Vérifier les dépendances
        try:
            import requests
            from rich.console import Console
            from rich.panel import Panel
        except ImportError as e:
            printf(f"[bold red]Module manquant: {str(e)}")
            printf("[bold yellow]Installez les dépendances avec: pip install -r requirements.txt")
            return
        
        # Lancer le bot
        bot = TikTokBot()
        bot.run()
        
    except KeyboardInterrupt:
        printf("\n[bold yellow]Au revoir!")
    except Exception as e:
        printf(f"[bold red]Erreur: {str(e)}")

if __name__ == "__main__":
    main()
