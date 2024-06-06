import sys
# pyc 생성 방지
sys.dont_write_bytecode = True
#QRC 업데이트
from qcr_converter import run_pyrcc5
# run_pyrcc5()
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsBlurEffect
import os 
import MyQRC_rc
import copy
import sys
import os
import random
from PyQt5.QtGui import QFont, QFontDatabase
# 모듈이 위치한 디렉토리를 지정합니다.
module_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Agricola/Agricola')
# sys.path에 모듈 디렉토리를 추가합니다.

if module_dir not in sys.path:
    sys.path.append(module_dir)
from Agricola.Agricola.repository import player_status_repository,game_status_repository,round_status_repository,undo_repository
from Agricola.Agricola.entity.field_type import FieldType
from Agricola.Agricola.entity.house_type import HouseType
from Agricola.Agricola.entity.crop_type import CropType
from Agricola.Agricola.entity.animal_type import AnimalType


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
#UI파일 연결
main = uic.loadUiType(resource_path("data/mainwindow_v1.ui"))[0] # 진짜 메인
###개인 영역 UI들###
personal_field_ui = uic.loadUiType(resource_path("data/PersonalField/field_frame.ui"))[0] # 농장 15개 빈칸 뚫린 ui
field_base_ui = uic.loadUiType(resource_path("data/PersonalField/field_base.ui"))[0] # field 하나 ui
personal_resources_ui= uic.loadUiType(resource_path("data/PersonalField/personal_resource.ui"))[0] # 화면 전환되는 개인 자원
personal_card_ui= uic.loadUiType(resource_path("data/PersonalField/personal_card.ui"))[0] # 내가 낸 카드 ui
personal_card_small_ui = uic.loadUiType(resource_path("data/PersonalField/mycard_small.ui"))[0] # 내가 낸 카드 ui
personal_card_big_ui = uic.loadUiType(resource_path("data/PersonalField/mycard_big.ui"))[0] # 내가 낸 카드 ui
#personal_card_ui= uic.loadUiType(resource_path("PersonalField/mycards.ui"))[0] # 개인 카드 ui

###공동 영역 UI들###
log_viewer_ui= uic.loadUiType(resource_path("data/log_viewer_dialog.ui"))[0] # 로그
basic_roundcard_ui= uic.loadUiType(resource_path("data/Basic/roundcard.ui"))[0] # 라운드카드 ui
worker_board_ui = uic.loadUiType(resource_path("data/Basic/worker_board.ui"))[0] # worker 보드
check_ui = uic.loadUiType(resource_path("data/check/check.ui"))[0] # worker 보드
text_log_ui = uic.loadUiType(resource_path("data/Basic/log.ui"))[0] # text log 박스
information_ui = uic.loadUiType(resource_path("data/Basic/information.ui"))[0] # information(설정, 점수표)
scoreboard_ui = uic.loadUiType(resource_path("data/Basic/scoreboard.ui"))[0] # 점수표
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
# field_0_ui
#  = uic.loadUiType("main.ui")[0]

