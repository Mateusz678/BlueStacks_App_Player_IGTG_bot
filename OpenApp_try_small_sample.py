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
def set_bluestacks_window(
    x=0,
    y=0,
    width=1280,
    height=720
):
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
    toRestartInNextRun = 0
    iStop = 0
    iEventToCheck = 1
    iEquipmentToCheck = 1
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