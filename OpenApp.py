import sys
import os
from datetime import datetime, timedelta
import psutil
import subprocess
import time
import pyautogui
import pygetwindow as gw
from pathlib import Path

# =========================
# KONFIGURACJA
# =========================

BASE_DIR = Path(__file__).resolve().parent
BLUESTACKS_PATH = r"C:\Program Files\BlueStacks_nxt\HD-Player.exe"
MAIN_LOADING_SCREEN_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\MAIN_LOADING_SCREEN.png"
CLOSE_AD_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\CLOSE_ADD_X_BUTTON.png"
ADVERTISEMENT_LABEL_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\ADVERTISEMENT_CHECK.png"
GDA_HUB_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_HUB_BUTTON.png"
GDA_OPS_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_OPS_BUTTON.png"
GDA_CLAIM_ALL_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\CLAIM_ALL_BUTTON.png"
GDA_RESTART_ALL_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\RESTART_ALL_BUTTON.png"
GDA_BACK_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\BACK_BUTTON.png"
SINGLE_CLAIM_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\SINGLE_CLAIM_BUTTON.png"
PLAY_AGAIN_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\PLAY_AGAIN_BUTTON.png"
BATTLE_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\BATTLE_BUTTON.png"
SHOP_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\SHOP_BUTTON.png"
START_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\START_BUTTON.png"
RESTART_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\RESTART_BUTTON.png"
SERVER_ISSUE_RESTART_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\SERVER_ISSUE_RESTART.png"
CAMPAIGN_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\CAMPAIGN_BUTTON.png"
FULL_USER_REWARD_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\FULL_USER_REWARDS.png"
FULL_USER_REWARD_CLAIM_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\FULL_USER_REWARDS_CLAIM_BUTTON.png"
FINISHED_GDA_OP_GOLD_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\FINISHED_GFA_OP_GOLD_ICON.png"
FINISHED_GDA_OP_RR_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\FINISHED_GDA_OP_RR_ICON.png"
FINISHED_GDA_OP_EWA_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\FINISHED_GDA_OP_EWA_ICON.png"
FINISHED_GDA_OP_WD_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\FINISHED_GDA_OP_WD_ICON.png"
FINISHED_GDA_OP_GOTG_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\FINISHED_GFA_OP_GOTG_ICON.png"
FINISHED_GDA_OP_TIH_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\FINISHED_GFA_OP_TIH_ICON.png"
FINISHED_GDA_OP_SCHOOLSOUT_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\FINISHED_GFA_OP_SCHOOLSOUT_ICON.png"

SOCIAL_HUB_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\SOCIAL_HUB_BUTTON.png"

BOSS_RAID_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\BOSS_RAID\BOSS_RAID_BUTTON.png"
BOSS_RAID_OTHER_USERS_REWARDS_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\BOSS_RAID\BOSS_RAID_OTHER_USERS_REWARDS_BUTTON.png"
BOSS_RAID_BATTLE_FIRST_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\BOSS_RAID\BOSS_RAID_BATTTLE_FIRST_BUTTON.png"
BOSS_RAID_BATTLE_AUTOFILL_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\BOSS_RAID\BOSS_RAID_BATTLE_AUTOFILL_BUTTON.png"
BOSS_RAID_START_BATTLE_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\BOSS_RAID\BOSS_RAID_START_BATTLE_BUTTON.png"
BOSS_RAID_CLAIM_OWN_BATTLE_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\BOSS_RAID\BOSS_RAID_CLAIM_OWN_BATTLE_BUTTON.png"
BOSS_RAID_BACK_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\BOSS_RAID\BOSS_RAID_BACK_BUTTON.png"

ALLIANCES_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\ALLIANCE\ALLIANCES_BUTTON.png"
ALLIANCES_BACK_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\ALLIANCE\ALLIANCES_BACK_BUTTON.png"
ALLIANCES_FIRST_BATTLE_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\ALLIANCE\ALLIANCE_FIRST_BATTLE_BUTTON.png"
ALLIANCES_LAST_BATTLE_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\ALLIANCE\ALLIANCE_LAST_BATTLE_BUTTON.png"
ALLIANCES_CLAIM_BATTLE_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\ALLIANCE\ALLIANCE_CLAIM_BATTLE_BUTTON.png"
ALLIANCES_WAVES_REWARDS_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\ALLIANCE\ALLIANCES_WAVES_REWARDS.png"
ALLIANCES_WAVES_REWARDS_CLAIM_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\ALLIANCE\ALLIANCES_WAVES_REWARDS_CLAIM.png"

FRIENDS_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\FRIENDS\FRIENDS_BUTTON.png"
FRIENDS_CLAIM_ALL_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\FRIENDS\FRIENDS_CLAIM_ALL_BUTTON.png"
FRIENDS_CLAIM_ALL_2_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\FRIENDS\FRIENDS_CLAIM_ALL_2_BUTTON.png"
FRIENDS_CLAIM_SINGLE_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\FRIENDS\FRIENDS_CLAIM_SINGLE_BUTTON.png"
FRIENDS_TAP_TO_CONTINUE_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\FRIENDS\FRIENDS_TAP_TO_CONTINUE_BUTTON.png"
FRIENDS_5_NEW_DAYS_REWARD_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\FRIENDS\FRIENDS_5_NEW_DAYS_REWARD_BUTTON.png"
FRIENDS_5_NEW_DAYS_REWARD_CLOSE_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\FRIENDS\FRIENDS_5_NEW_DAYS_REWARD_CLOSE_BUTTON.png"

EMPTY_SLOT_GDA_OP_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\EMPTY_SLOT_FOR_GDA_OP_ICON.png"
TUTH_SCROLL_COORD_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_OP_BANNER_TUTH_FOR_SCROLL.png"
THOTG_SCROLL_COORD_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_OP_BANNER_THOTG_FOR_SCROLL.png"
DD_SCROLL_COORD_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_OP_BANNER_DD_FOR_SCROLL.png"
GDA_OP_RR_BANNER_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_OP_BANNER_RR_WITH_START.png"
GDA_OP_TIH_BANNER_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_OP_BANNER_TIH_WITH_START.png"
GDA_OP_EWA_BANNER_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_OP_BANNER_EWA_WITH_START.png.png"
GDA_OP_WD_BANNER_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_OP_BANNER_WD_WITH_START.png.png"