# MAIN
class MainWindowClass(QMainWindow, main) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        font_path = os.path.join(os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'),'font'),'Pretendard-Medium.otf')
        
        # 폰트 파일 로드
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            pass
            # print("Failed to load font")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            font = QFont(font_family, 9)  # 로드된 폰트를 기본 폰트로 설정
            app.setFont(font)
        self.player_status = player_status_repository.PlayerStatusRepository().player_status
        self.game_status = game_status_repository.GameStatusRepository().game_status
        self.round_status = round_status_repository.RoundStatusRepository().round_status
        #플레이어 필드 위젯 설정
        self.personal_field = [WidgetPersonalField(i,self) for i in range(5)]
        for i in range(4):getattr(self,f"frm_p{i}_0").addWidget(self.personal_field[i])
        #메인 필드 위젯 설정
        self.frm_main_field.addWidget(self.personal_field[4])
        #플레이어 카드 위젯 설정
        self.personal_card = [PersonalCard_small(i,self) for i in range(4)]
        for i in range(4):getattr(self,f"frm_p{i}_1").addWidget(self.personal_card[i])
        #메인 카드 위젯 설정
        self.frm_main_card.addWidget(PersonalCard_big(self))
        
        #플레이어 리소스 위젯 설정
        self.personal_resource = [WidgetPersonalResource(i,self) for i in range(4)]
        for i in range(4):getattr(self,f"frm_p{i}_2").addWidget(self.personal_resource[i])
        #베이직 라운드 위젯 설정
        self.basic_round = [WidgetBasicRound(i,self) for i in range(16)]
        [getattr(self,f"basic_{i}").addWidget(self.basic_round[i]) for i in range(16)]
        numbers = list(range(14))
        random.shuffle(numbers)
        self.random_round = [WidgetrandomRound(i,numbers[i],self) for i in range(14)]
        [getattr(self,f"basic_{i+16}").addWidget(self.random_round[i]) for i in range(14)]


        self.worker_board = WorkerBoard(self)
        self.vlo_etc_workerboard.addWidget(self.worker_board)
        #텍스트 로그 창 설정
        # self.text_log = WidgetTextLog(self)
        # self.vlo_etc_log.addWidget(self.text_log)
        #인포메이션 칸(설정, 점수표)
        self.information = WidgetInformation(self)
        self.vlo_etc_information.addWidget(self.information)

        self.Class_check = Check(self)
        self.verticalLayout_37.addWidget(self.Class_check)
        ####################################init####################################
        self.timer_close,self.timer_open = QTimer(self),QTimer(self)
        self.log.clicked.connect(self.change_main_stacked)
        self.log.clicked.connect(self.update_state_of_all)
        self.pushButton_3.clicked.connect(self.round_test)
        self.log_popup = Log_viewer(self)
        # def pprint(text):
        #     ppprint("log : ")
        #     ppprint(text)
        # pprint(self.player.player_status[0].worker)
        # self.random_round_suffle()
        self.update_state_of_all()
        self.set_undo()
        ############################################################################

    def round_test(self):
        self.game_status.now_round = (self.game_status.now_round+1)%15
        pprint(f"현재 라운드는 {self.game_status.now_round}라운드입니다.")
        self.update_state_of_all()
        

        [getattr(self,f"basic_{i+16}").addWidget(self.random_round[i]) for i in range(13)]
    def set_undo(self):
        self.undo_player = copy.deepcopy(self.player_status)
        self.undo_gameStatus = copy.deepcopy(self.game_status)
        self.undo_round = copy.deepcopy(self.round_status)
        
    def undo(self):
        self.player_status = self.undo_player
        self.game_status = self.undo_gameStatus
        self.round_status = self.undo_round
        self.set_undo()
        self.update_state_of_all()
        pprint("턴 초기 화면으로 돌아갔습니다.")
    # def logging_dialog(self,text):
    #     self.log.logging(text)
    #     update()
    def pprint(self,text):
        print(text)
        self.log_2.setText(self.log_2.toPlainText()+"\n"+str(text))
        scroll_bar = self.log_2.verticalScrollBar()
        scroll_bar.setValue(scroll_bar.maximum())
        self.log_popup.logging(text)

    def change_main_stacked(self):
        self.update_state_of_all()
        currentWidget = self.stackedWidget.currentWidget().objectName()
        # if index == 0:self.stackedWidget.setCurrentIndex(1)
        # else:self.stackedWidget.setCurrentIndex(0)
        if currentWidget == "round_page":self.change_stacked_page("personal_page")
        else:self.change_stacked_page("round_page")



    def change_stacked_page(self, after_page):
        after_page = getattr(self, after_page)
        stacked_Widget = self.stackedWidget
        if not self.timer_close.isActive() and not self.timer_open.isActive():
            # 이걸로 속도 조절 낮을수록 빠름
            self.speed = 5
            self.timer_close = QTimer(self)
            self.timer_open = QTimer(self)
            self.total_timer_count = 20
            self.current_timer_count = 0
            self.timer_open.stop()
            self.timer_close.stop()
            self.timer_close.timeout.connect(lambda : process_timer_close(self,after_page))
            self.timer_close.start(self.speed)
            self.timer_open.timeout.connect(lambda : process_timer_open(self,after_page))
        def process_timer_close(self,after_page):
            self.opacity_effect = QGraphicsOpacityEffect(stacked_Widget.currentWidget())
            self.opacity_effect_after = QGraphicsOpacityEffect(after_page)
            self.opacity_effect_after.setOpacity(0)
            self.opacity_effect.setOpacity(1-0.05*self.current_timer_count)
            stacked_Widget.currentWidget().setGraphicsEffect(self.opacity_effect)
            self.current_timer_count += 1
            if self.current_timer_count == self.total_timer_count:
                stacked_Widget.setCurrentWidget(after_page)
                while not after_page.isVisible():
                    pass
                # self.title.setText(title)
                self.timer_open.start(self.speed)
                self.timer_close.stop()
                self.opacity_effect_after.setOpacity(1)
        def process_timer_open(self,after_page):
            self.opacity_effect_after.setOpacity(1-0.05*self.current_timer_count)
            after_page.setGraphicsEffect(self.opacity_effect_after)
            self.current_timer_count -= 1
            if self.current_timer_count == 0:
                self.timer_open.stop()

    def update_state_of_all(self):
        #resource 업데이트
        for c in self.personal_field:
            c.update_state()
            for cc in c.field:cc.update_state()
        # for c in self.personal_card:
        #     c.update_state()
        for c in self.personal_resource:
            c.update_state()
        for widget in self.random_round:
            widget.update_state()

class WidgetPersonalField(QWidget, personal_field_ui) :
    def __init__(self, player,parent) :
        super().__init__()
        self.setupUi(self)
        self.player = player
        self.parent = parent
        self.field = [WidgetFieldBase(i,self) for i in range(15) ]# field_0 ~ field_14 까지
        
        tmp_field_num = 0
        for i in range(3):
            for j in range(5):
                field = self.field[tmp_field_num]
                layout = getattr(self, f'hlo_{i}_{j}')
                layout.addWidget(field)
                tmp_field_num += 1

        # fence 객체들에 대하여 버튼 클릭 이벤트 추가
        if self.player == 4:
            for j in range(4):
                for i in range(5):
                    getattr(self, f'btn_fence_h{j}{i}').clicked.connect(lambda _, v="h",i=i,j=j: self.press_fence(v,j,i))
            for j in range(3):
                for i in range(6):
                    getattr(self, f'btn_fence_v{j}{i}').clicked.connect(lambda _,v="v", i=i,j=j: self.press_fence(v,j,i))
        else :
            for j in range(4):
                for i in range(5):
                    getattr(self, f'btn_fence_h{j}{i}').clicked.connect(self.parent.change_main_stacked)
                    getattr(self, f'btn_fence_h{j}{i}').setCheckable(False)
            for j in range(3):
                for i in range(6):
                    getattr(self, f'btn_fence_v{j}{i}').clicked.connect(self.parent.change_main_stacked)
                    getattr(self, f'btn_fence_v{j}{i}').setCheckable(False)

        
    def mousePressEvent(self,event):
        pprint(f"Pressed personalField Player ID : {self.player}")
        if self.player != 4:
            self.parent.change_main_stacked()            
    
    def press_fence(self, v,j,i):
        # try:
        player = myWindow.game_status.now_turn_player
        if v == "v":
            self.parent.player_status[player].farm.vertical_fence[j][i] = not self.parent.player_status[player].farm.vertical_fence[j][i]
        else:
            self.parent.player_status[player].farm.horizon_fence[j][i] = not self.parent.player_status[player].farm.horizon_fence[j][i]

            # self.parent.player_status[self.player].farm.horizon_fence[j][i] = not self.parent.player_status[self.player].farm.horizon_fence[j][i]
        pprint(f"{v}{j}{i}펜스 설치")
        # except:
            # pprint("오류오류")
        pprint(f"Player ID : {self.player} | Fence ID: {v}{j}{i}")
        update()

    def update_state(self):
        # 턴 비활성화
        if self.player == 4:
            player = self.parent.game_status.now_turn_player
        else:
            player = self.player
        self.setEnabled(player == self.parent.game_status.now_turn_player)
        # 펜스 state
        for j in range(4):
            for i in range(5):
                if self.parent.player_status[player].farm.horizon_fence[j][i] == True:
                    getattr(self, f'btn_fence_h{j}{i}').setStyleSheet(f"border:0.5px solid rgba(255, 255, 255, 128);border-image : url(:/newPrefix/images/fence_h_{player}.png);")
                else:
                    getattr(self, f'btn_fence_h{j}{i}').setStyleSheet("border:0.5px solid rgba(255, 255, 255, 128);border-image : none;")
        for j in range(3):
            for i in range(6):
                if self.parent.player_status[player].farm.vertical_fence[j][i] == True:
                    getattr(self, f'btn_fence_v{j}{i}').setStyleSheet(f"border:0.5px solid rgba(255, 255, 255, 128);border-image : url(:/newPrefix/images/fence_v_{player}.png);")
                else:
                    getattr(self, f'btn_fence_v{j}{i}').setStyleSheet("border:0.5px solid rgba(255, 255, 255, 128);border-image : none;")

class WidgetFieldBase(QWidget, field_base_ui) :
    def __init__(self, id,parent):
        super().__init__()
        self.setupUi(self)
        self.id = id # field에게 고유 id (0~14) 부여
        self.i = self.id//5
        self.j = self.id%5
        self.parent = parent
        self.player = self.parent.player
        if self.player == 4:
            self.btn_unit.clicked.connect(self.change_unit)
            self.btn_barn.clicked.connect(self.change_barn)
        else:
            self.btn_unit.clicked.connect(self.parent.parent.change_main_stacked)
            self.btn_barn.clicked.connect(self.parent.parent.change_main_stacked)
          
    def mousePressEvent(self,event):
        if self.player != 4:
            self.parent.parent.change_main_stacked()
        else:
            pprint(f"Pressed Fance Player ID : {self.parent.player} |  ID: {self.id}")
            self.change_house ()
            myWindow.player_status[myWindow.game_status.now_turn_player].farm.field[self.i][self.j].count+=1
            myWindow.update_state_of_all()

    def change_barn(self):
        player = myWindow.game_status.now_turn_player
        pprint(f"Player ID : {player} | Fence ID: {self.id} | Type: barn")

        myWindow.player_status[player].farm.field[self.i][self.j].barn = not myWindow.player_status[player].farm.field[self.i][self.j].barn
        myWindow.update_state_of_all()
        pprint("외양간 변경")
    def change_house(self):
        player = myWindow.game_status.now_turn_player
        # print("player : "+str(player))
        rand = [HouseType.DIRT,HouseType.STONE,HouseType.WOOD]
        rand.remove(getattr(HouseType,myWindow.player_status[player].farm.house_status.name))
        random.shuffle(rand)
        # print(rand)
        myWindow.player_status[player].farm.house_status = rand[0]
        myWindow.update_state_of_all()
    def change_unit(self):
        pprint("change_unit")
        player = myWindow.game_status.now_turn_player
        # print("player : "+str(player))

        rand = [AnimalType.NONE,AnimalType.COW,AnimalType.PIG,AnimalType.SHEEP,CropType.GRAIN,CropType.NONE,CropType.VEGETABLE]
        # print(myWindow.player_status[player].farm.field[self.i][self.j].kind)
        try:
            rand.remove(getattr(AnimalType,myWindow.player_status[player].farm.field[self.i][self.j].kind.name))
        except:
            try:
                rand.remove(getattr(CropType,myWindow.player_status[player].farm.field[self.i][self.j].kind.name))
            except:
                rand = [CropType.GRAIN,CropType.NONE,CropType.VEGETABLE]

        random.shuffle(rand)
        # print(rand)
        # print(rand[0])
        myWindow.player_status[player].farm.field[self.i][self.j].kind = rand[0]
        myWindow.update_state_of_all()
    def update_state(self):
        if self.player == 4:
            player = self.parent.parent.game_status.now_turn_player
        else:
            player = self.player

        CONVERTER_image={(0,0):"empty_field",(0,1):"empty_field",(0,2):"empty_field",(0,3):"empty_field",(1,0):"arable_land",(1,1):"arable_land",(1,2):"arable_land",(1,3):"arable_land",(2,0):"empty_field",(2,1):"empty_field",(2,2):"empty_field",(2,3):"empty_field",(3,1):"house_dirt",(3,2):"house_wood",(3,3):"house_stone"}
        
        # for player in range(4):
        house_status = self.parent.parent.player_status[player].farm.house_status.value # 집 종류 파악
        # print(house_status)

        # 배경화면 바꾸기
        field_status = self.parent.parent.player_status[player].farm.field[self.i][self.j].field_type.value
        self.widget.setStyleSheet(f"#widget{{border-image : url(:/newPrefix/images/{CONVERTER_image[field_status,house_status]}.png);}}")
        # 유닛 처리
        unit = self.parent.parent.player_status[player].farm.field[self.i][self.j].kind
        if not unit==None:
            kind = self.parent.parent.player_status[player].farm.field[self.i][self.j].kind.name.lower()
            if not kind == "none":
                self.btn_unit.setStyleSheet(f"#btn_unit{{border-image : url(:/newPrefix/images/{self.parent.parent.player_status[player].farm.field[self.i][self.j].kind.name.lower()}.png);}}")
            else:
                self.btn_unit.setStyleSheet(f"#btn_unit{{border:none;}}")
        else:
            self.btn_unit.setStyleSheet(f"#btn_unit{{border:none;}}")
        count = self.parent.parent.player_status[player].farm.field[self.i][self.j].count if self.parent.parent.player_status[player].farm.field[self.i][self.j].count not in [0,None] else ""
        self.count.setText(str(count))
        # 외양간 처리
        if self.parent.parent.player_status[player].farm.field[self.i][self.j].barn:
            styleSheet = f"QPushButton#btn_barn {{border-image: url(:/newPrefix/images/barn_{player}.png);}}"
        else:
            styleSheet = f"QPushButton#btn_barn {{border: none;}}"
        self.btn_barn.setStyleSheet(styleSheet)

        pass
        
    
# 개인 농장 오른 쪽 아이콘으로 보이는 작은 카드창
class PersonalCard_small(QWidget, personal_card_small_ui):
    def __init__(self, player, parent):
        super().__init__()
        self.setupUi(self)
        self.player = player
        self.parent = parent
    def mousePressEvent(self, event):
        self.setEnabled(self.player == self.parent.game_status.now_turn_player)
        pprint(f"Pressed personalField Player ID : {self.player}")
        self.parent.change_main_stacked()  
# 메인 창에 뜰 개인별 카드 창
class PersonalCard_big(QWidget, personal_card_big_ui):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
    def mousePressEvent(self, event):
        player = self.parent.game_status.now_turn_player
        pprint(f"Pressed personalField Player ID : {player}")




class WidgetPersonalResource(QWidget, personal_resources_ui) :
    def __init__(self, player,parent) :
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.setupUi(self)
        self.player = player
        self.parent = parent
        self.turn_info_1.setText("")
        self.turn_info_2.setText("")
    def mousePressEvent(self,event):
        pprint(f"Pressed Resource Player ID : {self.player}")
        index = self.stackedWidget.currentIndex()
        if index == 0:self.stackedWidget.setCurrentIndex(1)
        else:self.stackedWidget.setCurrentIndex(0)
    def update_state(self):
        # for player in range(4):
        player = self.player 

        for t in ["dirt","grain","reed","stone","vegetable","wood",'beg_token',"food"]:
            # self.personal_resource[player].count_dirt.setText(str(self.player.player_status[player].resource.dirt))
            getattr(self,f"count_{t}").setText(str(getattr(self.parent.player_status[player].resource,t)))
        # for t in ['sheep','cow','pig']:

        #     # self.personal_resource[player].count_dirt.setText(str(self.player.player_status[player].resource.dirt))
        #     getattr(self,f"count_{t}").setText(str(getattr(self.parent.player_status[player].farm,t)))
            
        getattr(self,f"count_worker").setText(str(self.parent.player_status[player].worker+self.parent.player_status[player].baby))
        "Fence 는 아직 진행중"
        # for t in ["fence",]:
        #     # getattr(self.personal_resource[player],f"count_{t}").setText(str(getattr(self.player_status[player].resource,t)))
        #     getattr(self.personal_resource[player],f"count_{t}")

        if self.parent.game_status.now_turn_player == player:
            self.turn_info_1.setText("NOW")
            self.turn_info_2.setText("NOW")
            self.lb_turn_icon_1.show()
            self.lb_turn_icon_2.show()
        elif self.parent.game_status.next_turn_player ==player:
            self.turn_info_1.setText("NEXT")
            self.turn_info_2.setText("NEXT")
            self.lb_turn_icon_1.hide()
            self.lb_turn_icon_2.hide()
        else :
            self.turn_info_1.setText("")
            self.turn_info_2.setText("")
            self.lb_turn_icon_1.hide()
            self.lb_turn_icon_2.hide()


class WidgetBasicRound(QWidget, basic_roundcard_ui) :
    def __init__(self,num,parent) :
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.parent = parent
        self.num = num
        self.setupUi(self)
        self.btn_round_1.setText('')
        self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/기본행동/기본행동 ({self.num}).png);}}")
        self.btn_round_4.hide()

    def mousePressEvent(self,event):
        pprint(f"Pressed basic round num : {self.num}")
        
class WidgetrandomRound(QWidget, basic_roundcard_ui) :
    def __init__(self, cardnumber,imagenumber,parent) :
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.parent = parent
        self.cardnum = cardnumber
        self.imagenum = imagenumber
        self.setupUi(self)
        self.btn_round_1.setText('')
        self.btn_round_4.hide()
        self.update_state()
    def mousePressEvent(self,event):
        pprint(f"Pressed basic round ID : {self.imagenum}")
        # print(i)
        
    def update_state(self):
        round = self.parent.game_status.now_round
        # print(self.imagenum)
        # print(i)
        
        if self.cardnum<=round-1:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/랜덤/랜덤 ({self.imagenum}).png);}}")
        elif self.cardnum<=3:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/라운드카드/number_1.png);}}")
        elif self.cardnum<=6:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/라운드카드/number_2.png);}}")
        elif self.cardnum<=8:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/라운드카드/number_3.png);}}")
        elif self.cardnum<=10:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/라운드카드/number_4.png);}}")
        elif self.cardnum<=12:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/라운드카드/number_5.png);}}")
        elif self.cardnum<=13:
            self.setStyleSheet(f"#widget{{border-image: url(:/newPrefix/images/라운드카드/number_6.png);}}")

        if self.imagenum<5 and "랜덤/랜덤" in self.styleSheet():
            self.btn_round_1.setText(str(1))
        else:
            self.btn_round_1.setText("")
        if  self.cardnum in [3,6,8,10,12,13]:
            self.btn_round_4.show()
            