GDA_EVENTS_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_EVENTS_BUTTON.png"
GDA_EVENT_GDA_BANNER_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_EVENT_GDA_BANNER.png"
GDA_EVENT_FWB_BANNER_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_EVENT_FWB_BANNER.png"
GDA_EVENT_RANK_UP_TAB_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_EVENT_RAUNK_UP_TAB.png"
GDA_EVENT_RANK_UP_BUTTON_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_EVENT_RAUNK_UP_BUTTON.png"
GDA_EVENT_PREBATTLE_UP_TAB_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_EVENT_PREBATTLE_TAB.png"
GDA_EVENT_ACTIVE_BATTLE_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_EVENT_ACTIVE_BATTLE_BUTTON.png"
GDA_EVENT_AUTOFILL_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_EVENT_AUTOFILL_BUTTON.png"
GDA_EVENT_INACTIVE_BATTLE_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GDA_EVENT_INACTIVE_BATTLE_BUTTON.png"

LLOD_EVENT_BANNER_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\LLOD_EVENT\LLOD_EVENT_BANNER.png"
LLOD_EVENT_BUY_ALL_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\LLOD_EVENT\LLOD_EVENT_FREE_BUTTON.png"
LLOD_EVENT_REFRESH_NOW_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\LLOD_EVENT\LLOD_EVENT_REFRESH_NOW_BUTTON.png"
LLOD_EVENT_TAP_TO_CONTINOU_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\LLOD_EVENT\LLOD_EVENT_TAP_TO_CONTINUE_BUTTON.png"
LLOD_EVENT_CLOSE_SHOP_LVL_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\LLOD_EVENT\LLOD_EVENT_CLOSE_SHOP_LVL.png"
LLOD_EVENT_FREE_FEFRESH_CHECK_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\LLOD_EVENT\LLOD_EVENT_FREE_RESFRESH_CHECK.png"

SHOPS_EQUIPMENT_BANNER_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\SHOPS\SHOPS_EQUIPMENT_BANNER.png"
SHOPS_EQUIPMENT_ON_LIST_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\SHOPS\SHOPS_EQUIPMENT_ON_LIST.png"
SHOP_EQUIPMENT_BUY_VIA_GOLD_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\SHOPS\SHOP_EQUIPMENT_BUY_VIA_GOLD_BUTTON.png"
SHOPS_EQUIPMENT_TAP_TO_CONTINUE_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\SHOPS\SHOPS_EQUIPMENT_TAP_TO_CONTINUE.png"

STORE_WITH_FREE_STAFF_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GEMS_REWARDS\STORE_WITH_FREE_STAFF.png"
STORE_TIME_LIMITED_TAB__DAILY_WITH_FREE_STAFF_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GEMS_REWARDS\STORE_TIME_LIMITED_TAB__DAILY_WITH_FREE_STAFF.png"
STORE_TIME_LIMITED_TAB_WITH_FREE_STAFF_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GEMS_REWARDS\STORE_TIME_LIMITED_TAB_WITH_FREE_STAFF.png"
STORE_TIME_LIMITED_TAB_DAILY_FREE_GEMS_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GEMS_REWARDS\STORE_TIME_LIMITED_TAB__DAILY_FREE_GEMS.png"
STORE_TIME_LIMITED_TAB__DAILY_TAB_TO_CONTINUE_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GEMS_REWARDS\STORE_TIME_LIMITED_TAB__DAILY_TAB_TO_CONTINUE.png"
STORE_FREE_INFO_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GEMS_REWARDS\STORE_FREE_INFO.png"
STORE_BACK_IMAGE = r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\IMAGES\GEMS_REWARDS\STORE_BACK.png"

LOG_FILE = Path(__file__).resolve().parent / "bot_log.txt"
class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        self.log.flush()

    def flush(self):
        self.terminal.flush()
        self.log.flush()

sys.stdout = Logger(LOG_FILE)

# =========================
# URUCHOMIENIE BLUESTACKS
# =========================
def start_game():
    """
    Sprawdza, czy konkretna instancja BlueStacks z grą jest już uruchomiona.
    Jeśli tak - niczego nie uruchamia.
    Jeśli nie - uruchamia grę.
    """

    # print(f"Unable to find BlueStacks window.")
    # log(f"Unable to find BlueStacks window.")

    for process in psutil.process_iter(["name", "cmdline"]):
        try:
            name = process.info["name"]
            cmdline = process.info["cmdline"]

            if name and name.lower() == "hd-player.exe" and cmdline:

                command = " ".join(cmdline)

                if (
                    "--instance Pie64" in command
                    and "com.ubisoft.invincible.guardians.globe.idle.superhero.rpg.battle.afk"
                    in command
                ):
                    log(f"Game is already working.")
                    return

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    log(f"Starting game via BlueStacks...")

    subprocess.Popen([
        r"C:\Program Files\BlueStacks_nxt\HD-Player.exe",
        "--instance",
        "Pie64",
        "--cmd",
        "launchApp",
        "--package",
        "com.ubisoft.invincible.guardians.globe.idle.superhero.rpg.battle.afk",
        "--source",
        "desktop_shortcut"
    ])

    log(f"Waiting 120 seconds for game to be launched...")
    time.sleep(120)

# =========================
# ZNAJDŹ ROZMIAR OKNA
# =========================
def get_bluestacks_geometry():
    windows = gw.getWindowsWithTitle("BlueStacks App Player")

    if not windows:
        log(f"Nie znaleziono okna BlueStacks.")
        return None

    window = windows[0]

    return {
        "left": window.left,
        "top": window.top,
        "width": window.width,
        "height": window.height
    }

# =========================
# ZMIEŃ ROZDZIELCZOŚC OKNA
# =========================
def set_bluestacks_window(x=0, y=0, width=879, height=1032):
    """
    Ustawia pozycję i rozmiar okna BlueStacks.

    x, y      - pozycja lewego górnego rogu okna
    width     - szerokość okna
    height    - wysokość okna
    """

    windows = gw.getWindowsWithTitle("BlueStacks App Player")

    if not windows:
        log(f"Nie znaleziono okna BlueStacks.")
        return False

    window = windows[0]

    # Ustawienie pozycji
    window.moveTo(x, y)

    # Ustawienie rozmiaru
    # window.resizeTo(width, height)

    # print(
    #     f"BlueStacks ustawiony: "
    #     f"pozycja=({x}, {y}), "
    #     f"rozmiar={width}x{height}"
    # )

    return True