class Log_viewer(QDialog,log_viewer_ui):
    def __init__(self,main):
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.log.setText("이 곳은 로그를 표기하는 곳입니다.")
        self.timer = QTimer()
        self.hide()
    def logging(self,text,time=500):
        self.timer.stop()
        self.log.setText(text)
        self.show()
        self.timer.timeout.connect(self.hide)
        self.timer.start(500) 

class WorkerBoard(QWidget, worker_board_ui):
    def __init__(self, parent):
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.setupUi(self)
        self.parent = parent
    def mousePressEvent(self,event):
        pprint(f"player{myWindow.game_status.now_turn_player} 번 말 선택")
        state = getattr(self,f"widget_{myWindow.game_status.now_turn_player}").isEnabled()
        getattr(self,f"widget_{myWindow.game_status.now_turn_player}").setEnabled(not state)
        """
        옵저버에게 status를 전달 받고 라운드카드 활성화 및 안내
        """
        pass
class Check(QWidget, check_ui):
    def __init__(self, parent):
        super().__init__()  # 부모 클래스의 __init__ 함수 호출
        self.setupUi(self)
        self.parent = parent
        self.btn_processing.clicked.connect(self.next_turn)
        self.btn_undo.clicked.connect(self.parent.undo)
    def next_turn(self):
        for i in [0,1,2,3]:
            getattr(self.parent.worker_board,f"widget_{i}").setEnabled(True)
        
        self.parent.game_status.now_turn_player = (self.parent.game_status.now_turn_player+1)%4
        self.parent.game_status.next_turn_player = (self.parent.game_status.now_turn_player+1)%4
        self.parent.update_state_of_all()
        pprint(f"현재 턴은 {self.parent.game_status.now_turn_player}플레이어 입니다.")

        self.parent.set_undo()

    def mousePressEvent(self,event):
        pass

class WidgetTextLog(QWidget, text_log_ui):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
    def mousePressEvent(self,event):
        # 팝업창으로 로그창 크게 보여주기 (중요도 하)
        pass

class WidgetInformation(QWidget, information_ui):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_scoreboard.clicked.connect(self.show_scoreboard)

    def setting(self):
        pass
    def show_scoreboard(self):
        self.scoreboard = Scoreboard(self.parent)
        self.scoreboard.exec_()

class Scoreboard(QDialog, scoreboard_ui):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    def mousePressEvent(self,event):
        self.close()

###실행 코드### 밑에 건들 필요 굳이 없음###
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
    
    #WindowClass의 인스턴스 생성
    myWindow = MainWindowClass()
    global pprint
    pprint = myWindow.pprint
    update = lambda: myWindow.update_state_of_all()
    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()