# =========================
# ZAMYKANIE BLUESTACKS
# =========================
def close_game(waiting_time=20):
    """
    Zamyka instancję BlueStacks Pie64.
    """

    log(f"Checking if game is running...")

    for process in psutil.process_iter(["name", "cmdline"]):
        try:
            name = process.info["name"]
            cmdline = process.info["cmdline"]

            if name and name.lower() == "hd-player.exe" and cmdline:

                command = " ".join(cmdline)

                if (
                    "--instance Pie64" in command
                    and "com.ubisoft.invincible.guardians.globe.idle.superhero.rpg.battle.afk"
                    in command
                ):
                    log(f"Game found. PID: {process.pid}")
                    log(f"Closing game...")

                    process.terminate()

                    try:
                        process.wait(timeout=5)
                        log(f"Game closed successfully.")

                    except psutil.TimeoutExpired:
                        log(f"Game did not close normally. Killing process...")
                        process.kill()

                    return True

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    log(f"Game is not running.")
    time.sleep(waiting_time)
    return False

# =========================
# SPRAWDZANIE CZY DANY OBRAZ ISTNIEJE
# =========================
def find_screenshot(image_path, timeout=10, confidence=0.8, waiting_time=1):
    """
    Szuka podanego przycisku na ekranie.

    image_path  - ścieżka do obrazka przycisku
    timeout     - maksymalny czas oczekiwania w sekundach
    confidence  - próg podobieństwa obrazu (0.0 - 1.0)

    Zwraca:
        True  - znaleziono i zwrócono 1
        False - nie znaleziono przycisku w określonym czasie i zwrócono 0
    """

    # log(f"Searching for image: {image_path}")

    start_time = time.time()

    while time.time() - start_time < timeout:

        try:
            location = pyautogui.locateCenterOnScreen(
                image_path,
                confidence=confidence
            )

            if location is not None:
                time.sleep(waiting_time)
                return 1
        except pyautogui.ImageNotFoundException:
            # Obraz nie został znaleziony.
            # Czekamy i próbujemy ponownie.
            pass

        

    log(f"Unable to find: {image_path}")
    time.sleep(waiting_time)
    return 0

# =========================
# KLIKANIE PRZYCISKU ZE SCREENA
# =========================
def click_button(image_path, timeout=10, confidence=0.8, waiting_time=0.5):
    """
    Szuka podanego przycisku na ekranie i klika jego środek.

    image_path  - ścieżka do obrazka przycisku
    timeout     - maksymalny czas oczekiwania w sekundach
    confidence  - próg podobieństwa obrazu (0.0 - 1.0)

    Zwraca:
        True  - znaleziono i kliknięto przycisk
        False - nie znaleziono przycisku w określonym czasie
    """

    # log(f"Searching for image: {image_path}")

    start_time = time.time()

    while time.time() - start_time < timeout:

        try:
            location = pyautogui.locateCenterOnScreen(
                image_path,
                confidence=confidence
            )

            if location is not None:
                x, y = location

                # print(f"Found image {image_path}: ({x}, {y})")
                log(f"Clicking {image_path}... ")

                pyautogui.click(x, y)
                time.sleep(waiting_time)
                return True

        except pyautogui.ImageNotFoundException:
            # Obraz nie został znaleziony.
            # Czekamy i próbujemy ponownie.
            pass

        

    log(f"Unable to find image: {image_path}")

    return False

# =========================
# KLIKANIE I ROBIENIE BACKUPU - SCREENA
# =========================
def click_button_with_screenshot(image_path, timeout=10, confidence=0.8, waiting_time=0.5):
    """
    Szuka podanego przycisku na ekranie.

    Po znalezieniu:
    1. wykonuje screenshot,
    2. zapisuje go w folderze SCREENSHOTS,
    3. klika środek przycisku.

    Zwraca:
        True  - znaleziono i kliknięto przycisk
        False - nie znaleziono przycisku w określonym czasie
    """

    log(f"Searching for image: {image_path}")

    start_time = time.time()

    while time.time() - start_time < timeout:

        try:
            location = pyautogui.locateCenterOnScreen(
                image_path,
                confidence=confidence
            )

            if location is not None:

                x, y = location

                # ========================= # ZNALEZIENIE OKNA BLUESTACKS # ========================= 
                windows = gw.getWindowsWithTitle("BlueStacks App Player") 
                
                if not windows: 
                    log(f"Unable to find BlueStacks window.") 
                    return False 
                
                window = windows[0] 
                # Pozycja i rozmiar okna 
                left = window.left 
                top = window.top 
                width = window.width 
                height = window.height 
                # ========================= # SCREENSHOT TYLKO BLUESTACKS # =========================

                os.makedirs("GDA_OPS_RESULTS", exist_ok=True)

                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                screenshot_path = os.path.join(
                    r"C:\Users\mateu\OneDrive\Pulpit\Resources\Python\InvincibleGTG_bot\GDA_OPS_RESULTS",
                    f"screenshot_{timestamp}.png"
                )
                pyautogui.screenshot( screenshot_path, region=( left, top, width, height ) )
                log(f"Screenshot saved: {screenshot_path}")
                
                time.sleep(2)
                
                log(f"Clicking {image_path}... ")
                pyautogui.click(x, y)
                

                time.sleep(waiting_time)

                return True

        except pyautogui.ImageNotFoundException:
            pass

        

    log(f"Unable to found: {image_path}")

    return False

# =========================
# KLIKANIE
# =========================
def click(x, y, delay=1):
    # log(f"Clicking: X={x}, Y={y}")
    pyautogui.click(x, y)
    time.sleep(delay)

# =========================
# SZUKANIE WSPÓŁRZĘDNYCH ZDJĘCIA
# =========================
def find_coordinates(image_path, timeout=10, confidence=0.8, waiting_time=0.5):
    """
    Szuka podanego przycisku na ekranie.

    Po znalezieniu:
    1. pobiera współrzędne punktu.

    Zwraca:
        (x, y)  - współrzędne punktu
        False - nie znaleziono przycisku w określonym czasie
    """

    log(f"Searching for image: {image_path}")

    start_time = time.time()

    while time.time() - start_time < timeout:

        try:
            location = pyautogui.locateCenterOnScreen(
                image_path,
                confidence=confidence
            )

            if location is not None:

                x, y = location

                # ========================= # ZNALEZIENIE OKNA BLUESTACKS # ========================= 
                windows = gw.getWindowsWithTitle("BlueStacks App Player") 
                
                if not windows: 
                    log(f"Unable to find BlueStacks window.") 
                    return False 
                
                window = windows[0] 
                # Pozycja i rozmiar okna 
                left = window.left 
                top = window.top 
                width = window.width 
                height = window.height 
                # ========================= # SCREENSHOT TYLKO BLUESTACKS # =========================

                os.makedirs("GDA_OPS_RESULTS", exist_ok=True)

                timestamp = datetime.now().strftime(
                    "%Y-%m-%d_%H-%M-%S"
                )

                return (x, y)

        except pyautogui.ImageNotFoundException:
            pass

        

    log(f"Unable to found: {image_path}")

    return False

# =========================
# SWIPOWANIE
# =========================
def swipe(start_x, start_y, end_x, end_y, duration=0.5, waiting_time=5):
    """
    Symuluje przeciągnięcie palcem.

    start_x, start_y - punkt rozpoczęcia
    end_x, end_y     - punkt zakończenia
    duration         - czas trwania gestu w sekundach
    """

    log(f"Swipe: ({start_x}, {start_y}) -> "
        f"({end_x}, {end_y})")

    pyautogui.moveTo(start_x, start_y, duration=0.1)

    pyautogui.dragTo(
        end_x,
        end_y,
        duration=duration,
        button="left"
    )

    time.sleep(waiting_time)

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(timestamp, "|", message)

# =========================
# GŁÓWNY PROGRAM
# =========================

def main(nIteration=1, toRestart =0):

    # if (nIteration == 1):
    toRestartInNextRun = toRestart
    vGdaOp_Tuth_turned_on = 0
    vGdaOp_TaG_turned_on = 0
    vGdaOp_DD_turned_on = 0
    vGdaOp_Gotg_turned_on = 0
    vGdaOp_RR_turned_on = 0
    vGdaOp_TiH_turned_on = 0
    vGdaOp_EWA_turned_on = 0
    vGdaOp_WD_turned_on = 0
    iStoreToCheck = 1                     
    # if (1==0):
    #     open the game
    
    start_game()

    if nIteration % 10 == 0 or toRestartInNextRun == 1:
        close_game()
        if nIteration % 10 == 0:
            log(f"Restart game each 10 iteration...")
        else:
            log(f"There were no matching search in previous iteration. Game will be restarted...")
        start_game()

    toRestartInNextRun = 1

    # geometry = get_bluestacks_geometry()
    # set_bluestacks_window(x=-320, y=0)
    # print(geometry)
    iStop = 0
    while iStop < 10 and (find_screenshot(SERVER_ISSUE_RESTART_IMAGE, timeout=5) or find_screenshot(RESTART_IMAGE, timeout=5) or find_screenshot(MAIN_LOADING_SCREEN_IMAGE, timeout=5)):
        # check if game needs to be restarted
        # click_button(SERVER_ISSUE_RESTART_IMAGE, waiting_time=120, timeout=3)
        # click_button(RESTART_IMAGE, waiting_time=120, timeout=1)
        close_game()
        log(f"There is a issue, game will be restarted...")
        start_game()
        iStop += 1

    if find_screenshot(ADVERTISEMENT_LABEL_IMAGE):
        set_bluestacks_window(x=-320, y=0)
    else:
        set_bluestacks_window(x=0, y=0)

    iStop = 0
    while iStop < 10 and find_screenshot(CLOSE_AD_IMAGE, timeout=5, waiting_time=0.5):
        # close add and all messages
        click_button(CLOSE_AD_IMAGE, waiting_time=3, timeout=1)
        toRestartInNextRun = 0
        iStop += 1
         
    if find_screenshot(CAMPAIGN_IMAGE, timeout=5):
        # go to the main screen
        click_button(CAMPAIGN_IMAGE, waiting_time=1, timeout=1)
        toRestartInNextRun = 0
        # take reawrds
        if nIteration % 10 == 0:
            if find_screenshot(FULL_USER_REWARD_IMAGE, confidence=0.95, timeout=5, waiting_time=0.5):
                # run if there is possibility
                click_button(FULL_USER_REWARD_IMAGE, waiting_time=1, timeout=2)
                click_button(FULL_USER_REWARD_CLAIM_IMAGE, waiting_time=1, timeout=5)
                log(f"Campain rewards collected.")
                toRestartInNextRun = 0

        # take free daily/weekly/monthly gems
        if nIteration % 20 == 0:
            iStoreToCheck = 1
            if iStoreToCheck == 1 and find_screenshot(STORE_FREE_INFO_IMAGE, confidence=0.8, waiting_time=1):
                iStoreToCheck = 0
                click_button(STORE_FREE_INFO_IMAGE, confidence=0.7, waiting_time=2)
                if find_screenshot(STORE_TIME_LIMITED_TAB_WITH_FREE_STAFF_IMAGE, confidence=0.8, waiting_time=1):
                    click_button(STORE_TIME_LIMITED_TAB_WITH_FREE_STAFF_IMAGE, confidence=0.7, waiting_time=2)
                    if find_screenshot(STORE_TIME_LIMITED_TAB__DAILY_WITH_FREE_STAFF_IMAGE, confidence=0.8, waiting_time=1):
                        click_button(STORE_TIME_LIMITED_TAB__DAILY_WITH_FREE_STAFF_IMAGE, confidence=0.7, waiting_time=2)
                        if find_screenshot(STORE_TIME_LIMITED_TAB_DAILY_FREE_GEMS_IMAGE, confidence=0.8, waiting_time=1):
                            click_button(STORE_TIME_LIMITED_TAB_DAILY_FREE_GEMS_IMAGE, confidence=0.7, waiting_time=2)
                            click_button_with_screenshot(STORE_TIME_LIMITED_TAB__DAILY_TAB_TO_CONTINUE_IMAGE, confidence=0.7, waiting_time=2)
                            log(f"Daily gems has been collected")
                # framgnet to odbioru tygodniowych i miesięcznych
                # if ...

                iStop = 0
                while iStop < 5 and find_screenshot(STORE_BACK_IMAGE, waiting_time=1):
                    click_button(STORE_BACK_IMAGE, waiting_time=1)
                    iStop += 1

    # open GDA HUB
    if find_screenshot(GDA_HUB_IMAGE, timeout=5, waiting_time=0.5):
        click_button(GDA_HUB_IMAGE, waiting_time=1, timeout=3)
        toRestartInNextRun = 0
    # open GDA OPS list
    if find_screenshot(GDA_OPS_IMAGE, timeout=5, waiting_time=0.5):
        click_button(GDA_OPS_IMAGE, waiting_time=1, timeout=3)
        toRestartInNextRun = 0

    if find_screenshot(GDA_CLAIM_ALL_IMAGE, timeout=15, waiting_time=2):
        # restart more then one OPS
        click_button(GDA_CLAIM_ALL_IMAGE, waiting_time=10, timeout=15)
        find_screenshot(GDA_RESTART_ALL_IMAGE, confidence=0.6, waiting_time=5)
        click_button_with_screenshot(GDA_RESTART_ALL_IMAGE, confidence=0.6, waiting_time=5, timeout=60)
        log(f"Operation rewards collected from multiple GDA Ops.")
        toRestartInNextRun = 0
    else:

        if find_screenshot(SINGLE_CLAIM_IMAGE, timeout=15, waiting_time=1):
            # restart single OP
            click_button(SINGLE_CLAIM_IMAGE, waiting_time=7, timeout=5)
            click_button_with_screenshot(PLAY_AGAIN_IMAGE, waiting_time=7, timeout=10)
            click_button(BATTLE_IMAGE, waiting_time=7, timeout=10)
            click_button(GDA_BACK_IMAGE, waiting_time=3, timeout=10)
            toRestartInNextRun = 0

        # chcemy to zamienić na obsługe tych ikon na górnej belce, kiedy mają już złota obwódkę
        # if find_screenshot(FINISHED_GDA_OP_GOLD_IMAGE, confidence=0.99, timeout=10):
        #     # restart single OP - Turning up the heat
        #     click_button(FINISHED_GDA_OP_GOLD_IMAGE, waiting_time=7, timeout=5)
        #     click_button_with_screenshot(PLAY_AGAIN_IMAGE, waiting_time=7, timeout=15)
        #     click_button(BATTLE_IMAGE, waiting_time=7, timeout=10)
        #     log(f"Operation rewards collected from TuTh Op.")
        #     click_button(GDA_BACK_IMAGE, waiting_time=3, timeout=10)

        # if find_screenshot(FINISHED_GDA_OP_RR_IMAGE, confidence=0.95, timeout=10):
        #     # restart single OP
        #     click_button(FINISHED_GDA_OP_RR_IMAGE, waiting_time=7, timeout=5)
        #     click_button_with_screenshot(PLAY_AGAIN_IMAGE, waiting_time=7, timeout=15)
        #     click_button(BATTLE_IMAGE, waiting_time=7, timeout=10)
        #     log(f"Operation rewards collected from WD Op.")
        #     click_button(GDA_BACK_IMAGE, waiting_time=3, timeout=10)

        # ad same thig fot TiH
        # ...

        # if find_screenshot(FINISHED_GDA_OP_SCHOOLSOUT_IMAGE, confidence=0.95, timeout=10):
        #     # restart single OP
        #     click_button(FINISHED_GDA_OP_SCHOOLSOUT_IMAGE, waiting_time=7, timeout=5)
        #     # click_button_with_screenshot(PLAY_AGAIN_IMAGE, waiting_time=7, timeout=15)
        #     # click_button(BATTLE_IMAGE, waiting_time=7, timeout=10)
        #     log(f"Operation rewards collected from Schools Out Op.")
        #     click_button(GDA_BACK_IMAGE, waiting_time=3, timeout=10)
        
        # if vGdaOp_WD_turned_on == 0 and find_screenshot(FINISHED_GDA_OP_WD_IMAGE, confidence=0.95, timeout=10):
        #     # restart single OP
        #     click_button(FINISHED_GDA_OP_WD_IMAGE, waiting_time=7, timeout=5)
        #     click_button_with_screenshot(PLAY_AGAIN_IMAGE, waiting_time=7, timeout=15)
        #     click_button(BATTLE_IMAGE, waiting_time=7, timeout=10)
        #     log(f"Operation rewards collected from WD Op.")
        #     vGdaOp_WD_turned_on = 1
        #     click_button(GDA_BACK_IMAGE, waiting_time=3, timeout=10)
        #     toRestartInNextRun = 0
        
        # if vGdaOp_TiH_turned_on == 0 and find_screenshot(FINISHED_GDA_OP_TIH_IMAGE, confidence=0.95, timeout=10):
        #     # restart single OP
        #     click_button(FINISHED_GDA_OP_TIH_IMAGE, waiting_time=7, timeout=5)
        #     click_button_with_screenshot(PLAY_AGAIN_IMAGE, waiting_time=7, timeout=15)
        #     click_button(BATTLE_IMAGE, waiting_time=7, timeout=10)
        #     log(f"Operation rewards collected from GOTG Op.")
        #     vGdaOp_TiH_turned_on = 1
        #     click_button(GDA_BACK_IMAGE, waiting_time=3, timeout=10)
        #     toRestartInNextRun = 0

        # if vGdaOp_Gotg_turned_on == 0 and find_screenshot(FINISHED_GDA_OP_GOTG_IMAGE, confidence=0.95, timeout=10):
        #     # restart single OP
        #     click_button(FINISHED_GDA_OP_GOTG_IMAGE, waiting_time=7, timeout=5)
        #     click_button_with_screenshot(PLAY_AGAIN_IMAGE, waiting_time=7, timeout=15)
        #     click_button(BATTLE_IMAGE, waiting_time=7, timeout=10)
        #     log(f"Operation rewards collected from GOTG Op.")
        #     vGdaOp_Gotg_turned_on = 1
        #     click_button(GDA_BACK_IMAGE, waiting_time=3, timeout=10)
        #     toRestartInNextRun = 0

        # if vGdaOp_EWA_turned_on == 0 and find_screenshot(FINISHED_GDA_OP_EWA_IMAGE, confidence=0.95, timeout=10):
        #     # restart single OP
        #     click_button(FINISHED_GDA_OP_EWA_IMAGE, waiting_time=7, timeout=5)
        #     click_button_with_screenshot(PLAY_AGAIN_IMAGE, waiting_time=7, timeout=15)
        #     click_button(BATTLE_IMAGE, waiting_time=7, timeout=10)
        #     log(f"Operation rewards collected from EWA Op.")
        #     vGdaOp_EWA_turned_on = 1
        #     click_button(GDA_BACK_IMAGE, waiting_time=3, timeout=10)
        #     toRestartInNextRun = 0

        

        # if find_screenshot(GDA_CLAIM_ALL_IMAGE, timeout=15):
        #     # restart more then one OPS
        #     click_button(GDA_CLAIM_ALL_IMAGE, waiting_time=10, timeout=15)
        #     click_button_with_screenshot(GDA_RESTART_ALL_IMAGE, confidence=0.6, waiting_time=5, timeout=60)
        #     log(f"Operation rewards collected from multiple GDA Ops.")
        #     toRestartInNextRun = 0

        if find_screenshot(EMPTY_SLOT_GDA_OP_IMAGE, timeout=15):
            iStop = 0
            while iStop < 5 and find_screenshot(START_IMAGE, timeout=15, waiting_time=1):
                # run if there is not runned OP
                click_button(START_IMAGE, waiting_time=7, timeout=5)
                click_button(BATTLE_IMAGE, waiting_time=7)
                click_button(GDA_BACK_IMAGE, waiting_time=3)
                toRestartInNextRun = 0
                iStop += 1
            
            iStop = 0
            if find_screenshot(TUTH_SCROLL_COORD_IMAGE, timeout=10, waiting_time=1):
                (x_s, y_s) = find_coordinates(TUTH_SCROLL_COORD_IMAGE)
            else:
                (x_s, y_s) = (392, 262)
            if find_screenshot(DD_SCROLL_COORD_IMAGE, timeout=10, waiting_time=1):
                (x_e, y_e) = find_coordinates(DD_SCROLL_COORD_IMAGE)
            else: 
                (x_e, y_e) = (397, 594)
            while iStop < 8 and find_screenshot(EMPTY_SLOT_GDA_OP_IMAGE, timeout=15):
                toRestartInNextRun = 0
                swipe(x_e, y_e, x_s, y_s, duration=0.5)

                while vGdaOp_RR_turned_on == 0 and find_screenshot(GDA_OP_RR_BANNER_IMAGE, timeout=10, confidence=0.95, waiting_time=1):
                    # run if there is not runned OP
                    click_button(GDA_OP_RR_BANNER_IMAGE, waiting_time=7, timeout=5)
                    click_button(BATTLE_IMAGE, waiting_time=7)
                    vGdaOp_RR_turned_on = 1
                    click_button(GDA_BACK_IMAGE, waiting_time=3)
                    toRestartInNextRun = 0
                    break

                while vGdaOp_TiH_turned_on == 0 and find_screenshot(GDA_OP_TIH_BANNER_IMAGE, timeout=10, confidence=0.95, waiting_time=1):
                    # run if there is not runned OP
                    click_button(GDA_OP_TIH_BANNER_IMAGE, waiting_time=7, timeout=5)
                    click_button(BATTLE_IMAGE, waiting_time=7)
                    vGdaOp_TiH_turned_on = 1
                    click_button(GDA_BACK_IMAGE, waiting_time=3)
                    toRestartInNextRun = 0
                    break

                while vGdaOp_EWA_turned_on == 0 and find_screenshot(GDA_OP_EWA_BANNER_IMAGE, timeout=10, confidence=0.95, waiting_time=1):
                    # run if there is not runned OP
                    click_button(GDA_OP_EWA_BANNER_IMAGE, waiting_time=7, timeout=5)
                    click_button(BATTLE_IMAGE, waiting_time=7)
                    vGdaOp_EWA_turned_on = 1
                    click_button(GDA_BACK_IMAGE, waiting_time=3)
                    toRestartInNextRun = 0
                    break

                while vGdaOp_WD_turned_on == 0 and find_screenshot(GDA_OP_WD_BANNER_IMAGE, timeout=10, confidence=0.95, waiting_time=1):
                    # run if there is not runned OP
                    click_button(GDA_OP_WD_BANNER_IMAGE, waiting_time=7, timeout=5)
                    click_button(BATTLE_IMAGE, waiting_time=7)
                    vGdaOp_WD_turned_on = 1
                    click_button(GDA_BACK_IMAGE, waiting_time=3)
                    toRestartInNextRun = 0
                    break

                while find_screenshot(SINGLE_CLAIM_IMAGE, timeout=15, waiting_time=1):
                    # restart single OP
                    click_button(SINGLE_CLAIM_IMAGE, waiting_time=7, timeout=5)
                    click_button_with_screenshot(PLAY_AGAIN_IMAGE, waiting_time=7, timeout=10)
                    click_button(BATTLE_IMAGE, waiting_time=7, timeout=10)
                    click_button(GDA_BACK_IMAGE, waiting_time=3, timeout=10)
                    toRestartInNextRun = 0
                    break
                iStop+=1

    # open GDA HUB
    if find_screenshot(GDA_HUB_IMAGE, timeout=5, waiting_time=0.5):
        click_button(GDA_HUB_IMAGE, waiting_time=1, timeout=3)
        toRestartInNextRun = 0
    # open GDA OPS list
    if find_screenshot(GDA_OPS_IMAGE, timeout=5, waiting_time=0.5):
        click_button(GDA_OPS_IMAGE, waiting_time=1, timeout=3)
        toRestartInNextRun = 0
    # go to events tab
    if find_screenshot(GDA_EVENTS_IMAGE, timeout=5, waiting_time=0.5):
        click_button(GDA_EVENTS_IMAGE, waiting_time=1, timeout=3)
        toRestartInNextRun = 0
        if find_screenshot(SINGLE_CLAIM_IMAGE, timeout=15, waiting_time=1):
            # restart operation
            click_button(SINGLE_CLAIM_IMAGE, waiting_time=7, timeout=5)
            click_button_with_screenshot(PLAY_AGAIN_IMAGE, waiting_time=7)
            toRestartInNextRun = 0
            if find_screenshot(GDA_EVENT_RANK_UP_TAB_IMAGE, timeout=15, confidence=0.95, waiting_time=1):
                # rank up to higher level
                click_button(GDA_EVENT_RANK_UP_TAB_IMAGE, waiting_time=7, timeout=5)
                toRestartInNextRun = 0
                iStop = 0
                while iStop < 7 and find_screenshot(GDA_EVENT_RANK_UP_BUTTON_IMAGE, timeout=15, confidence=0.95, waiting_time=1):
                    click_button(GDA_EVENT_RANK_UP_BUTTON_IMAGE, waiting_time=5, timeout=5)
                    toRestartInNextRun = 0
                    iStop += 1
                click_button(GDA_EVENT_PREBATTLE_UP_TAB_IMAGE, waiting_time=7, timeout=5)
                # dopisać w zasadzie feamgnet o tym autofil jeśli jest puste
                if find_screenshot(GDA_EVENT_INACTIVE_BATTLE_IMAGE, timeout=15, waiting_time=1):
                    click_button(GDA_EVENT_AUTOFILL_IMAGE, waiting_time=7, timeout=10)
                    toRestartInNextRun = 0
                click_button(GDA_EVENT_ACTIVE_BATTLE_IMAGE, waiting_time=7, timeout=10)
            click_button(BATTLE_IMAGE, waiting_time=7)
            log(f"Operation rewards collected from GDA Event.")
            toRestartInNextRun = 0
            click_button(GDA_BACK_IMAGE, waiting_time=3)
        elif find_screenshot(GDA_EVENT_GDA_BANNER_IMAGE, timeout=15, confidence=0.95, waiting_time=1) or find_screenshot(GDA_EVENT_FWB_BANNER_IMAGE, timeout=15, confidence=0.95, waiting_time=1):
            # run if there is possibility
            click_button(START_IMAGE, waiting_time=7, timeout=5)
            toRestartInNextRun = 0
            if find_screenshot(GDA_EVENT_RANK_UP_TAB_IMAGE, timeout=15, confidence=0.95, waiting_time=1):
                # rank up to higher level
                click_button(GDA_EVENT_RANK_UP_TAB_IMAGE, waiting_time=7, timeout=5)
                toRestartInNextRun = 0
                iStop = 0
                while iStop < 7 and find_screenshot(GDA_EVENT_RANK_UP_BUTTON_IMAGE, timeout=15, confidence=0.95, waiting_time=1):
                    click_button(GDA_EVENT_RANK_UP_BUTTON_IMAGE, waiting_time=5, timeout=5)
                    toRestartInNextRun = 0
                    iStop += 1
                click_button(GDA_EVENT_PREBATTLE_UP_TAB_IMAGE, waiting_time=7, timeout=5)
            # dopisać w zasadzie feamgnet o tym autofil jeśli jest puste
            if find_screenshot(GDA_EVENT_INACTIVE_BATTLE_IMAGE, timeout=15, waiting_time=1):
                click_button(GDA_EVENT_AUTOFILL_IMAGE, waiting_time=7, timeout=10)
                toRestartInNextRun = 0
            click_button(GDA_EVENT_ACTIVE_BATTLE_IMAGE, waiting_time=7, timeout=10)
            log(f"GDA Event has been launched.")
            click_button(GDA_BACK_IMAGE, waiting_time=3, timeout=10)
            toRestartInNextRun = 0
        

    iStop = 0
    while iStop < 8 and find_screenshot(GDA_BACK_IMAGE, waiting_time=0.5):
        # go back to main page
        click_button(GDA_BACK_IMAGE, waiting_time=1.5, timeout=3)
        toRestartInNextRun = 0
        iStop += 1
    
    # sprawdzenie czy można stoczyć bitwę w alliance - jeśli można to to zrób
    # if nIteration ==  1 or nIteration % 10 == 0:
    if nIteration % 10 == 0:
        if find_screenshot(SOCIAL_HUB_IMAGE, timeout=15, waiting_time=0.5):
            click_button(SOCIAL_HUB_IMAGE, waiting_time=1.5, timeout=3)
            toRestartInNextRun = 0
            # Boss raid:
            if find_screenshot(BOSS_RAID_IMAGE, timeout=15, waiting_time=1):
                click_button(BOSS_RAID_IMAGE, waiting_time=5, timeout=3)
                toRestartInNextRun = 0
                # claim tokens from other alliance memeber:
                if find_screenshot(BOSS_RAID_OTHER_USERS_REWARDS_IMAGE, timeout=10, waiting_time=1):
                    click_button(BOSS_RAID_OTHER_USERS_REWARDS_IMAGE, waiting_time=5, timeout=3)
                    log(f"BOSS RAID rewards collected.")
                    toRestartInNextRun = 0
                # if it possible then go for a battle:
                iStop = 0
                while iStop < 3 and find_screenshot(BOSS_RAID_BATTLE_FIRST_IMAGE, timeout=10, waiting_time=1):
                    click_button(BOSS_RAID_BATTLE_FIRST_IMAGE, waiting_time=5, timeout=3)
                    # if slots are empty just click autofill:
                    click_button(BOSS_RAID_BATTLE_AUTOFILL_IMAGE, waiting_time=5, timeout=5)
                    click_button(BOSS_RAID_START_BATTLE_IMAGE, waiting_time=60, timeout=5)
                    click_button_with_screenshot(BOSS_RAID_CLAIM_OWN_BATTLE_IMAGE, waiting_time=5, timeout=60)
                    log(f"BOSS RAID battle finished succesfully.")
                    toRestartInNextRun = 0
                    iStop += 1
                click_button(BOSS_RAID_BACK_IMAGE, waiting_time=5, timeout=5)
            # alliance - collect reward and go for battle:
            if find_screenshot(ALLIANCES_IMAGE, timeout=10):
                click_button(ALLIANCES_IMAGE, waiting_time=10, timeout=3)
                toRestartInNextRun = 0
                # go for alliance battle
                if find_screenshot(ALLIANCES_FIRST_BATTLE_IMAGE, timeout=10):
                    click_button(ALLIANCES_FIRST_BATTLE_IMAGE, waiting_time=5, timeout=3)
                    # if slots are empty just click autofill:
                    click_button(ALLIANCES_LAST_BATTLE_IMAGE, waiting_time=5, timeout=5)
                    find_screenshot(ALLIANCES_CLAIM_BATTLE_IMAGE, timeout=10, waiting_time=3)
                    click_button_with_screenshot(ALLIANCES_CLAIM_BATTLE_IMAGE, waiting_time=120, timeout=5)
                    log(f"Alliance battle finished succesfully.")
                    toRestartInNextRun = 0
                # claim alliance reward
                if find_screenshot(ALLIANCES_WAVES_REWARDS_IMAGE, timeout=10):
                    click_button(ALLIANCES_WAVES_REWARDS_IMAGE, waiting_time=3, timeout=3)
                    find_screenshot(ALLIANCES_WAVES_REWARDS_CLAIM_IMAGE, timeout=10, waiting_time=2)
                    click_button_with_screenshot(ALLIANCES_WAVES_REWARDS_CLAIM_IMAGE, waiting_time=4)
                    log(f"Alliance rewards has been collected")
                    toRestartInNextRun = 0
                click_button(GDA_BACK_IMAGE, waiting_time=5, timeout=7)
            # FIRNEDS - collect reward 
            if find_screenshot(FRIENDS_IMAGE, timeout=10):
                click_button(FRIENDS_IMAGE, waiting_time=10, timeout=3)
                toRestartInNextRun = 0
                # go for alliance battle
                if find_screenshot(FRIENDS_CLAIM_ALL_IMAGE, timeout=10) or find_screenshot(FRIENDS_CLAIM_ALL_2_IMAGE, timeout=10):
                    click_button(FRIENDS_CLAIM_ALL_IMAGE, waiting_time=5, timeout=3)
                    click_button(FRIENDS_CLAIM_ALL_2_IMAGE, waiting_time=5, timeout=3)
                    # add mayby while loop for tap_To_continue, cuz there can be also second screen (for new level of friendship)
                    iStop = 0
                    while iStop < 5 and find_screenshot(FRIENDS_TAP_TO_CONTINUE_IMAGE, timeout=10, confidence=0.5):
                        click_button_with_screenshot(FRIENDS_TAP_TO_CONTINUE_IMAGE, waiting_time=5, timeout=5)
                        toRestartInNextRun = 0
                        iStop += 1
                    log(f"Friends gifts collected succesfully.")
                        
                    toRestartInNextRun = 0
                if find_screenshot(FRIENDS_CLAIM_SINGLE_IMAGE, timeout=10):
                    click_button(FRIENDS_CLAIM_SINGLE_IMAGE, waiting_time=5, timeout=3)
                    # add mayby while loop for tap_To_continue, cuz there can be also second screen (for new level of friendship)
                    iStop = 0
                    while iStop < 2 and find_screenshot(FRIENDS_TAP_TO_CONTINUE_IMAGE, timeout=10, confidence=0.5):
                        click_button_with_screenshot(FRIENDS_TAP_TO_CONTINUE_IMAGE, waiting_time=5, timeout=5)
                        toRestartInNextRun = 0
                        iStop += 1
                    log(f"Friend gift collected succesfully.")
                    toRestartInNextRun = 0
                if find_screenshot(FRIENDS_5_NEW_DAYS_REWARD_IMAGE, timeout=10):
                    click_button(FRIENDS_5_NEW_DAYS_REWARD_IMAGE, waiting_time=5, timeout=3)
                    # add mayby while loop for tap_To_continue, cuz there can be also second screen (for new level of friendship)
                    iStop = 0
                    while iStop < 3 and find_screenshot(FRIENDS_5_NEW_DAYS_REWARD_CLOSE_IMAGE, timeout=10, confidence=0.9):
                        click_button_with_screenshot(FRIENDS_5_NEW_DAYS_REWARD_CLOSE_IMAGE, waiting_time=5, timeout=5)
                        toRestartInNextRun = 0
                        iStop += 1
                    log(f"New 5 days with friends gift collected succesfully.")
                    toRestartInNextRun = 0
                # add condition for taking rewars for each 5 day
                # if...
                click_button(GDA_BACK_IMAGE, waiting_time=5, timeout=7)
            # ODEBRANIE PREZENTÓW OD ZNAJOMYCH
        
    # dodać obsługe tego tylko raz na X cykli
 
    # resfresh shops
    # dodać obsługe tego tylko raz na X cykli
    iStop = 0
    iEventToCheck = 1
    iEquipmentToCheck = 1
    while iStop < 6:
        click_button(SHOP_IMAGE, waiting_time=1)
        iStop += 1
        if iEventToCheck == 1 and find_screenshot(LLOD_EVENT_BANNER_IMAGE, confidence=0.9, waiting_time=1):
            iEventToCheck = 0
            toRestartInNextRun = 0
            iStop3 = 0
            while iStop3 < 3 and find_screenshot(LLOD_EVENT_BUY_ALL_IMAGE, confidence=0.95, waiting_time=1):
                iStop3 += 1
                click_button(LLOD_EVENT_BUY_ALL_IMAGE, waiting_time=2)
                log(f"Heroes has been obtained.")
                click_button_with_screenshot(LLOD_EVENT_TAP_TO_CONTINOU_IMAGE, waiting_time=1)
                if find_screenshot(LLOD_EVENT_CLOSE_SHOP_LVL_IMAGE, confidence=0.9, waiting_time=1):
                    click_button_with_screenshot(LLOD_EVENT_CLOSE_SHOP_LVL_IMAGE, waiting_time=1)
                    log(f"Shop has been promoted to higher lvl.")
                iStop2 = 0
                while iStop2 < 4 and find_screenshot(LLOD_EVENT_FREE_FEFRESH_CHECK_IMAGE, confidence=1, waiting_time=1):
                    iStop2 += 1
                    click_button(LLOD_EVENT_REFRESH_NOW_IMAGE, waiting_time=2)
        elif iEquipmentToCheck == 1 and find_screenshot(SHOPS_EQUIPMENT_ON_LIST_IMAGE, confidence=0.99, waiting_time=1):
            iEquipmentToCheck = 0
            iStop3 = 0
            while iStop3 < 6 and find_screenshot(SHOP_EQUIPMENT_BUY_VIA_GOLD_IMAGE, confidence=0.7, waiting_time=1):
                iStop3 += 1
                click_button(SHOP_EQUIPMENT_BUY_VIA_GOLD_IMAGE, confidence=0.7, waiting_time=2)
                log(f"Item has ben purchased in a equipment shop.")
                click_button_with_screenshot(SHOPS_EQUIPMENT_TAP_TO_CONTINUE_IMAGE, confidence=0.6, waiting_time=1)
    log(f"Shops has been refreshed.")
    log(f"Done!")

    return toRestartInNextRun
    
# if __name__ == "__main__":
#     main()

if __name__ == "__main__":

    INTERVAL = 8 * 60
    ITERATION = 1
    PREVIOUS_ITERATION = 0
    while True:

        cycle_start = time.time()

        try:
            print("\n==============================")
            log(f"STARTING NEW CYCLE #{ITERATION}")
            print("==============================\n")
            PREVIOUS_ITERATION = main(nIteration=ITERATION, toRestart=PREVIOUS_ITERATION)

        except Exception as e:
            log(f"Issue occurs: {e}")

        elapsed = time.time() - cycle_start

        log(f"Cycle #{ITERATION} took {elapsed:.1f} seconds.")

        ITERATION += 1

        # Obliczenie godziny kolejnego cyklu
        next_run = datetime.now() + timedelta(seconds=INTERVAL)

        print(
            f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} | Next cycle starts #{ITERATION} at "
            f"{next_run.strftime('%H:%M:%S')}"
        )

        time.sleep(INTERVAL)