from __future__ import print_function

import sip
import PyQt4.QtCore

def _mockf(*args, **kwargs): pass




def qAlpha(*a,**k): pass

def qBlue(*a,**k): pass

def qDrawBorderPixmap(*a,**k): pass

def qDrawPlainRect(*a,**k): pass

def qDrawShadeLine(*a,**k): pass

def qDrawShadePanel(*a,**k): pass

def qDrawShadeRect(*a,**k): pass

def qDrawWinButton(*a,**k): pass

def qDrawWinPanel(*a,**k): pass

def qFuzzyCompare(*a,**k): pass

def qGray(*a,**k): pass

def qGreen(*a,**k): pass

def qIsGray(*a,**k): pass

def qRed(*a,**k): pass

def qRgb(*a,**k): pass

def qRgba(*a,**k): pass

def qSwap(*a,**k): pass

def qt_x11_wait_for_window_manager(*a,**k): pass

class Display(object):
  pass


  def __init__(self, *args, **kwargs): pass


class QPaintDevice(object):
  pass
  PdmDepth = 6
  PdmDpiX = 7
  PdmDpiY = 8
  PdmHeight = 2
  PdmHeightMM = 4
  PdmNumColors = 5
  PdmPhysicalDpiX = 9
  PdmPhysicalDpiY = 10
  PdmWidth = 1
  PdmWidthMM = 3
  def colorCount(*a,**k): pass
  def depth(*a,**k): pass
  def height(*a,**k): pass
  def heightMM(*a,**k): pass
  def logicalDpiX(*a,**k): pass
  def logicalDpiY(*a,**k): pass
  def metric(*a,**k): pass
  def numColors(*a,**k): pass
  def paintEngine(*a,**k): pass
  def paintingActive(*a,**k): pass
  def physicalDpiX(*a,**k): pass
  def physicalDpiY(*a,**k): pass
  def width(*a,**k): pass
  def widthMM(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPixmap(QPaintDevice):
  pass
  ExplicitlyShared = 1
  ImplicitlyShared = 0
  def alphaChannel(*a,**k): pass
  def cacheKey(*a,**k): pass
  def convertFromImage(*a,**k): pass
  def copy(*a,**k): pass
  def createHeuristicMask(*a,**k): pass
  def createMaskFromColor(*a,**k): pass
  def defaultDepth(*a,**k): pass
  def detach(*a,**k): pass
  def devType(*a,**k): pass
  def fill(*a,**k): pass
  def fromImage(*a,**k): pass
  def fromImageReader(*a,**k): pass
  def fromX11Pixmap(*a,**k): pass
  def grabWidget(*a,**k): pass
  def grabWindow(*a,**k): pass
  def handle(*a,**k): pass
  def hasAlpha(*a,**k): pass
  def hasAlphaChannel(*a,**k): pass
  def isNull(*a,**k): pass
  def isQBitmap(*a,**k): pass
  def load(*a,**k): pass
  def loadFromData(*a,**k): pass
  def mask(*a,**k): pass
  def rect(*a,**k): pass
  def save(*a,**k): pass
  def scaled(*a,**k): pass
  def scaledToHeight(*a,**k): pass
  def scaledToWidth(*a,**k): pass
  def scroll(*a,**k): pass
  def serialNumber(*a,**k): pass
  def setAlphaChannel(*a,**k): pass
  def setMask(*a,**k): pass
  def size(*a,**k): pass
  def swap(*a,**k): pass
  def toImage(*a,**k): pass
  def transformed(*a,**k): pass
  def trueMatrix(*a,**k): pass
  def x11Info(*a,**k): pass
  def x11PictureHandle(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QBitmap(QPixmap):
  pass

  def clear(*a,**k): pass
  def fromData(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QImage(QPaintDevice):
  pass
  Format_ARGB32 = 5
  Format_ARGB32_Premultiplied = 6
  Format_ARGB4444_Premultiplied = 15
  Format_ARGB6666_Premultiplied = 10
  Format_ARGB8555_Premultiplied = 12
  Format_ARGB8565_Premultiplied = 8
  Format_Indexed8 = 3
  Format_Invalid = 0
  Format_Mono = 1
  Format_MonoLSB = 2
  Format_RGB16 = 7
  Format_RGB32 = 4
  Format_RGB444 = 14
  Format_RGB555 = 11
  Format_RGB666 = 9
  Format_RGB888 = 13
  InvertRgb = 0
  InvertRgba = 1
  def allGray(*a,**k): pass
  def alphaChannel(*a,**k): pass
  def bitPlaneCount(*a,**k): pass
  def bits(*a,**k): pass
  def byteCount(*a,**k): pass
  def bytesPerLine(*a,**k): pass
  def cacheKey(*a,**k): pass
  def color(*a,**k): pass
  def colorTable(*a,**k): pass
  def constBits(*a,**k): pass
  def constScanLine(*a,**k): pass
  def convertToFormat(*a,**k): pass
  def copy(*a,**k): pass
  def createAlphaMask(*a,**k): pass
  def createHeuristicMask(*a,**k): pass
  def createMaskFromColor(*a,**k): pass
  def detach(*a,**k): pass
  def devType(*a,**k): pass
  def dotsPerMeterX(*a,**k): pass
  def dotsPerMeterY(*a,**k): pass
  def fill(*a,**k): pass
  def format(*a,**k): pass
  def fromData(*a,**k): pass
  def hasAlphaChannel(*a,**k): pass
  def invertPixels(*a,**k): pass
  def isDetached(*a,**k): pass
  def isGrayscale(*a,**k): pass
  def isNull(*a,**k): pass
  def load(*a,**k): pass
  def loadFromData(*a,**k): pass
  def mirrored(*a,**k): pass
  def numBytes(*a,**k): pass
  def offset(*a,**k): pass
  def pixel(*a,**k): pass
  def pixelIndex(*a,**k): pass
  def rect(*a,**k): pass
  def rgbSwapped(*a,**k): pass
  def save(*a,**k): pass
  def scaled(*a,**k): pass
  def scaledToHeight(*a,**k): pass
  def scaledToWidth(*a,**k): pass
  def scanLine(*a,**k): pass
  def serialNumber(*a,**k): pass
  def setAlphaChannel(*a,**k): pass
  def setColor(*a,**k): pass
  def setColorCount(*a,**k): pass
  def setColorTable(*a,**k): pass
  def setDotsPerMeterX(*a,**k): pass
  def setDotsPerMeterY(*a,**k): pass
  def setNumColors(*a,**k): pass
  def setOffset(*a,**k): pass
  def setPixel(*a,**k): pass
  def setText(*a,**k): pass
  def size(*a,**k): pass
  def swap(*a,**k): pass
  def text(*a,**k): pass
  def textKeys(*a,**k): pass
  def transformed(*a,**k): pass
  def trueMatrix(*a,**k): pass
  def valid(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPrinter(QPaintDevice):
  pass
  A0 = 5
  A1 = 6
  A2 = 7
  A3 = 8
  A4 = 0
  A5 = 9
  A6 = 10
  A7 = 11
  A8 = 12
  A9 = 13
  Aborted = 2
  Active = 1
  AllPages = 0
  Auto = 6
  B0 = 14
  B1 = 15
  B10 = 16
  B2 = 17
  B3 = 18
  B4 = 19
  B5 = 1
  B6 = 20
  B7 = 21
  B8 = 22
  B9 = 23
  C5E = 24
  Cassette = 11
  Cicero = 5
  Color = 1
  Comm10E = 25
  CurrentPage = 3
  Custom = 30
  DLE = 26
  DevicePixel = 6
  Didot = 4
  DuplexAuto = 1
  DuplexLongSide = 2
  DuplexNone = 0
  DuplexShortSide = 3
  Envelope = 4
  EnvelopeManual = 5
  Error = 3
  Executive = 4
  FirstPageFirst = 0
  Folio = 27
  FormSource = 12
  GrayScale = 0
  HighResolution = 2
  Idle = 0
  Inch = 2
  Landscape = 1
  LargeCapacity = 10
  LargeFormat = 9
  LastPageFirst = 1
  Ledger = 28
  Legal = 3
  Letter = 2
  Lower = 1
  Manual = 3
  MaxPageSource = 13
  Middle = 2
  Millimeter = 0
  NativeFormat = 0
  OnlyOne = 0
  PageRange = 2
  PdfFormat = 1
  Pica = 3
  Point = 1
  Portrait = 0
  PostScriptFormat = 2
  PrinterResolution = 1
  ScreenResolution = 0
  Selection = 1
  SmallFormat = 8
  Tabloid = 29
  Tractor = 7
  def abort(*a,**k): pass
  def actualNumCopies(*a,**k): pass
  def collateCopies(*a,**k): pass
  def colorMode(*a,**k): pass
  def copyCount(*a,**k): pass
  def creator(*a,**k): pass
  def docName(*a,**k): pass
  def doubleSidedPrinting(*a,**k): pass
  def duplex(*a,**k): pass
  def fontEmbeddingEnabled(*a,**k): pass
  def fromPage(*a,**k): pass
  def fullPage(*a,**k): pass
  def getPageMargins(*a,**k): pass
  def isValid(*a,**k): pass
  def newPage(*a,**k): pass
  def numCopies(*a,**k): pass
  def orientation(*a,**k): pass
  def outputFileName(*a,**k): pass
  def outputFormat(*a,**k): pass
  def pageOrder(*a,**k): pass
  def pageRect(*a,**k): pass
  def pageSize(*a,**k): pass
  def paperRect(*a,**k): pass
  def paperSize(*a,**k): pass
  def paperSource(*a,**k): pass
  def printEngine(*a,**k): pass
  def printProgram(*a,**k): pass
  def printRange(*a,**k): pass
  def printerName(*a,**k): pass
  def printerSelectionOption(*a,**k): pass
  def printerState(*a,**k): pass
  def resolution(*a,**k): pass
  def setCollateCopies(*a,**k): pass
  def setColorMode(*a,**k): pass
  def setCopyCount(*a,**k): pass
  def setCreator(*a,**k): pass
  def setDocName(*a,**k): pass
  def setDoubleSidedPrinting(*a,**k): pass
  def setDuplex(*a,**k): pass
  def setEngines(*a,**k): pass
  def setFontEmbeddingEnabled(*a,**k): pass
  def setFromTo(*a,**k): pass
  def setFullPage(*a,**k): pass
  def setNumCopies(*a,**k): pass
  def setOrientation(*a,**k): pass
  def setOutputFileName(*a,**k): pass
  def setOutputFormat(*a,**k): pass
  def setPageMargins(*a,**k): pass
  def setPageOrder(*a,**k): pass
  def setPageSize(*a,**k): pass
  def setPaperSize(*a,**k): pass
  def setPaperSource(*a,**k): pass
  def setPrintProgram(*a,**k): pass
  def setPrintRange(*a,**k): pass
  def setPrinterName(*a,**k): pass
  def setPrinterSelectionOption(*a,**k): pass
  def setResolution(*a,**k): pass
  def supportedResolutions(*a,**k): pass
  def supportsMultipleCopies(*a,**k): pass
  def toPage(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPicture(QPaintDevice):
  pass

  def boundingRect(*a,**k): pass
  def data(*a,**k): pass
  def detach(*a,**k): pass
  def devType(*a,**k): pass
  def inputFormatList(*a,**k): pass
  def inputFormats(*a,**k): pass
  def isDetached(*a,**k): pass
  def isNull(*a,**k): pass
  def load(*a,**k): pass
  def outputFormatList(*a,**k): pass
  def outputFormats(*a,**k): pass
  def pictureFormat(*a,**k): pass
  def play(*a,**k): pass
  def save(*a,**k): pass
  def setBoundingRect(*a,**k): pass
  def setData(*a,**k): pass
  def size(*a,**k): pass
  def swap(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QWidget(PyQt4.QtCore.QObject):
  pass
  DrawChildren = 2
  DrawWindowBackground = 1
  IgnoreMask = 4
  PdmDepth = 6
  PdmDpiX = 7
  PdmDpiY = 8
  PdmHeight = 2
  PdmHeightMM = 4
  PdmNumColors = 5
  PdmPhysicalDpiX = 9
  PdmPhysicalDpiY = 10
  PdmWidth = 1
  PdmWidthMM = 3
  def acceptDrops(*a,**k): pass
  def accessibleDescription(*a,**k): pass
  def accessibleName(*a,**k): pass
  def actionEvent(*a,**k): pass
  def actions(*a,**k): pass
  def activateWindow(*a,**k): pass
  def addAction(*a,**k): pass
  def addActions(*a,**k): pass
  def adjustSize(*a,**k): pass
  def autoFillBackground(*a,**k): pass
  def backgroundRole(*a,**k): pass
  def baseSize(*a,**k): pass
  def changeEvent(*a,**k): pass
  def childAt(*a,**k): pass
  def childrenRect(*a,**k): pass
  def childrenRegion(*a,**k): pass
  def clearFocus(*a,**k): pass
  def clearMask(*a,**k): pass
  def close(*a,**k): pass
  def closeEvent(*a,**k): pass
  def colorCount(*a,**k): pass
  def contentsMargins(*a,**k): pass
  def contentsRect(*a,**k): pass
  def contextMenuEvent(*a,**k): pass
  def contextMenuPolicy(*a,**k): pass
  def create(*a,**k): pass
  def cursor(*a,**k): pass
  def customContextMenuRequested(*a,**k): pass
  def depth(*a,**k): pass
  def destroy(*a,**k): pass
  def devType(*a,**k): pass
  def dragEnterEvent(*a,**k): pass
  def dragLeaveEvent(*a,**k): pass
  def dragMoveEvent(*a,**k): pass
  def dropEvent(*a,**k): pass
  def effectiveWinId(*a,**k): pass
  def enabledChange(*a,**k): pass
  def ensurePolished(*a,**k): pass
  def enterEvent(*a,**k): pass
  def find(*a,**k): pass
  def focusInEvent(*a,**k): pass
  def focusNextChild(*a,**k): pass
  def focusNextPrevChild(*a,**k): pass
  def focusOutEvent(*a,**k): pass
  def focusPolicy(*a,**k): pass
  def focusPreviousChild(*a,**k): pass
  def focusProxy(*a,**k): pass
  def focusWidget(*a,**k): pass
  def font(*a,**k): pass
  def fontChange(*a,**k): pass
  def fontInfo(*a,**k): pass
  def fontMetrics(*a,**k): pass
  def foregroundRole(*a,**k): pass
  def frameGeometry(*a,**k): pass
  def frameSize(*a,**k): pass
  def geometry(*a,**k): pass
  def getContentsMargins(*a,**k): pass
  def grabGesture(*a,**k): pass
  def grabKeyboard(*a,**k): pass
  def grabMouse(*a,**k): pass
  def grabShortcut(*a,**k): pass
  def graphicsEffect(*a,**k): pass
  def graphicsProxyWidget(*a,**k): pass
  def handle(*a,**k): pass
  def hasFocus(*a,**k): pass
  def hasMouseTracking(*a,**k): pass
  def height(*a,**k): pass
  def heightForWidth(*a,**k): pass
  def heightMM(*a,**k): pass
  def hide(*a,**k): pass
  def hideEvent(*a,**k): pass
  def inputContext(*a,**k): pass
  def inputMethodEvent(*a,**k): pass
  def inputMethodHints(*a,**k): pass
  def inputMethodQuery(*a,**k): pass
  def insertAction(*a,**k): pass
  def insertActions(*a,**k): pass
  def isActiveWindow(*a,**k): pass
  def isAncestorOf(*a,**k): pass
  def isEnabled(*a,**k): pass
  def isEnabledTo(*a,**k): pass
  def isEnabledToTLW(*a,**k): pass
  def isFullScreen(*a,**k): pass
  def isHidden(*a,**k): pass
  def isLeftToRight(*a,**k): pass
  def isMaximized(*a,**k): pass
  def isMinimized(*a,**k): pass
  def isModal(*a,**k): pass
  def isRightToLeft(*a,**k): pass
  def isTopLevel(*a,**k): pass
  def isVisible(*a,**k): pass
  def isVisibleTo(*a,**k): pass
  def isWindow(*a,**k): pass
  def isWindowModified(*a,**k): pass
  def keyPressEvent(*a,**k): pass
  def keyReleaseEvent(*a,**k): pass
  def keyboardGrabber(*a,**k): pass
  def languageChange(*a,**k): pass
  def layout(*a,**k): pass
  def layoutDirection(*a,**k): pass
  def leaveEvent(*a,**k): pass
  def locale(*a,**k): pass
  def logicalDpiX(*a,**k): pass
  def logicalDpiY(*a,**k): pass
  def lower(*a,**k): pass
  def mapFrom(*a,**k): pass
  def mapFromGlobal(*a,**k): pass
  def mapFromParent(*a,**k): pass
  def mapTo(*a,**k): pass
  def mapToGlobal(*a,**k): pass
  def mapToParent(*a,**k): pass
  def mask(*a,**k): pass
  def maximumHeight(*a,**k): pass
  def maximumSize(*a,**k): pass
  def maximumWidth(*a,**k): pass
  def metric(*a,**k): pass
  def minimumHeight(*a,**k): pass
  def minimumSize(*a,**k): pass
  def minimumSizeHint(*a,**k): pass
  def minimumWidth(*a,**k): pass
  def mouseDoubleClickEvent(*a,**k): pass
  def mouseGrabber(*a,**k): pass
  def mouseMoveEvent(*a,**k): pass
  def mousePressEvent(*a,**k): pass
  def mouseReleaseEvent(*a,**k): pass
  def move(*a,**k): pass
  def moveEvent(*a,**k): pass
  def nativeParentWidget(*a,**k): pass
  def nextInFocusChain(*a,**k): pass
  def normalGeometry(*a,**k): pass
  def numColors(*a,**k): pass
  def overrideWindowFlags(*a,**k): pass
  def overrideWindowState(*a,**k): pass
  def paintEngine(*a,**k): pass
  def paintEvent(*a,**k): pass
  def paintingActive(*a,**k): pass
  def palette(*a,**k): pass
  def paletteChange(*a,**k): pass
  def parentWidget(*a,**k): pass
  def physicalDpiX(*a,**k): pass
  def physicalDpiY(*a,**k): pass
  def pos(*a,**k): pass
  def previousInFocusChain(*a,**k): pass
  def raise_(*a,**k): pass
  def rect(*a,**k): pass
  def releaseKeyboard(*a,**k): pass
  def releaseMouse(*a,**k): pass
  def releaseShortcut(*a,**k): pass
  def removeAction(*a,**k): pass
  def render(*a,**k): pass
  def repaint(*a,**k): pass
  def resetInputContext(*a,**k): pass
  def resize(*a,**k): pass
  def resizeEvent(*a,**k): pass
  def restoreGeometry(*a,**k): pass
  def saveGeometry(*a,**k): pass
  def scroll(*a,**k): pass
  def setAcceptDrops(*a,**k): pass
  def setAccessibleDescription(*a,**k): pass
  def setAccessibleName(*a,**k): pass
  def setAttribute(*a,**k): pass
  def setAutoFillBackground(*a,**k): pass
  def setBackgroundRole(*a,**k): pass
  def setBaseSize(*a,**k): pass
  def setContentsMargins(*a,**k): pass
  def setContextMenuPolicy(*a,**k): pass
  def setCursor(*a,**k): pass
  def setDisabled(*a,**k): pass
  def setEnabled(*a,**k): pass
  def setFixedHeight(*a,**k): pass
  def setFixedSize(*a,**k): pass
  def setFixedWidth(*a,**k): pass
  def setFocus(*a,**k): pass
  def setFocusPolicy(*a,**k): pass
  def setFocusProxy(*a,**k): pass
  def setFont(*a,**k): pass
  def setForegroundRole(*a,**k): pass
  def setGeometry(*a,**k): pass
  def setGraphicsEffect(*a,**k): pass
  def setHidden(*a,**k): pass
  def setInputContext(*a,**k): pass
  def setInputMethodHints(*a,**k): pass
  def setLayout(*a,**k): pass
  def setLayoutDirection(*a,**k): pass
  def setLocale(*a,**k): pass
  def setMask(*a,**k): pass
  def setMaximumHeight(*a,**k): pass
  def setMaximumSize(*a,**k): pass
  def setMaximumWidth(*a,**k): pass
  def setMinimumHeight(*a,**k): pass
  def setMinimumSize(*a,**k): pass
  def setMinimumWidth(*a,**k): pass
  def setMouseTracking(*a,**k): pass
  def setPalette(*a,**k): pass
  def setShortcutAutoRepeat(*a,**k): pass
  def setShortcutEnabled(*a,**k): pass
  def setShown(*a,**k): pass
  def setSizeIncrement(*a,**k): pass
  def setSizePolicy(*a,**k): pass
  def setStatusTip(*a,**k): pass
  def setStyle(*a,**k): pass
  def setStyleSheet(*a,**k): pass
  def setTabOrder(*a,**k): pass
  def setToolTip(*a,**k): pass
  def setUpdatesEnabled(*a,**k): pass
  def setVisible(*a,**k): pass
  def setWhatsThis(*a,**k): pass
  def setWindowFilePath(*a,**k): pass
  def setWindowFlags(*a,**k): pass
  def setWindowIcon(*a,**k): pass
  def setWindowIconText(*a,**k): pass
  def setWindowModality(*a,**k): pass
  def setWindowModified(*a,**k): pass
  def setWindowOpacity(*a,**k): pass
  def setWindowRole(*a,**k): pass
  def setWindowState(*a,**k): pass
  def setWindowTitle(*a,**k): pass
  def show(*a,**k): pass
  def showEvent(*a,**k): pass
  def showFullScreen(*a,**k): pass
  def showMaximized(*a,**k): pass
  def showMinimized(*a,**k): pass
  def showNormal(*a,**k): pass
  def size(*a,**k): pass
  def sizeHint(*a,**k): pass
  def sizeIncrement(*a,**k): pass
  def sizePolicy(*a,**k): pass
  def stackUnder(*a,**k): pass
  def statusTip(*a,**k): pass
  def style(*a,**k): pass
  def styleSheet(*a,**k): pass
  def tabletEvent(*a,**k): pass
  def testAttribute(*a,**k): pass
  def toolTip(*a,**k): pass
  def topLevelWidget(*a,**k): pass
  def underMouse(*a,**k): pass
  def ungrabGesture(*a,**k): pass
  def unsetCursor(*a,**k): pass
  def unsetLayoutDirection(*a,**k): pass
  def unsetLocale(*a,**k): pass
  def update(*a,**k): pass
  def updateGeometry(*a,**k): pass
  def updateMicroFocus(*a,**k): pass
  def updatesEnabled(*a,**k): pass
  def visibleRegion(*a,**k): pass
  def whatsThis(*a,**k): pass
  def wheelEvent(*a,**k): pass
  def width(*a,**k): pass
  def widthMM(*a,**k): pass
  def winId(*a,**k): pass
  def window(*a,**k): pass
  def windowActivationChange(*a,**k): pass
  def windowFilePath(*a,**k): pass
  def windowFlags(*a,**k): pass
  def windowIcon(*a,**k): pass
  def windowIconText(*a,**k): pass
  def windowModality(*a,**k): pass
  def windowOpacity(*a,**k): pass
  def windowRole(*a,**k): pass
  def windowState(*a,**k): pass
  def windowTitle(*a,**k): pass
  def windowType(*a,**k): pass
  def x(*a,**k): pass
  def x11Info(*a,**k): pass
  def x11PictureHandle(*a,**k): pass
  def y(*a,**k): pass

class QAbstractButton(QWidget):
  pass

  def animateClick(*a,**k): pass
  def autoExclusive(*a,**k): pass
  def autoRepeat(*a,**k): pass
  def autoRepeatDelay(*a,**k): pass
  def autoRepeatInterval(*a,**k): pass
  def checkStateSet(*a,**k): pass
  def click(*a,**k): pass
  def clicked(*a,**k): pass
  def group(*a,**k): pass
  def hitButton(*a,**k): pass
  def icon(*a,**k): pass
  def iconSize(*a,**k): pass
  def isCheckable(*a,**k): pass
  def isChecked(*a,**k): pass
  def isDown(*a,**k): pass
  def nextCheckState(*a,**k): pass
  def pressed(*a,**k): pass
  def released(*a,**k): pass
  def setAutoExclusive(*a,**k): pass
  def setAutoRepeat(*a,**k): pass
  def setAutoRepeatDelay(*a,**k): pass
  def setAutoRepeatInterval(*a,**k): pass
  def setCheckable(*a,**k): pass
  def setChecked(*a,**k): pass
  def setDown(*a,**k): pass
  def setIcon(*a,**k): pass
  def setIconSize(*a,**k): pass
  def setShortcut(*a,**k): pass
  def setText(*a,**k): pass
  def shortcut(*a,**k): pass
  def text(*a,**k): pass
  def toggle(*a,**k): pass
  def toggled(*a,**k): pass

class QCheckBox(QAbstractButton):
  pass

  def checkState(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def isTristate(*a,**k): pass
  def setCheckState(*a,**k): pass
  def setTristate(*a,**k): pass
  def stateChanged(*a,**k): pass

class QPushButton(QAbstractButton):
  pass

  def autoDefault(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def isDefault(*a,**k): pass
  def isFlat(*a,**k): pass
  def menu(*a,**k): pass
  def setAutoDefault(*a,**k): pass
  def setDefault(*a,**k): pass
  def setFlat(*a,**k): pass
  def setMenu(*a,**k): pass
  def showMenu(*a,**k): pass

class QCommandLinkButton(QPushButton):
  pass

  def description(*a,**k): pass
  def setDescription(*a,**k): pass

class QToolButton(QAbstractButton):
  pass
  DelayedPopup = 0
  InstantPopup = 2
  MenuButtonPopup = 1
  def arrowType(*a,**k): pass
  def autoRaise(*a,**k): pass
  def defaultAction(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def menu(*a,**k): pass
  def popupMode(*a,**k): pass
  def setArrowType(*a,**k): pass
  def setAutoRaise(*a,**k): pass
  def setDefaultAction(*a,**k): pass
  def setMenu(*a,**k): pass
  def setPopupMode(*a,**k): pass
  def setToolButtonStyle(*a,**k): pass
  def showMenu(*a,**k): pass
  def toolButtonStyle(*a,**k): pass
  def triggered(*a,**k): pass

class QRadioButton(QAbstractButton):
  pass

  def initStyleOption(*a,**k): pass

class QFrame(QWidget):
  pass
  Box = 1
  HLine = 4
  NoFrame = 0
  Panel = 2
  Plain = 16
  Raised = 32
  Shadow_Mask = 240
  Shape_Mask = 15
  StyledPanel = 6
  Sunken = 48
  VLine = 5
  WinPanel = 3
  def drawFrame(*a,**k): pass
  def frameRect(*a,**k): pass
  def frameShadow(*a,**k): pass
  def frameShape(*a,**k): pass
  def frameStyle(*a,**k): pass
  def frameWidth(*a,**k): pass
  def lineWidth(*a,**k): pass
  def midLineWidth(*a,**k): pass
  def setFrameRect(*a,**k): pass
  def setFrameShadow(*a,**k): pass
  def setFrameShape(*a,**k): pass
  def setFrameStyle(*a,**k): pass
  def setLineWidth(*a,**k): pass
  def setMidLineWidth(*a,**k): pass

class QAbstractScrollArea(QFrame):
  pass

  def addScrollBarWidget(*a,**k): pass
  def cornerWidget(*a,**k): pass
  def horizontalScrollBar(*a,**k): pass
  def horizontalScrollBarPolicy(*a,**k): pass
  def maximumViewportSize(*a,**k): pass
  def scrollBarWidgets(*a,**k): pass
  def scrollContentsBy(*a,**k): pass
  def setCornerWidget(*a,**k): pass
  def setHorizontalScrollBar(*a,**k): pass
  def setHorizontalScrollBarPolicy(*a,**k): pass
  def setVerticalScrollBar(*a,**k): pass
  def setVerticalScrollBarPolicy(*a,**k): pass
  def setViewport(*a,**k): pass
  def setViewportMargins(*a,**k): pass
  def setupViewport(*a,**k): pass
  def verticalScrollBar(*a,**k): pass
  def verticalScrollBarPolicy(*a,**k): pass
  def viewport(*a,**k): pass
  def viewportEvent(*a,**k): pass

class QAbstractItemView(QAbstractScrollArea):
  pass
  AboveItem = 1
  AllEditTriggers = 31
  AnimatingState = 6
  AnyKeyPressed = 16
  BelowItem = 2
  CollapsingState = 5
  ContiguousSelection = 4
  CurrentChanged = 1
  DoubleClicked = 2
  DragDrop = 3
  DragOnly = 1
  DragSelectingState = 2
  DraggingState = 1
  DropOnly = 2
  EditKeyPressed = 8
  EditingState = 3
  EnsureVisible = 0
  ExpandingState = 4
  ExtendedSelection = 3
  InternalMove = 4
  MoveDown = 1
  MoveEnd = 5
  MoveHome = 4
  MoveLeft = 2
  MoveNext = 8
  MovePageDown = 7
  MovePageUp = 6
  MovePrevious = 9
  MoveRight = 3
  MoveUp = 0
  MultiSelection = 2
  NoDragDrop = 0
  NoEditTriggers = 0
  NoSelection = 0
  NoState = 0
  OnItem = 0
  OnViewport = 3
  PositionAtBottom = 2
  PositionAtCenter = 3
  PositionAtTop = 1
  ScrollPerItem = 0
  ScrollPerPixel = 1
  SelectColumns = 2
  SelectItems = 0
  SelectRows = 1
  SelectedClicked = 4
  SingleSelection = 1
  def activated(*a,**k): pass
  def alternatingRowColors(*a,**k): pass
  def autoScrollMargin(*a,**k): pass
  def clearSelection(*a,**k): pass
  def clicked(*a,**k): pass
  def closeEditor(*a,**k): pass
  def closePersistentEditor(*a,**k): pass
  def commitData(*a,**k): pass
  def currentChanged(*a,**k): pass
  def currentIndex(*a,**k): pass
  def dataChanged(*a,**k): pass
  def defaultDropAction(*a,**k): pass
  def dirtyRegionOffset(*a,**k): pass
  def doubleClicked(*a,**k): pass
  def dragDropMode(*a,**k): pass
  def dragDropOverwriteMode(*a,**k): pass
  def dragEnabled(*a,**k): pass
  def dropIndicatorPosition(*a,**k): pass
  def edit(*a,**k): pass
  def editTriggers(*a,**k): pass
  def editorDestroyed(*a,**k): pass
  def entered(*a,**k): pass
  def executeDelayedItemsLayout(*a,**k): pass
  def hasAutoScroll(*a,**k): pass
  def horizontalOffset(*a,**k): pass
  def horizontalScrollMode(*a,**k): pass
  def horizontalScrollbarAction(*a,**k): pass
  def horizontalScrollbarValueChanged(*a,**k): pass
  def horizontalStepsPerItem(*a,**k): pass
  def iconSize(*a,**k): pass
  def indexAt(*a,**k): pass
  def indexWidget(*a,**k): pass
  def isIndexHidden(*a,**k): pass
  def itemDelegate(*a,**k): pass
  def itemDelegateForColumn(*a,**k): pass
  def itemDelegateForRow(*a,**k): pass
  def keyboardSearch(*a,**k): pass
  def model(*a,**k): pass
  def moveCursor(*a,**k): pass
  def openPersistentEditor(*a,**k): pass
  def pressed(*a,**k): pass
  def reset(*a,**k): pass
  def rootIndex(*a,**k): pass
  def rowsAboutToBeRemoved(*a,**k): pass
  def rowsInserted(*a,**k): pass
  def scheduleDelayedItemsLayout(*a,**k): pass
  def scrollDirtyRegion(*a,**k): pass
  def scrollTo(*a,**k): pass
  def scrollToBottom(*a,**k): pass
  def scrollToTop(*a,**k): pass
  def selectAll(*a,**k): pass
  def selectedIndexes(*a,**k): pass
  def selectionBehavior(*a,**k): pass
  def selectionChanged(*a,**k): pass
  def selectionCommand(*a,**k): pass
  def selectionMode(*a,**k): pass
  def selectionModel(*a,**k): pass
  def setAlternatingRowColors(*a,**k): pass
  def setAutoScroll(*a,**k): pass
  def setAutoScrollMargin(*a,**k): pass
  def setCurrentIndex(*a,**k): pass
  def setDefaultDropAction(*a,**k): pass
  def setDirtyRegion(*a,**k): pass
  def setDragDropMode(*a,**k): pass
  def setDragDropOverwriteMode(*a,**k): pass
  def setDragEnabled(*a,**k): pass
  def setDropIndicatorShown(*a,**k): pass
  def setEditTriggers(*a,**k): pass
  def setHorizontalScrollMode(*a,**k): pass
  def setHorizontalStepsPerItem(*a,**k): pass
  def setIconSize(*a,**k): pass
  def setIndexWidget(*a,**k): pass
  def setItemDelegate(*a,**k): pass
  def setItemDelegateForColumn(*a,**k): pass
  def setItemDelegateForRow(*a,**k): pass
  def setModel(*a,**k): pass
  def setRootIndex(*a,**k): pass
  def setSelection(*a,**k): pass
  def setSelectionBehavior(*a,**k): pass
  def setSelectionMode(*a,**k): pass
  def setSelectionModel(*a,**k): pass
  def setState(*a,**k): pass
  def setTabKeyNavigation(*a,**k): pass
  def setTextElideMode(*a,**k): pass
  def setVerticalScrollMode(*a,**k): pass
  def setVerticalStepsPerItem(*a,**k): pass
  def showDropIndicator(*a,**k): pass
  def sizeHintForColumn(*a,**k): pass
  def sizeHintForIndex(*a,**k): pass
  def sizeHintForRow(*a,**k): pass
  def startDrag(*a,**k): pass
  def state(*a,**k): pass
  def tabKeyNavigation(*a,**k): pass
  def textElideMode(*a,**k): pass
  def updateEditorData(*a,**k): pass
  def updateEditorGeometries(*a,**k): pass
  def updateGeometries(*a,**k): pass
  def verticalOffset(*a,**k): pass
  def verticalScrollMode(*a,**k): pass
  def verticalScrollbarAction(*a,**k): pass
  def verticalScrollbarValueChanged(*a,**k): pass
  def verticalStepsPerItem(*a,**k): pass
  def viewOptions(*a,**k): pass
  def viewportEntered(*a,**k): pass
  def visualRect(*a,**k): pass
  def visualRegionForSelection(*a,**k): pass

class QColumnView(QAbstractItemView):
  pass

  def columnWidths(*a,**k): pass
  def createColumn(*a,**k): pass
  def initializeColumn(*a,**k): pass
  def previewWidget(*a,**k): pass
  def resizeGripsVisible(*a,**k): pass
  def setColumnWidths(*a,**k): pass
  def setPreviewWidget(*a,**k): pass
  def setResizeGripsVisible(*a,**k): pass
  def updatePreviewWidget(*a,**k): pass

class QHeaderView(QAbstractItemView):
  pass
  Custom = 2
  Fixed = 2
  Interactive = 0
  ResizeToContents = 3
  Stretch = 1
  def cascadingSectionResizes(*a,**k): pass
  def count(*a,**k): pass
  def defaultAlignment(*a,**k): pass
  def defaultSectionSize(*a,**k): pass
  def geometriesChanged(*a,**k): pass
  def headerDataChanged(*a,**k): pass
  def hiddenSectionCount(*a,**k): pass
  def hideSection(*a,**k): pass
  def highlightSections(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def initialize(*a,**k): pass
  def initializeSections(*a,**k): pass
  def isClickable(*a,**k): pass
  def isMovable(*a,**k): pass
  def isSectionHidden(*a,**k): pass
  def isSortIndicatorShown(*a,**k): pass
  def length(*a,**k): pass
  def logicalIndex(*a,**k): pass
  def logicalIndexAt(*a,**k): pass
  def minimumSectionSize(*a,**k): pass
  def moveSection(*a,**k): pass
  def offset(*a,**k): pass
  def orientation(*a,**k): pass
  def paintSection(*a,**k): pass
  def resizeMode(*a,**k): pass
  def resizeSection(*a,**k): pass
  def resizeSections(*a,**k): pass
  def restoreState(*a,**k): pass
  def saveState(*a,**k): pass
  def sectionAutoResize(*a,**k): pass
  def sectionClicked(*a,**k): pass
  def sectionCountChanged(*a,**k): pass
  def sectionDoubleClicked(*a,**k): pass
  def sectionEntered(*a,**k): pass
  def sectionHandleDoubleClicked(*a,**k): pass
  def sectionMoved(*a,**k): pass
  def sectionPosition(*a,**k): pass
  def sectionPressed(*a,**k): pass
  def sectionResized(*a,**k): pass
  def sectionSize(*a,**k): pass
  def sectionSizeFromContents(*a,**k): pass
  def sectionSizeHint(*a,**k): pass
  def sectionViewportPosition(*a,**k): pass
  def sectionsAboutToBeRemoved(*a,**k): pass
  def sectionsHidden(*a,**k): pass
  def sectionsInserted(*a,**k): pass
  def sectionsMoved(*a,**k): pass
  def setCascadingSectionResizes(*a,**k): pass
  def setClickable(*a,**k): pass
  def setDefaultAlignment(*a,**k): pass
  def setDefaultSectionSize(*a,**k): pass
  def setHighlightSections(*a,**k): pass
  def setMinimumSectionSize(*a,**k): pass
  def setMovable(*a,**k): pass
  def setOffset(*a,**k): pass
  def setOffsetToLastSection(*a,**k): pass
  def setOffsetToSectionPosition(*a,**k): pass
  def setResizeMode(*a,**k): pass
  def setSectionHidden(*a,**k): pass
  def setSortIndicator(*a,**k): pass
  def setSortIndicatorShown(*a,**k): pass
  def setStretchLastSection(*a,**k): pass
  def showSection(*a,**k): pass
  def sortIndicatorChanged(*a,**k): pass
  def sortIndicatorOrder(*a,**k): pass
  def sortIndicatorSection(*a,**k): pass
  def stretchLastSection(*a,**k): pass
  def stretchSectionCount(*a,**k): pass
  def swapSections(*a,**k): pass
  def updateSection(*a,**k): pass
  def visualIndex(*a,**k): pass
  def visualIndexAt(*a,**k): pass

class QListView(QAbstractItemView):
  pass
  Adjust = 1
  Batched = 1
  Fixed = 0
  Free = 1
  IconMode = 1
  LeftToRight = 0
  ListMode = 0
  SinglePass = 0
  Snap = 2
  Static = 0
  TopToBottom = 1
  def batchSize(*a,**k): pass
  def clearPropertyFlags(*a,**k): pass
  def flow(*a,**k): pass
  def gridSize(*a,**k): pass
  def indexesMoved(*a,**k): pass
  def isRowHidden(*a,**k): pass
  def isSelectionRectVisible(*a,**k): pass
  def isWrapping(*a,**k): pass
  def layoutMode(*a,**k): pass
  def modelColumn(*a,**k): pass
  def movement(*a,**k): pass
  def rectForIndex(*a,**k): pass
  def resizeMode(*a,**k): pass
  def setBatchSize(*a,**k): pass
  def setFlow(*a,**k): pass
  def setGridSize(*a,**k): pass
  def setLayoutMode(*a,**k): pass
  def setModelColumn(*a,**k): pass
  def setMovement(*a,**k): pass
  def setPositionForIndex(*a,**k): pass
  def setResizeMode(*a,**k): pass
  def setRowHidden(*a,**k): pass
  def setSelectionRectVisible(*a,**k): pass
  def setSpacing(*a,**k): pass
  def setUniformItemSizes(*a,**k): pass
  def setViewMode(*a,**k): pass
  def setWordWrap(*a,**k): pass
  def setWrapping(*a,**k): pass
  def spacing(*a,**k): pass
  def uniformItemSizes(*a,**k): pass
  def viewMode(*a,**k): pass
  def wordWrap(*a,**k): pass

class QListWidget(QListView):
  pass

  def addItem(*a,**k): pass
  def addItems(*a,**k): pass
  def clear(*a,**k): pass
  def count(*a,**k): pass
  def currentItem(*a,**k): pass
  def currentItemChanged(*a,**k): pass
  def currentRow(*a,**k): pass
  def currentRowChanged(*a,**k): pass
  def currentTextChanged(*a,**k): pass
  def dropMimeData(*a,**k): pass
  def editItem(*a,**k): pass
  def findItems(*a,**k): pass
  def indexFromItem(*a,**k): pass
  def insertItem(*a,**k): pass
  def insertItems(*a,**k): pass
  def isItemHidden(*a,**k): pass
  def isItemSelected(*a,**k): pass
  def isSortingEnabled(*a,**k): pass
  def item(*a,**k): pass
  def itemActivated(*a,**k): pass
  def itemAt(*a,**k): pass
  def itemChanged(*a,**k): pass
  def itemClicked(*a,**k): pass
  def itemDoubleClicked(*a,**k): pass
  def itemEntered(*a,**k): pass
  def itemFromIndex(*a,**k): pass
  def itemPressed(*a,**k): pass
  def itemSelectionChanged(*a,**k): pass
  def itemWidget(*a,**k): pass
  def items(*a,**k): pass
  def mimeData(*a,**k): pass
  def mimeTypes(*a,**k): pass
  def removeItemWidget(*a,**k): pass
  def row(*a,**k): pass
  def scrollToItem(*a,**k): pass
  def selectedItems(*a,**k): pass
  def setCurrentItem(*a,**k): pass
  def setCurrentRow(*a,**k): pass
  def setItemHidden(*a,**k): pass
  def setItemSelected(*a,**k): pass
  def setItemWidget(*a,**k): pass
  def setSortingEnabled(*a,**k): pass
  def sortItems(*a,**k): pass
  def supportedDropActions(*a,**k): pass
  def takeItem(*a,**k): pass
  def visualItemRect(*a,**k): pass

class QUndoView(QListView):
  pass

  def cleanIcon(*a,**k): pass
  def emptyLabel(*a,**k): pass
  def group(*a,**k): pass
  def setCleanIcon(*a,**k): pass
  def setEmptyLabel(*a,**k): pass
  def setGroup(*a,**k): pass
  def setStack(*a,**k): pass
  def stack(*a,**k): pass

class QTableView(QAbstractItemView):
  pass

  def clearSpans(*a,**k): pass
  def columnAt(*a,**k): pass
  def columnCountChanged(*a,**k): pass
  def columnMoved(*a,**k): pass
  def columnResized(*a,**k): pass
  def columnSpan(*a,**k): pass
  def columnViewportPosition(*a,**k): pass
  def columnWidth(*a,**k): pass
  def gridStyle(*a,**k): pass
  def hideColumn(*a,**k): pass
  def hideRow(*a,**k): pass
  def horizontalHeader(*a,**k): pass
  def isColumnHidden(*a,**k): pass
  def isCornerButtonEnabled(*a,**k): pass
  def isRowHidden(*a,**k): pass
  def isSortingEnabled(*a,**k): pass
  def resizeColumnToContents(*a,**k): pass
  def resizeColumnsToContents(*a,**k): pass
  def resizeRowToContents(*a,**k): pass
  def resizeRowsToContents(*a,**k): pass
  def rowAt(*a,**k): pass
  def rowCountChanged(*a,**k): pass
  def rowHeight(*a,**k): pass
  def rowMoved(*a,**k): pass
  def rowResized(*a,**k): pass
  def rowSpan(*a,**k): pass
  def rowViewportPosition(*a,**k): pass
  def selectColumn(*a,**k): pass
  def selectRow(*a,**k): pass
  def setColumnHidden(*a,**k): pass
  def setColumnWidth(*a,**k): pass
  def setCornerButtonEnabled(*a,**k): pass
  def setGridStyle(*a,**k): pass
  def setHorizontalHeader(*a,**k): pass
  def setRowHeight(*a,**k): pass
  def setRowHidden(*a,**k): pass
  def setShowGrid(*a,**k): pass
  def setSortingEnabled(*a,**k): pass
  def setSpan(*a,**k): pass
  def setVerticalHeader(*a,**k): pass
  def setWordWrap(*a,**k): pass
  def showColumn(*a,**k): pass
  def showGrid(*a,**k): pass
  def showRow(*a,**k): pass
  def sortByColumn(*a,**k): pass
  def verticalHeader(*a,**k): pass
  def wordWrap(*a,**k): pass

class QTableWidget(QTableView):
  pass

  def cellActivated(*a,**k): pass
  def cellChanged(*a,**k): pass
  def cellClicked(*a,**k): pass
  def cellDoubleClicked(*a,**k): pass
  def cellEntered(*a,**k): pass
  def cellPressed(*a,**k): pass
  def cellWidget(*a,**k): pass
  def clear(*a,**k): pass
  def clearContents(*a,**k): pass
  def column(*a,**k): pass
  def columnCount(*a,**k): pass
  def currentCellChanged(*a,**k): pass
  def currentColumn(*a,**k): pass
  def currentItem(*a,**k): pass
  def currentItemChanged(*a,**k): pass
  def currentRow(*a,**k): pass
  def dropMimeData(*a,**k): pass
  def editItem(*a,**k): pass
  def findItems(*a,**k): pass
  def horizontalHeaderItem(*a,**k): pass
  def indexFromItem(*a,**k): pass
  def insertColumn(*a,**k): pass
  def insertRow(*a,**k): pass
  def isItemSelected(*a,**k): pass
  def item(*a,**k): pass
  def itemActivated(*a,**k): pass
  def itemAt(*a,**k): pass
  def itemChanged(*a,**k): pass
  def itemClicked(*a,**k): pass
  def itemDoubleClicked(*a,**k): pass
  def itemEntered(*a,**k): pass
  def itemFromIndex(*a,**k): pass
  def itemPressed(*a,**k): pass
  def itemPrototype(*a,**k): pass
  def itemSelectionChanged(*a,**k): pass
  def items(*a,**k): pass
  def mimeData(*a,**k): pass
  def mimeTypes(*a,**k): pass
  def removeCellWidget(*a,**k): pass
  def removeColumn(*a,**k): pass
  def removeRow(*a,**k): pass
  def row(*a,**k): pass
  def rowCount(*a,**k): pass
  def scrollToItem(*a,**k): pass
  def selectedItems(*a,**k): pass
  def selectedRanges(*a,**k): pass
  def setCellWidget(*a,**k): pass
  def setColumnCount(*a,**k): pass
  def setCurrentCell(*a,**k): pass
  def setCurrentItem(*a,**k): pass
  def setHorizontalHeaderItem(*a,**k): pass
  def setHorizontalHeaderLabels(*a,**k): pass
  def setItem(*a,**k): pass
  def setItemPrototype(*a,**k): pass
  def setItemSelected(*a,**k): pass
  def setRangeSelected(*a,**k): pass
  def setRowCount(*a,**k): pass
  def setVerticalHeaderItem(*a,**k): pass
  def setVerticalHeaderLabels(*a,**k): pass
  def sortItems(*a,**k): pass
  def supportedDropActions(*a,**k): pass
  def takeHorizontalHeaderItem(*a,**k): pass
  def takeItem(*a,**k): pass
  def takeVerticalHeaderItem(*a,**k): pass
  def verticalHeaderItem(*a,**k): pass
  def visualColumn(*a,**k): pass
  def visualItemRect(*a,**k): pass
  def visualRow(*a,**k): pass

class QTreeView(QAbstractItemView):
  pass

  def allColumnsShowFocus(*a,**k): pass
  def autoExpandDelay(*a,**k): pass
  def collapse(*a,**k): pass
  def collapseAll(*a,**k): pass
  def collapsed(*a,**k): pass
  def columnAt(*a,**k): pass
  def columnCountChanged(*a,**k): pass
  def columnMoved(*a,**k): pass
  def columnResized(*a,**k): pass
  def columnViewportPosition(*a,**k): pass
  def columnWidth(*a,**k): pass
  def drawBranches(*a,**k): pass
  def drawRow(*a,**k): pass
  def drawTree(*a,**k): pass
  def expand(*a,**k): pass
  def expandAll(*a,**k): pass
  def expandToDepth(*a,**k): pass
  def expanded(*a,**k): pass
  def expandsOnDoubleClick(*a,**k): pass
  def header(*a,**k): pass
  def hideColumn(*a,**k): pass
  def indentation(*a,**k): pass
  def indexAbove(*a,**k): pass
  def indexBelow(*a,**k): pass
  def indexRowSizeHint(*a,**k): pass
  def isAnimated(*a,**k): pass
  def isColumnHidden(*a,**k): pass
  def isExpanded(*a,**k): pass
  def isFirstColumnSpanned(*a,**k): pass
  def isHeaderHidden(*a,**k): pass
  def isRowHidden(*a,**k): pass
  def isSortingEnabled(*a,**k): pass
  def itemsExpandable(*a,**k): pass
  def reexpand(*a,**k): pass
  def resizeColumnToContents(*a,**k): pass
  def rootIsDecorated(*a,**k): pass
  def rowHeight(*a,**k): pass
  def rowsRemoved(*a,**k): pass
  def setAllColumnsShowFocus(*a,**k): pass
  def setAnimated(*a,**k): pass
  def setAutoExpandDelay(*a,**k): pass
  def setColumnHidden(*a,**k): pass
  def setColumnWidth(*a,**k): pass
  def setExpanded(*a,**k): pass
  def setExpandsOnDoubleClick(*a,**k): pass
  def setFirstColumnSpanned(*a,**k): pass
  def setHeader(*a,**k): pass
  def setHeaderHidden(*a,**k): pass
  def setIndentation(*a,**k): pass
  def setItemsExpandable(*a,**k): pass
  def setRootIsDecorated(*a,**k): pass
  def setRowHidden(*a,**k): pass
  def setSortingEnabled(*a,**k): pass
  def setUniformRowHeights(*a,**k): pass
  def setWordWrap(*a,**k): pass
  def showColumn(*a,**k): pass
  def sortByColumn(*a,**k): pass
  def uniformRowHeights(*a,**k): pass
  def wordWrap(*a,**k): pass

class QTreeWidget(QTreeView):
  pass

  def addTopLevelItem(*a,**k): pass
  def addTopLevelItems(*a,**k): pass
  def clear(*a,**k): pass
  def collapseItem(*a,**k): pass
  def columnCount(*a,**k): pass
  def currentColumn(*a,**k): pass
  def currentItem(*a,**k): pass
  def currentItemChanged(*a,**k): pass
  def dropMimeData(*a,**k): pass
  def editItem(*a,**k): pass
  def expandItem(*a,**k): pass
  def findItems(*a,**k): pass
  def headerItem(*a,**k): pass
  def indexFromItem(*a,**k): pass
  def indexOfTopLevelItem(*a,**k): pass
  def insertTopLevelItem(*a,**k): pass
  def insertTopLevelItems(*a,**k): pass
  def invisibleRootItem(*a,**k): pass
  def isFirstItemColumnSpanned(*a,**k): pass
  def isItemExpanded(*a,**k): pass
  def isItemHidden(*a,**k): pass
  def isItemSelected(*a,**k): pass
  def itemAbove(*a,**k): pass
  def itemActivated(*a,**k): pass
  def itemAt(*a,**k): pass
  def itemBelow(*a,**k): pass
  def itemChanged(*a,**k): pass
  def itemClicked(*a,**k): pass
  def itemCollapsed(*a,**k): pass
  def itemDoubleClicked(*a,**k): pass
  def itemEntered(*a,**k): pass
  def itemExpanded(*a,**k): pass
  def itemFromIndex(*a,**k): pass
  def itemPressed(*a,**k): pass
  def itemSelectionChanged(*a,**k): pass
  def itemWidget(*a,**k): pass
  def items(*a,**k): pass
  def mimeData(*a,**k): pass
  def mimeTypes(*a,**k): pass
  def removeItemWidget(*a,**k): pass
  def scrollToItem(*a,**k): pass
  def selectedItems(*a,**k): pass
  def setColumnCount(*a,**k): pass
  def setCurrentItem(*a,**k): pass
  def setFirstItemColumnSpanned(*a,**k): pass
  def setHeaderItem(*a,**k): pass
  def setHeaderLabel(*a,**k): pass
  def setHeaderLabels(*a,**k): pass
  def setItemExpanded(*a,**k): pass
  def setItemHidden(*a,**k): pass
  def setItemSelected(*a,**k): pass
  def setItemWidget(*a,**k): pass
  def sortColumn(*a,**k): pass
  def sortItems(*a,**k): pass
  def supportedDropActions(*a,**k): pass
  def takeTopLevelItem(*a,**k): pass
  def topLevelItem(*a,**k): pass
  def topLevelItemCount(*a,**k): pass
  def visualItemRect(*a,**k): pass

class QGraphicsView(QAbstractScrollArea):
  pass
  AnchorUnderMouse = 2
  AnchorViewCenter = 1
  BoundingRectViewportUpdate = 4
  CacheBackground = 1
  CacheNone = 0
  DontAdjustForAntialiasing = 4
  DontClipPainter = 1
  DontSavePainterState = 2
  FullViewportUpdate = 0
  MinimalViewportUpdate = 1
  NoAnchor = 0
  NoDrag = 0
  NoViewportUpdate = 3
  RubberBandDrag = 2
  ScrollHandDrag = 1
  SmartViewportUpdate = 2
  def alignment(*a,**k): pass
  def backgroundBrush(*a,**k): pass
  def cacheMode(*a,**k): pass
  def centerOn(*a,**k): pass
  def dragMode(*a,**k): pass
  def drawBackground(*a,**k): pass
  def drawForeground(*a,**k): pass
  def drawItems(*a,**k): pass
  def ensureVisible(*a,**k): pass
  def fitInView(*a,**k): pass
  def foregroundBrush(*a,**k): pass
  def invalidateScene(*a,**k): pass
  def isInteractive(*a,**k): pass
  def isTransformed(*a,**k): pass
  def itemAt(*a,**k): pass
  def items(*a,**k): pass
  def mapFromScene(*a,**k): pass
  def mapToScene(*a,**k): pass
  def matrix(*a,**k): pass
  def optimizationFlags(*a,**k): pass
  def renderHints(*a,**k): pass
  def resetCachedContent(*a,**k): pass
  def resetMatrix(*a,**k): pass
  def resetTransform(*a,**k): pass
  def resizeAnchor(*a,**k): pass
  def rotate(*a,**k): pass
  def rubberBandSelectionMode(*a,**k): pass
  def scale(*a,**k): pass
  def scene(*a,**k): pass
  def sceneRect(*a,**k): pass
  def setAlignment(*a,**k): pass
  def setBackgroundBrush(*a,**k): pass
  def setCacheMode(*a,**k): pass
  def setDragMode(*a,**k): pass
  def setForegroundBrush(*a,**k): pass
  def setInteractive(*a,**k): pass
  def setMatrix(*a,**k): pass
  def setOptimizationFlag(*a,**k): pass
  def setOptimizationFlags(*a,**k): pass
  def setRenderHint(*a,**k): pass
  def setRenderHints(*a,**k): pass
  def setResizeAnchor(*a,**k): pass
  def setRubberBandSelectionMode(*a,**k): pass
  def setScene(*a,**k): pass
  def setSceneRect(*a,**k): pass
  def setTransform(*a,**k): pass
  def setTransformationAnchor(*a,**k): pass
  def setViewportUpdateMode(*a,**k): pass
  def shear(*a,**k): pass
  def transform(*a,**k): pass
  def transformationAnchor(*a,**k): pass
  def translate(*a,**k): pass
  def updateScene(*a,**k): pass
  def updateSceneRect(*a,**k): pass
  def viewportTransform(*a,**k): pass
  def viewportUpdateMode(*a,**k): pass

class QMdiArea(QAbstractScrollArea):
  pass
  ActivationHistoryOrder = 2
  CreationOrder = 0
  DontMaximizeSubWindowOnActivation = 1
  StackingOrder = 1
  SubWindowView = 0
  TabbedView = 1
  def activateNextSubWindow(*a,**k): pass
  def activatePreviousSubWindow(*a,**k): pass
  def activationOrder(*a,**k): pass
  def activeSubWindow(*a,**k): pass
  def addSubWindow(*a,**k): pass
  def background(*a,**k): pass
  def cascadeSubWindows(*a,**k): pass
  def closeActiveSubWindow(*a,**k): pass
  def closeAllSubWindows(*a,**k): pass
  def currentSubWindow(*a,**k): pass
  def documentMode(*a,**k): pass
  def removeSubWindow(*a,**k): pass
  def setActivationOrder(*a,**k): pass
  def setActiveSubWindow(*a,**k): pass
  def setBackground(*a,**k): pass
  def setDocumentMode(*a,**k): pass
  def setOption(*a,**k): pass
  def setTabPosition(*a,**k): pass
  def setTabShape(*a,**k): pass
  def setTabsClosable(*a,**k): pass
  def setTabsMovable(*a,**k): pass
  def setViewMode(*a,**k): pass
  def subWindowActivated(*a,**k): pass
  def subWindowList(*a,**k): pass
  def tabPosition(*a,**k): pass
  def tabShape(*a,**k): pass
  def tabsClosable(*a,**k): pass
  def tabsMovable(*a,**k): pass
  def testOption(*a,**k): pass
  def tileSubWindows(*a,**k): pass
  def viewMode(*a,**k): pass

class QPlainTextEdit(QAbstractScrollArea):
  pass
  NoWrap = 0
  WidgetWidth = 1
  def anchorAt(*a,**k): pass
  def appendHtml(*a,**k): pass
  def appendPlainText(*a,**k): pass
  def backgroundVisible(*a,**k): pass
  def blockBoundingGeometry(*a,**k): pass
  def blockBoundingRect(*a,**k): pass
  def blockCount(*a,**k): pass
  def blockCountChanged(*a,**k): pass
  def canInsertFromMimeData(*a,**k): pass
  def canPaste(*a,**k): pass
  def centerCursor(*a,**k): pass
  def centerOnScroll(*a,**k): pass
  def clear(*a,**k): pass
  def contentOffset(*a,**k): pass
  def copy(*a,**k): pass
  def copyAvailable(*a,**k): pass
  def createMimeDataFromSelection(*a,**k): pass
  def createStandardContextMenu(*a,**k): pass
  def currentCharFormat(*a,**k): pass
  def cursorForPosition(*a,**k): pass
  def cursorPositionChanged(*a,**k): pass
  def cursorRect(*a,**k): pass
  def cursorWidth(*a,**k): pass
  def cut(*a,**k): pass
  def document(*a,**k): pass
  def documentTitle(*a,**k): pass
  def ensureCursorVisible(*a,**k): pass
  def extraSelections(*a,**k): pass
  def firstVisibleBlock(*a,**k): pass
  def getPaintContext(*a,**k): pass
  def insertFromMimeData(*a,**k): pass
  def insertPlainText(*a,**k): pass
  def isReadOnly(*a,**k): pass
  def isUndoRedoEnabled(*a,**k): pass
  def lineWrapMode(*a,**k): pass
  def loadResource(*a,**k): pass
  def maximumBlockCount(*a,**k): pass
  def mergeCurrentCharFormat(*a,**k): pass
  def modificationChanged(*a,**k): pass
  def moveCursor(*a,**k): pass
  def overwriteMode(*a,**k): pass
  def paste(*a,**k): pass
  def print(*a,**k): pass
  def print_(*a,**k): pass
  def redo(*a,**k): pass
  def redoAvailable(*a,**k): pass
  def selectAll(*a,**k): pass
  def selectionChanged(*a,**k): pass
  def setBackgroundVisible(*a,**k): pass
  def setCenterOnScroll(*a,**k): pass
  def setCurrentCharFormat(*a,**k): pass
  def setCursorWidth(*a,**k): pass
  def setDocument(*a,**k): pass
  def setDocumentTitle(*a,**k): pass
  def setExtraSelections(*a,**k): pass
  def setLineWrapMode(*a,**k): pass
  def setMaximumBlockCount(*a,**k): pass
  def setOverwriteMode(*a,**k): pass
  def setPlainText(*a,**k): pass
  def setReadOnly(*a,**k): pass
  def setTabChangesFocus(*a,**k): pass
  def setTabStopWidth(*a,**k): pass
  def setTextCursor(*a,**k): pass
  def setTextInteractionFlags(*a,**k): pass
  def setUndoRedoEnabled(*a,**k): pass
  def setWordWrapMode(*a,**k): pass
  def tabChangesFocus(*a,**k): pass
  def tabStopWidth(*a,**k): pass
  def textChanged(*a,**k): pass
  def textCursor(*a,**k): pass
  def textInteractionFlags(*a,**k): pass
  def toPlainText(*a,**k): pass
  def undo(*a,**k): pass
  def undoAvailable(*a,**k): pass
  def updateRequest(*a,**k): pass
  def wordWrapMode(*a,**k): pass

class QScrollArea(QAbstractScrollArea):
  pass

  def alignment(*a,**k): pass
  def ensureVisible(*a,**k): pass
  def ensureWidgetVisible(*a,**k): pass
  def setAlignment(*a,**k): pass
  def setWidget(*a,**k): pass
  def setWidgetResizable(*a,**k): pass
  def takeWidget(*a,**k): pass
  def widget(*a,**k): pass
  def widgetResizable(*a,**k): pass

class QTextEdit(QAbstractScrollArea):
  pass
  AutoAll = -1
  AutoBulletList = 1
  AutoNone = 0
  FixedColumnWidth = 3
  FixedPixelWidth = 2
  NoWrap = 0
  WidgetWidth = 1
  def acceptRichText(*a,**k): pass
  def alignment(*a,**k): pass
  def anchorAt(*a,**k): pass
  def append(*a,**k): pass
  def autoFormatting(*a,**k): pass
  def canInsertFromMimeData(*a,**k): pass
  def canPaste(*a,**k): pass
  def clear(*a,**k): pass
  def copy(*a,**k): pass
  def copyAvailable(*a,**k): pass
  def createMimeDataFromSelection(*a,**k): pass
  def createStandardContextMenu(*a,**k): pass
  def currentCharFormat(*a,**k): pass
  def currentCharFormatChanged(*a,**k): pass
  def currentFont(*a,**k): pass
  def cursorForPosition(*a,**k): pass
  def cursorPositionChanged(*a,**k): pass
  def cursorRect(*a,**k): pass
  def cursorWidth(*a,**k): pass
  def cut(*a,**k): pass
  def document(*a,**k): pass
  def documentTitle(*a,**k): pass
  def ensureCursorVisible(*a,**k): pass
  def extraSelections(*a,**k): pass
  def fontFamily(*a,**k): pass
  def fontItalic(*a,**k): pass
  def fontPointSize(*a,**k): pass
  def fontUnderline(*a,**k): pass
  def fontWeight(*a,**k): pass
  def insertFromMimeData(*a,**k): pass
  def insertHtml(*a,**k): pass
  def insertPlainText(*a,**k): pass
  def isReadOnly(*a,**k): pass
  def isUndoRedoEnabled(*a,**k): pass
  def lineWrapColumnOrWidth(*a,**k): pass
  def lineWrapMode(*a,**k): pass
  def loadResource(*a,**k): pass
  def mergeCurrentCharFormat(*a,**k): pass
  def moveCursor(*a,**k): pass
  def overwriteMode(*a,**k): pass
  def paste(*a,**k): pass
  def print(*a,**k): pass
  def print_(*a,**k): pass
  def redo(*a,**k): pass
  def redoAvailable(*a,**k): pass
  def scrollToAnchor(*a,**k): pass
  def selectAll(*a,**k): pass
  def selectionChanged(*a,**k): pass
  def setAcceptRichText(*a,**k): pass
  def setAlignment(*a,**k): pass
  def setAutoFormatting(*a,**k): pass
  def setCurrentCharFormat(*a,**k): pass
  def setCurrentFont(*a,**k): pass
  def setCursorWidth(*a,**k): pass
  def setDocument(*a,**k): pass
  def setDocumentTitle(*a,**k): pass
  def setExtraSelections(*a,**k): pass
  def setFontFamily(*a,**k): pass
  def setFontItalic(*a,**k): pass
  def setFontPointSize(*a,**k): pass
  def setFontUnderline(*a,**k): pass
  def setFontWeight(*a,**k): pass
  def setHtml(*a,**k): pass
  def setLineWrapColumnOrWidth(*a,**k): pass
  def setLineWrapMode(*a,**k): pass
  def setOverwriteMode(*a,**k): pass
  def setPlainText(*a,**k): pass
  def setReadOnly(*a,**k): pass
  def setTabChangesFocus(*a,**k): pass
  def setTabStopWidth(*a,**k): pass
  def setText(*a,**k): pass
  def setTextBackgroundColor(*a,**k): pass
  def setTextColor(*a,**k): pass
  def setTextCursor(*a,**k): pass
  def setTextInteractionFlags(*a,**k): pass
  def setUndoRedoEnabled(*a,**k): pass
  def setWordWrapMode(*a,**k): pass
  def tabChangesFocus(*a,**k): pass
  def tabStopWidth(*a,**k): pass
  def textBackgroundColor(*a,**k): pass
  def textChanged(*a,**k): pass
  def textColor(*a,**k): pass
  def textCursor(*a,**k): pass
  def textInteractionFlags(*a,**k): pass
  def toHtml(*a,**k): pass
  def toPlainText(*a,**k): pass
  def undo(*a,**k): pass
  def undoAvailable(*a,**k): pass
  def wordWrapMode(*a,**k): pass
  def zoomIn(*a,**k): pass
  def zoomOut(*a,**k): pass

class QTextBrowser(QTextEdit):
  pass

  def anchorClicked(*a,**k): pass
  def backward(*a,**k): pass
  def backwardAvailable(*a,**k): pass
  def backwardHistoryCount(*a,**k): pass
  def clearHistory(*a,**k): pass
  def forward(*a,**k): pass
  def forwardAvailable(*a,**k): pass
  def forwardHistoryCount(*a,**k): pass
  def highlighted(*a,**k): pass
  def historyChanged(*a,**k): pass
  def historyTitle(*a,**k): pass
  def historyUrl(*a,**k): pass
  def home(*a,**k): pass
  def isBackwardAvailable(*a,**k): pass
  def isForwardAvailable(*a,**k): pass
  def openExternalLinks(*a,**k): pass
  def openLinks(*a,**k): pass
  def reload(*a,**k): pass
  def searchPaths(*a,**k): pass
  def setOpenExternalLinks(*a,**k): pass
  def setOpenLinks(*a,**k): pass
  def setSearchPaths(*a,**k): pass
  def setSource(*a,**k): pass
  def source(*a,**k): pass
  def sourceChanged(*a,**k): pass

class QToolBox(QFrame):
  pass

  def addItem(*a,**k): pass
  def count(*a,**k): pass
  def currentChanged(*a,**k): pass
  def currentIndex(*a,**k): pass
  def currentWidget(*a,**k): pass
  def indexOf(*a,**k): pass
  def insertItem(*a,**k): pass
  def isItemEnabled(*a,**k): pass
  def itemIcon(*a,**k): pass
  def itemInserted(*a,**k): pass
  def itemRemoved(*a,**k): pass
  def itemText(*a,**k): pass
  def itemToolTip(*a,**k): pass
  def removeItem(*a,**k): pass
  def setCurrentIndex(*a,**k): pass
  def setCurrentWidget(*a,**k): pass
  def setItemEnabled(*a,**k): pass
  def setItemIcon(*a,**k): pass
  def setItemText(*a,**k): pass
  def setItemToolTip(*a,**k): pass
  def widget(*a,**k): pass

class QLCDNumber(QFrame):
  pass
  Bin = 3
  Dec = 1
  Filled = 1
  Flat = 2
  Hex = 0
  Oct = 2
  Outline = 0
  def checkOverflow(*a,**k): pass
  def digitCount(*a,**k): pass
  def display(*a,**k): pass
  def intValue(*a,**k): pass
  def mode(*a,**k): pass
  def numDigits(*a,**k): pass
  def overflow(*a,**k): pass
  def segmentStyle(*a,**k): pass
  def setBinMode(*a,**k): pass
  def setDecMode(*a,**k): pass
  def setDigitCount(*a,**k): pass
  def setHexMode(*a,**k): pass
  def setMode(*a,**k): pass
  def setNumDigits(*a,**k): pass
  def setOctMode(*a,**k): pass
  def setSegmentStyle(*a,**k): pass
  def setSmallDecimalPoint(*a,**k): pass
  def smallDecimalPoint(*a,**k): pass
  def value(*a,**k): pass

class QLabel(QFrame):
  pass

  def alignment(*a,**k): pass
  def buddy(*a,**k): pass
  def clear(*a,**k): pass
  def hasScaledContents(*a,**k): pass
  def hasSelectedText(*a,**k): pass
  def indent(*a,**k): pass
  def linkActivated(*a,**k): pass
  def linkHovered(*a,**k): pass
  def margin(*a,**k): pass
  def movie(*a,**k): pass
  def openExternalLinks(*a,**k): pass
  def picture(*a,**k): pass
  def pixmap(*a,**k): pass
  def selectedText(*a,**k): pass
  def selectionStart(*a,**k): pass
  def setAlignment(*a,**k): pass
  def setBuddy(*a,**k): pass
  def setIndent(*a,**k): pass
  def setMargin(*a,**k): pass
  def setMovie(*a,**k): pass
  def setNum(*a,**k): pass
  def setOpenExternalLinks(*a,**k): pass
  def setPicture(*a,**k): pass
  def setPixmap(*a,**k): pass
  def setScaledContents(*a,**k): pass
  def setSelection(*a,**k): pass
  def setText(*a,**k): pass
  def setTextFormat(*a,**k): pass
  def setTextInteractionFlags(*a,**k): pass
  def setWordWrap(*a,**k): pass
  def text(*a,**k): pass
  def textFormat(*a,**k): pass
  def textInteractionFlags(*a,**k): pass
  def wordWrap(*a,**k): pass

class QSplitter(QFrame):
  pass

  def addWidget(*a,**k): pass
  def childrenCollapsible(*a,**k): pass
  def closestLegalPosition(*a,**k): pass
  def count(*a,**k): pass
  def createHandle(*a,**k): pass
  def getRange(*a,**k): pass
  def handleWidth(*a,**k): pass
  def indexOf(*a,**k): pass
  def insertWidget(*a,**k): pass
  def isCollapsible(*a,**k): pass
  def moveSplitter(*a,**k): pass
  def opaqueResize(*a,**k): pass
  def orientation(*a,**k): pass
  def refresh(*a,**k): pass
  def restoreState(*a,**k): pass
  def saveState(*a,**k): pass
  def setChildrenCollapsible(*a,**k): pass
  def setCollapsible(*a,**k): pass
  def setHandleWidth(*a,**k): pass
  def setOpaqueResize(*a,**k): pass
  def setOrientation(*a,**k): pass
  def setRubberBand(*a,**k): pass
  def setSizes(*a,**k): pass
  def setStretchFactor(*a,**k): pass
  def sizes(*a,**k): pass
  def splitterMoved(*a,**k): pass
  def widget(*a,**k): pass

class QStackedWidget(QFrame):
  pass

  def addWidget(*a,**k): pass
  def count(*a,**k): pass
  def currentChanged(*a,**k): pass
  def currentIndex(*a,**k): pass
  def currentWidget(*a,**k): pass
  def indexOf(*a,**k): pass
  def insertWidget(*a,**k): pass
  def removeWidget(*a,**k): pass
  def setCurrentIndex(*a,**k): pass
  def setCurrentWidget(*a,**k): pass
  def widget(*a,**k): pass
  def widgetRemoved(*a,**k): pass

class QDialog(QWidget):
  pass
  Accepted = 1
  Rejected = 0
  def accept(*a,**k): pass
  def accepted(*a,**k): pass
  def done(*a,**k): pass
  def exec_(*a,**k): pass
  def extension(*a,**k): pass
  def finished(*a,**k): pass
  def isSizeGripEnabled(*a,**k): pass
  def open(*a,**k): pass
  def orientation(*a,**k): pass
  def reject(*a,**k): pass
  def rejected(*a,**k): pass
  def result(*a,**k): pass
  def setExtension(*a,**k): pass
  def setModal(*a,**k): pass
  def setOrientation(*a,**k): pass
  def setResult(*a,**k): pass
  def setSizeGripEnabled(*a,**k): pass
  def showExtension(*a,**k): pass

class QAbstractPrintDialog(QDialog):
  pass
  AllPages = 0
  CurrentPage = 3
  DontUseSheet = 32
  PageRange = 2
  PrintCollateCopies = 16
  PrintCurrentPage = 64
  PrintPageRange = 4
  PrintSelection = 2
  PrintShowPageSize = 8
  PrintToFile = 1
  Selection = 1
  def addEnabledOption(*a,**k): pass
  def enabledOptions(*a,**k): pass
  def fromPage(*a,**k): pass
  def isOptionEnabled(*a,**k): pass
  def maxPage(*a,**k): pass
  def minPage(*a,**k): pass
  def printRange(*a,**k): pass
  def printer(*a,**k): pass
  def setEnabledOptions(*a,**k): pass
  def setFromTo(*a,**k): pass
  def setMinMax(*a,**k): pass
  def setOptionTabs(*a,**k): pass
  def setPrintRange(*a,**k): pass
  def toPage(*a,**k): pass

class QPrintDialog(QAbstractPrintDialog):
  pass

  def options(*a,**k): pass
  def setOption(*a,**k): pass
  def setOptions(*a,**k): pass
  def testOption(*a,**k): pass

class QColorDialog(QDialog):
  pass
  DontUseNativeDialog = 4
  NoButtons = 2
  ShowAlphaChannel = 1
  def colorSelected(*a,**k): pass
  def currentColor(*a,**k): pass
  def currentColorChanged(*a,**k): pass
  def customColor(*a,**k): pass
  def customCount(*a,**k): pass
  def getColor(*a,**k): pass
  def getRgba(*a,**k): pass
  def options(*a,**k): pass
  def selectedColor(*a,**k): pass
  def setCurrentColor(*a,**k): pass
  def setCustomColor(*a,**k): pass
  def setOption(*a,**k): pass
  def setOptions(*a,**k): pass
  def setStandardColor(*a,**k): pass
  def testOption(*a,**k): pass

class QErrorMessage(QDialog):
  pass

  def qtHandler(*a,**k): pass
  def showMessage(*a,**k): pass

class QFileDialog(QDialog):
  pass
  Accept = 3
  AcceptOpen = 0
  AcceptSave = 1
  AnyFile = 0
  Detail = 0
  Directory = 2
  DirectoryOnly = 4
  DontConfirmOverwrite = 4
  DontResolveSymlinks = 2
  DontUseNativeDialog = 16
  DontUseSheet = 8
  ExistingFile = 1
  ExistingFiles = 3
  FileName = 1
  FileType = 2
  HideNameFilterDetails = 64
  List = 1
  LookIn = 0
  ReadOnly = 32
  Reject = 4
  ShowDirsOnly = 1
  def acceptMode(*a,**k): pass
  def confirmOverwrite(*a,**k): pass
  def currentChanged(*a,**k): pass
  def defaultSuffix(*a,**k): pass
  def directory(*a,**k): pass
  def directoryEntered(*a,**k): pass
  def fileMode(*a,**k): pass
  def fileSelected(*a,**k): pass
  def filesSelected(*a,**k): pass
  def filter(*a,**k): pass
  def filterSelected(*a,**k): pass
  def filters(*a,**k): pass
  def getExistingDirectory(*a,**k): pass
  def getOpenFileName(*a,**k): pass
  def getOpenFileNameAndFilter(*a,**k): pass
  def getOpenFileNames(*a,**k): pass
  def getOpenFileNamesAndFilter(*a,**k): pass
  def getSaveFileName(*a,**k): pass
  def getSaveFileNameAndFilter(*a,**k): pass
  def history(*a,**k): pass
  def iconProvider(*a,**k): pass
  def isNameFilterDetailsVisible(*a,**k): pass
  def isReadOnly(*a,**k): pass
  def itemDelegate(*a,**k): pass
  def labelText(*a,**k): pass
  def nameFilters(*a,**k): pass
  def options(*a,**k): pass
  def proxyModel(*a,**k): pass
  def resolveSymlinks(*a,**k): pass
  def restoreState(*a,**k): pass
  def saveState(*a,**k): pass
  def selectFile(*a,**k): pass
  def selectFilter(*a,**k): pass
  def selectNameFilter(*a,**k): pass
  def selectedFiles(*a,**k): pass
  def selectedFilter(*a,**k): pass
  def selectedNameFilter(*a,**k): pass
  def setAcceptMode(*a,**k): pass
  def setConfirmOverwrite(*a,**k): pass
  def setDefaultSuffix(*a,**k): pass
  def setDirectory(*a,**k): pass
  def setFileMode(*a,**k): pass
  def setFilter(*a,**k): pass
  def setFilters(*a,**k): pass
  def setHistory(*a,**k): pass
  def setIconProvider(*a,**k): pass
  def setItemDelegate(*a,**k): pass
  def setLabelText(*a,**k): pass
  def setNameFilter(*a,**k): pass
  def setNameFilterDetailsVisible(*a,**k): pass
  def setNameFilters(*a,**k): pass
  def setOption(*a,**k): pass
  def setOptions(*a,**k): pass
  def setProxyModel(*a,**k): pass
  def setReadOnly(*a,**k): pass
  def setResolveSymlinks(*a,**k): pass
  def setSidebarUrls(*a,**k): pass
  def setViewMode(*a,**k): pass
  def sidebarUrls(*a,**k): pass
  def testOption(*a,**k): pass
  def viewMode(*a,**k): pass

class QFontDialog(QDialog):
  pass
  DontUseNativeDialog = 2
  NoButtons = 1
  def currentFont(*a,**k): pass
  def currentFontChanged(*a,**k): pass
  def fontSelected(*a,**k): pass
  def getFont(*a,**k): pass
  def options(*a,**k): pass
  def selectedFont(*a,**k): pass
  def setCurrentFont(*a,**k): pass
  def setOption(*a,**k): pass
  def setOptions(*a,**k): pass
  def testOption(*a,**k): pass

class QInputDialog(QDialog):
  pass
  DoubleInput = 2
  IntInput = 1
  NoButtons = 1
  TextInput = 0
  UseListViewForComboBoxItems = 2
  def cancelButtonText(*a,**k): pass
  def comboBoxItems(*a,**k): pass
  def doubleDecimals(*a,**k): pass
  def doubleMaximum(*a,**k): pass
  def doubleMinimum(*a,**k): pass
  def doubleValue(*a,**k): pass
  def doubleValueChanged(*a,**k): pass
  def doubleValueSelected(*a,**k): pass
  def getDouble(*a,**k): pass
  def getInt(*a,**k): pass
  def getInteger(*a,**k): pass
  def getItem(*a,**k): pass
  def getText(*a,**k): pass
  def inputMode(*a,**k): pass
  def intMaximum(*a,**k): pass
  def intMinimum(*a,**k): pass
  def intStep(*a,**k): pass
  def intValue(*a,**k): pass
  def intValueChanged(*a,**k): pass
  def intValueSelected(*a,**k): pass
  def isComboBoxEditable(*a,**k): pass
  def labelText(*a,**k): pass
  def okButtonText(*a,**k): pass
  def options(*a,**k): pass
  def setCancelButtonText(*a,**k): pass
  def setComboBoxEditable(*a,**k): pass
  def setComboBoxItems(*a,**k): pass
  def setDoubleDecimals(*a,**k): pass
  def setDoubleMaximum(*a,**k): pass
  def setDoubleMinimum(*a,**k): pass
  def setDoubleRange(*a,**k): pass
  def setDoubleValue(*a,**k): pass
  def setInputMode(*a,**k): pass
  def setIntMaximum(*a,**k): pass
  def setIntMinimum(*a,**k): pass
  def setIntRange(*a,**k): pass
  def setIntStep(*a,**k): pass
  def setIntValue(*a,**k): pass
  def setLabelText(*a,**k): pass
  def setOkButtonText(*a,**k): pass
  def setOption(*a,**k): pass
  def setOptions(*a,**k): pass
  def setTextEchoMode(*a,**k): pass
  def setTextValue(*a,**k): pass
  def testOption(*a,**k): pass
  def textEchoMode(*a,**k): pass
  def textValue(*a,**k): pass
  def textValueChanged(*a,**k): pass
  def textValueSelected(*a,**k): pass

class QMessageBox(QDialog):
  pass
  Abort = 262144
  AcceptRole = 0
  ActionRole = 3
  Apply = 33554432
  ApplyRole = 8
  ButtonMask = -769
  Cancel = 4194304
  Close = 2097152
  Critical = 3
  Default = 256
  DestructiveRole = 2
  Discard = 8388608
  Escape = 512
  FirstButton = 1024
  FlagMask = 768
  Help = 16777216
  HelpRole = 4
  Ignore = 1048576
  Information = 1
  InvalidRole = -1
  LastButton = 134217728
  No = 65536
  NoAll = 131072
  NoButton = 0
  NoIcon = 0
  NoRole = 6
  NoToAll = 131072
  Ok = 1024
  Open = 8192
  Question = 4
  RejectRole = 1
  Reset = 67108864
  ResetRole = 7
  RestoreDefaults = 134217728
  Retry = 524288
  Save = 2048
  SaveAll = 4096
  Warning = 2
  Yes = 16384
  YesAll = 32768
  YesRole = 5
  YesToAll = 32768
  def about(*a,**k): pass
  def aboutQt(*a,**k): pass
  def addButton(*a,**k): pass
  def button(*a,**k): pass
  def buttonClicked(*a,**k): pass
  def buttonRole(*a,**k): pass
  def buttonText(*a,**k): pass
  def buttons(*a,**k): pass
  def clickedButton(*a,**k): pass
  def critical(*a,**k): pass
  def defaultButton(*a,**k): pass
  def detailedText(*a,**k): pass
  def escapeButton(*a,**k): pass
  def icon(*a,**k): pass
  def iconPixmap(*a,**k): pass
  def information(*a,**k): pass
  def informativeText(*a,**k): pass
  def question(*a,**k): pass
  def removeButton(*a,**k): pass
  def setButtonText(*a,**k): pass
  def setDefaultButton(*a,**k): pass
  def setDetailedText(*a,**k): pass
  def setEscapeButton(*a,**k): pass
  def setIcon(*a,**k): pass
  def setIconPixmap(*a,**k): pass
  def setInformativeText(*a,**k): pass
  def setStandardButtons(*a,**k): pass
  def setText(*a,**k): pass
  def setTextFormat(*a,**k): pass
  def standardButton(*a,**k): pass
  def standardButtons(*a,**k): pass
  def standardIcon(*a,**k): pass
  def text(*a,**k): pass
  def textFormat(*a,**k): pass
  def warning(*a,**k): pass

class QPageSetupDialog(QDialog):
  pass
  DontUseSheet = 1
  def addEnabledOption(*a,**k): pass
  def enabledOptions(*a,**k): pass
  def isOptionEnabled(*a,**k): pass
  def options(*a,**k): pass
  def printer(*a,**k): pass
  def setEnabledOptions(*a,**k): pass
  def setOption(*a,**k): pass
  def setOptions(*a,**k): pass
  def testOption(*a,**k): pass

class QPrintPreviewDialog(QDialog):
  pass

  def paintRequested(*a,**k): pass
  def printer(*a,**k): pass

class QProgressDialog(QDialog):
  pass

  def autoClose(*a,**k): pass
  def autoReset(*a,**k): pass
  def cancel(*a,**k): pass
  def canceled(*a,**k): pass
  def forceShow(*a,**k): pass
  def labelText(*a,**k): pass
  def maximum(*a,**k): pass
  def minimum(*a,**k): pass
  def minimumDuration(*a,**k): pass
  def reset(*a,**k): pass
  def setAutoClose(*a,**k): pass
  def setAutoReset(*a,**k): pass
  def setBar(*a,**k): pass
  def setCancelButton(*a,**k): pass
  def setCancelButtonText(*a,**k): pass
  def setLabel(*a,**k): pass
  def setLabelText(*a,**k): pass
  def setMaximum(*a,**k): pass
  def setMinimum(*a,**k): pass
  def setMinimumDuration(*a,**k): pass
  def setRange(*a,**k): pass
  def setValue(*a,**k): pass
  def value(*a,**k): pass
  def wasCanceled(*a,**k): pass

class QWizard(QDialog):
  pass
  AeroStyle = 3
  BackButton = 0
  BackgroundPixmap = 3
  BannerPixmap = 2
  CancelButton = 4
  CancelButtonOnLeft = 1024
  ClassicStyle = 0
  CommitButton = 2
  CustomButton1 = 6
  CustomButton2 = 7
  CustomButton3 = 8
  DisabledBackButtonOnLastPage = 64
  ExtendedWatermarkPixmap = 4
  FinishButton = 3
  HaveCustomButton1 = 8192
  HaveCustomButton2 = 16384
  HaveCustomButton3 = 32768
  HaveFinishButtonOnEarlyPages = 256
  HaveHelpButton = 2048
  HaveNextButtonOnLastPage = 128
  HelpButton = 5
  HelpButtonOnRight = 4096
  IgnoreSubTitles = 2
  IndependentPages = 1
  LogoPixmap = 1
  MacStyle = 2
  ModernStyle = 1
  NextButton = 1
  NoBackButtonOnLastPage = 32
  NoBackButtonOnStartPage = 16
  NoCancelButton = 512
  NoDefaultButton = 8
  Stretch = 9
  WatermarkPixmap = 0
  def addPage(*a,**k): pass
  def back(*a,**k): pass
  def button(*a,**k): pass
  def buttonText(*a,**k): pass
  def cleanupPage(*a,**k): pass
  def currentId(*a,**k): pass
  def currentIdChanged(*a,**k): pass
  def currentPage(*a,**k): pass
  def customButtonClicked(*a,**k): pass
  def field(*a,**k): pass
  def hasVisitedPage(*a,**k): pass
  def helpRequested(*a,**k): pass
  def initializePage(*a,**k): pass
  def next(*a,**k): pass
  def nextId(*a,**k): pass
  def options(*a,**k): pass
  def page(*a,**k): pass
  def pageAdded(*a,**k): pass
  def pageIds(*a,**k): pass
  def pageRemoved(*a,**k): pass
  def pixmap(*a,**k): pass
  def removePage(*a,**k): pass
  def restart(*a,**k): pass
  def setButton(*a,**k): pass
  def setButtonLayout(*a,**k): pass
  def setButtonText(*a,**k): pass
  def setDefaultProperty(*a,**k): pass
  def setField(*a,**k): pass
  def setOption(*a,**k): pass
  def setOptions(*a,**k): pass
  def setPage(*a,**k): pass
  def setPixmap(*a,**k): pass
  def setSideWidget(*a,**k): pass
  def setStartId(*a,**k): pass
  def setSubTitleFormat(*a,**k): pass
  def setTitleFormat(*a,**k): pass
  def setWizardStyle(*a,**k): pass
  def sideWidget(*a,**k): pass
  def startId(*a,**k): pass
  def subTitleFormat(*a,**k): pass
  def testOption(*a,**k): pass
  def titleFormat(*a,**k): pass
  def validateCurrentPage(*a,**k): pass
  def visitedPages(*a,**k): pass
  def wizardStyle(*a,**k): pass

class QAbstractSlider(QWidget):
  pass
  SliderMove = 7
  SliderNoAction = 0
  SliderOrientationChange = 1
  SliderPageStepAdd = 3
  SliderPageStepSub = 4
  SliderRangeChange = 0
  SliderSingleStepAdd = 1
  SliderSingleStepSub = 2
  SliderStepsChange = 2
  SliderToMaximum = 6
  SliderToMinimum = 5
  SliderValueChange = 3
  def actionTriggered(*a,**k): pass
  def hasTracking(*a,**k): pass
  def invertedAppearance(*a,**k): pass
  def invertedControls(*a,**k): pass
  def isSliderDown(*a,**k): pass
  def maximum(*a,**k): pass
  def minimum(*a,**k): pass
  def orientation(*a,**k): pass
  def pageStep(*a,**k): pass
  def rangeChanged(*a,**k): pass
  def repeatAction(*a,**k): pass
  def setInvertedAppearance(*a,**k): pass
  def setInvertedControls(*a,**k): pass
  def setMaximum(*a,**k): pass
  def setMinimum(*a,**k): pass
  def setOrientation(*a,**k): pass
  def setPageStep(*a,**k): pass
  def setRange(*a,**k): pass
  def setRepeatAction(*a,**k): pass
  def setSingleStep(*a,**k): pass
  def setSliderDown(*a,**k): pass
  def setSliderPosition(*a,**k): pass
  def setTracking(*a,**k): pass
  def setValue(*a,**k): pass
  def singleStep(*a,**k): pass
  def sliderChange(*a,**k): pass
  def sliderMoved(*a,**k): pass
  def sliderPosition(*a,**k): pass
  def sliderPressed(*a,**k): pass
  def sliderReleased(*a,**k): pass
  def triggerAction(*a,**k): pass
  def value(*a,**k): pass
  def valueChanged(*a,**k): pass

class QDial(QAbstractSlider):
  pass

  def initStyleOption(*a,**k): pass
  def notchSize(*a,**k): pass
  def notchTarget(*a,**k): pass
  def notchesVisible(*a,**k): pass
  def setNotchTarget(*a,**k): pass
  def setNotchesVisible(*a,**k): pass
  def setWrapping(*a,**k): pass
  def wrapping(*a,**k): pass

class QScrollBar(QAbstractSlider):
  pass

  def initStyleOption(*a,**k): pass

class QSlider(QAbstractSlider):
  pass
  NoTicks = 0
  TicksAbove = 1
  TicksBelow = 2
  TicksBothSides = 3
  TicksLeft = 1
  TicksRight = 2
  def initStyleOption(*a,**k): pass
  def setTickInterval(*a,**k): pass
  def setTickPosition(*a,**k): pass
  def tickInterval(*a,**k): pass
  def tickPosition(*a,**k): pass

class QAbstractSpinBox(QWidget):
  pass
  CorrectToNearestValue = 1
  CorrectToPreviousValue = 0
  NoButtons = 2
  PlusMinus = 1
  StepDownEnabled = 2
  StepNone = 0
  StepUpEnabled = 1
  UpDownArrows = 0
  def alignment(*a,**k): pass
  def buttonSymbols(*a,**k): pass
  def clear(*a,**k): pass
  def correctionMode(*a,**k): pass
  def editingFinished(*a,**k): pass
  def fixup(*a,**k): pass
  def hasAcceptableInput(*a,**k): pass
  def hasFrame(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def interpretText(*a,**k): pass
  def isAccelerated(*a,**k): pass
  def isReadOnly(*a,**k): pass
  def keyboardTracking(*a,**k): pass
  def lineEdit(*a,**k): pass
  def selectAll(*a,**k): pass
  def setAccelerated(*a,**k): pass
  def setAlignment(*a,**k): pass
  def setButtonSymbols(*a,**k): pass
  def setCorrectionMode(*a,**k): pass
  def setFrame(*a,**k): pass
  def setKeyboardTracking(*a,**k): pass
  def setLineEdit(*a,**k): pass
  def setReadOnly(*a,**k): pass
  def setSpecialValueText(*a,**k): pass
  def setWrapping(*a,**k): pass
  def specialValueText(*a,**k): pass
  def stepBy(*a,**k): pass
  def stepDown(*a,**k): pass
  def stepEnabled(*a,**k): pass
  def stepUp(*a,**k): pass
  def text(*a,**k): pass
  def validate(*a,**k): pass
  def wrapping(*a,**k): pass

class QDateTimeEdit(QAbstractSpinBox):
  pass
  AmPmSection = 1
  DateSections_Mask = 1792
  DaySection = 256
  HourSection = 16
  MSecSection = 2
  MinuteSection = 8
  MonthSection = 512
  NoSection = 0
  SecondSection = 4
  TimeSections_Mask = 31
  YearSection = 1024
  def calendarPopup(*a,**k): pass
  def calendarWidget(*a,**k): pass
  def clearMaximumDate(*a,**k): pass
  def clearMaximumDateTime(*a,**k): pass
  def clearMaximumTime(*a,**k): pass
  def clearMinimumDate(*a,**k): pass
  def clearMinimumDateTime(*a,**k): pass
  def clearMinimumTime(*a,**k): pass
  def currentSection(*a,**k): pass
  def currentSectionIndex(*a,**k): pass
  def date(*a,**k): pass
  def dateChanged(*a,**k): pass
  def dateTime(*a,**k): pass
  def dateTimeChanged(*a,**k): pass
  def dateTimeFromText(*a,**k): pass
  def displayFormat(*a,**k): pass
  def displayedSections(*a,**k): pass
  def maximumDate(*a,**k): pass
  def maximumDateTime(*a,**k): pass
  def maximumTime(*a,**k): pass
  def minimumDate(*a,**k): pass
  def minimumDateTime(*a,**k): pass
  def minimumTime(*a,**k): pass
  def sectionAt(*a,**k): pass
  def sectionCount(*a,**k): pass
  def sectionText(*a,**k): pass
  def setCalendarPopup(*a,**k): pass
  def setCalendarWidget(*a,**k): pass
  def setCurrentSection(*a,**k): pass
  def setCurrentSectionIndex(*a,**k): pass
  def setDate(*a,**k): pass
  def setDateRange(*a,**k): pass
  def setDateTime(*a,**k): pass
  def setDateTimeRange(*a,**k): pass
  def setDisplayFormat(*a,**k): pass
  def setMaximumDate(*a,**k): pass
  def setMaximumDateTime(*a,**k): pass
  def setMaximumTime(*a,**k): pass
  def setMinimumDate(*a,**k): pass
  def setMinimumDateTime(*a,**k): pass
  def setMinimumTime(*a,**k): pass
  def setSelectedSection(*a,**k): pass
  def setTime(*a,**k): pass
  def setTimeRange(*a,**k): pass
  def setTimeSpec(*a,**k): pass
  def textFromDateTime(*a,**k): pass
  def time(*a,**k): pass
  def timeChanged(*a,**k): pass
  def timeSpec(*a,**k): pass

class QDateEdit(QDateTimeEdit):
  pass



class QTimeEdit(QDateTimeEdit):
  pass



class QDoubleSpinBox(QAbstractSpinBox):
  pass

  def cleanText(*a,**k): pass
  def decimals(*a,**k): pass
  def maximum(*a,**k): pass
  def minimum(*a,**k): pass
  def prefix(*a,**k): pass
  def setDecimals(*a,**k): pass
  def setMaximum(*a,**k): pass
  def setMinimum(*a,**k): pass
  def setPrefix(*a,**k): pass
  def setRange(*a,**k): pass
  def setSingleStep(*a,**k): pass
  def setSuffix(*a,**k): pass
  def setValue(*a,**k): pass
  def singleStep(*a,**k): pass
  def suffix(*a,**k): pass
  def textFromValue(*a,**k): pass
  def value(*a,**k): pass
  def valueChanged(*a,**k): pass
  def valueFromText(*a,**k): pass

class QSpinBox(QAbstractSpinBox):
  pass

  def cleanText(*a,**k): pass
  def maximum(*a,**k): pass
  def minimum(*a,**k): pass
  def prefix(*a,**k): pass
  def setMaximum(*a,**k): pass
  def setMinimum(*a,**k): pass
  def setPrefix(*a,**k): pass
  def setRange(*a,**k): pass
  def setSingleStep(*a,**k): pass
  def setSuffix(*a,**k): pass
  def setValue(*a,**k): pass
  def singleStep(*a,**k): pass
  def suffix(*a,**k): pass
  def textFromValue(*a,**k): pass
  def value(*a,**k): pass
  def valueChanged(*a,**k): pass
  def valueFromText(*a,**k): pass

class QCalendarWidget(QWidget):
  pass
  ISOWeekNumbers = 1
  LongDayNames = 3
  NoHorizontalHeader = 0
  NoSelection = 0
  NoVerticalHeader = 0
  ShortDayNames = 2
  SingleLetterDayNames = 1
  SingleSelection = 1
  def activated(*a,**k): pass
  def clicked(*a,**k): pass
  def currentPageChanged(*a,**k): pass
  def dateEditAcceptDelay(*a,**k): pass
  def dateTextFormat(*a,**k): pass
  def firstDayOfWeek(*a,**k): pass
  def headerTextFormat(*a,**k): pass
  def horizontalHeaderFormat(*a,**k): pass
  def isDateEditEnabled(*a,**k): pass
  def isGridVisible(*a,**k): pass
  def isHeaderVisible(*a,**k): pass
  def isNavigationBarVisible(*a,**k): pass
  def maximumDate(*a,**k): pass
  def minimumDate(*a,**k): pass
  def monthShown(*a,**k): pass
  def paintCell(*a,**k): pass
  def selectedDate(*a,**k): pass
  def selectionChanged(*a,**k): pass
  def selectionMode(*a,**k): pass
  def setCurrentPage(*a,**k): pass
  def setDateEditAcceptDelay(*a,**k): pass
  def setDateEditEnabled(*a,**k): pass
  def setDateRange(*a,**k): pass
  def setDateTextFormat(*a,**k): pass
  def setFirstDayOfWeek(*a,**k): pass
  def setGridVisible(*a,**k): pass
  def setHeaderTextFormat(*a,**k): pass
  def setHeaderVisible(*a,**k): pass
  def setHorizontalHeaderFormat(*a,**k): pass
  def setMaximumDate(*a,**k): pass
  def setMinimumDate(*a,**k): pass
  def setNavigationBarVisible(*a,**k): pass
  def setSelectedDate(*a,**k): pass
  def setSelectionMode(*a,**k): pass
  def setVerticalHeaderFormat(*a,**k): pass
  def setWeekdayTextFormat(*a,**k): pass
  def showNextMonth(*a,**k): pass
  def showNextYear(*a,**k): pass
  def showPreviousMonth(*a,**k): pass
  def showPreviousYear(*a,**k): pass
  def showSelectedDate(*a,**k): pass
  def showToday(*a,**k): pass
  def updateCell(*a,**k): pass
  def updateCells(*a,**k): pass
  def verticalHeaderFormat(*a,**k): pass
  def weekdayTextFormat(*a,**k): pass
  def yearShown(*a,**k): pass

class QComboBox(QWidget):
  pass
  AdjustToContents = 0
  AdjustToContentsOnFirstShow = 1
  AdjustToMinimumContentsLength = 2
  AdjustToMinimumContentsLengthWithIcon = 3
  InsertAfterCurrent = 4
  InsertAlphabetically = 6
  InsertAtBottom = 3
  InsertAtCurrent = 2
  InsertAtTop = 1
  InsertBeforeCurrent = 5
  NoInsert = 0
  def activated(*a,**k): pass
  def addItem(*a,**k): pass
  def addItems(*a,**k): pass
  def autoCompletion(*a,**k): pass
  def autoCompletionCaseSensitivity(*a,**k): pass
  def clear(*a,**k): pass
  def clearEditText(*a,**k): pass
  def completer(*a,**k): pass
  def count(*a,**k): pass
  def currentIndex(*a,**k): pass
  def currentIndexChanged(*a,**k): pass
  def currentText(*a,**k): pass
  def duplicatesEnabled(*a,**k): pass
  def editTextChanged(*a,**k): pass
  def findData(*a,**k): pass
  def findText(*a,**k): pass
  def hasFrame(*a,**k): pass
  def hidePopup(*a,**k): pass
  def highlighted(*a,**k): pass
  def iconSize(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def insertItem(*a,**k): pass
  def insertItems(*a,**k): pass
  def insertPolicy(*a,**k): pass
  def insertSeparator(*a,**k): pass
  def isEditable(*a,**k): pass
  def itemData(*a,**k): pass
  def itemDelegate(*a,**k): pass
  def itemIcon(*a,**k): pass
  def itemText(*a,**k): pass
  def lineEdit(*a,**k): pass
  def maxCount(*a,**k): pass
  def maxVisibleItems(*a,**k): pass
  def minimumContentsLength(*a,**k): pass
  def model(*a,**k): pass
  def modelColumn(*a,**k): pass
  def removeItem(*a,**k): pass
  def rootModelIndex(*a,**k): pass
  def setAutoCompletion(*a,**k): pass
  def setAutoCompletionCaseSensitivity(*a,**k): pass
  def setCompleter(*a,**k): pass
  def setCurrentIndex(*a,**k): pass
  def setDuplicatesEnabled(*a,**k): pass
  def setEditText(*a,**k): pass
  def setEditable(*a,**k): pass
  def setFrame(*a,**k): pass
  def setIconSize(*a,**k): pass
  def setInsertPolicy(*a,**k): pass
  def setItemData(*a,**k): pass
  def setItemDelegate(*a,**k): pass
  def setItemIcon(*a,**k): pass
  def setItemText(*a,**k): pass
  def setLineEdit(*a,**k): pass
  def setMaxCount(*a,**k): pass
  def setMaxVisibleItems(*a,**k): pass
  def setMinimumContentsLength(*a,**k): pass
  def setModel(*a,**k): pass
  def setModelColumn(*a,**k): pass
  def setRootModelIndex(*a,**k): pass
  def setSizeAdjustPolicy(*a,**k): pass
  def setValidator(*a,**k): pass
  def setView(*a,**k): pass
  def showPopup(*a,**k): pass
  def sizeAdjustPolicy(*a,**k): pass
  def validator(*a,**k): pass
  def view(*a,**k): pass

class QFontComboBox(QComboBox):
  pass
  AllFonts = 0
  MonospacedFonts = 4
  NonScalableFonts = 2
  ProportionalFonts = 8
  ScalableFonts = 1
  def currentFont(*a,**k): pass
  def currentFontChanged(*a,**k): pass
  def fontFilters(*a,**k): pass
  def setCurrentFont(*a,**k): pass
  def setFontFilters(*a,**k): pass
  def setWritingSystem(*a,**k): pass
  def writingSystem(*a,**k): pass

class QDesktopWidget(QWidget):
  pass

  def availableGeometry(*a,**k): pass
  def isVirtualDesktop(*a,**k): pass
  def numScreens(*a,**k): pass
  def primaryScreen(*a,**k): pass
  def resized(*a,**k): pass
  def screen(*a,**k): pass
  def screenCount(*a,**k): pass
  def screenCountChanged(*a,**k): pass
  def screenGeometry(*a,**k): pass
  def screenNumber(*a,**k): pass
  def workAreaResized(*a,**k): pass

class QDialogButtonBox(QWidget):
  pass
  Abort = 262144
  AcceptRole = 0
  ActionRole = 3
  Apply = 33554432
  ApplyRole = 8
  Cancel = 4194304
  Close = 2097152
  DestructiveRole = 2
  Discard = 8388608
  GnomeLayout = 3
  Help = 16777216
  HelpRole = 4
  Ignore = 1048576
  InvalidRole = -1
  KdeLayout = 2
  MacLayout = 1
  No = 65536
  NoButton = 0
  NoRole = 6
  NoToAll = 131072
  Ok = 1024
  Open = 8192
  RejectRole = 1
  Reset = 67108864
  ResetRole = 7
  RestoreDefaults = 134217728
  Retry = 524288
  Save = 2048
  SaveAll = 4096
  WinLayout = 0
  Yes = 16384
  YesRole = 5
  YesToAll = 32768
  def accepted(*a,**k): pass
  def addButton(*a,**k): pass
  def button(*a,**k): pass
  def buttonRole(*a,**k): pass
  def buttons(*a,**k): pass
  def centerButtons(*a,**k): pass
  def clear(*a,**k): pass
  def clicked(*a,**k): pass
  def helpRequested(*a,**k): pass
  def orientation(*a,**k): pass
  def rejected(*a,**k): pass
  def removeButton(*a,**k): pass
  def setCenterButtons(*a,**k): pass
  def setOrientation(*a,**k): pass
  def setStandardButtons(*a,**k): pass
  def standardButton(*a,**k): pass
  def standardButtons(*a,**k): pass

class QDockWidget(QWidget):
  pass
  AllDockWidgetFeatures = 7
  DockWidgetClosable = 1
  DockWidgetFloatable = 4
  DockWidgetMovable = 2
  DockWidgetVerticalTitleBar = 8
  NoDockWidgetFeatures = 0
  def allowedAreas(*a,**k): pass
  def allowedAreasChanged(*a,**k): pass
  def dockLocationChanged(*a,**k): pass
  def features(*a,**k): pass
  def featuresChanged(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def isAreaAllowed(*a,**k): pass
  def isFloating(*a,**k): pass
  def setAllowedAreas(*a,**k): pass
  def setFeatures(*a,**k): pass
  def setFloating(*a,**k): pass
  def setTitleBarWidget(*a,**k): pass
  def setWidget(*a,**k): pass
  def titleBarWidget(*a,**k): pass
  def toggleViewAction(*a,**k): pass
  def topLevelChanged(*a,**k): pass
  def visibilityChanged(*a,**k): pass
  def widget(*a,**k): pass

class QToolBar(QWidget):
  pass

  def actionAt(*a,**k): pass
  def actionGeometry(*a,**k): pass
  def actionTriggered(*a,**k): pass
  def addSeparator(*a,**k): pass
  def addWidget(*a,**k): pass
  def allowedAreas(*a,**k): pass
  def allowedAreasChanged(*a,**k): pass
  def clear(*a,**k): pass
  def iconSize(*a,**k): pass
  def iconSizeChanged(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def insertSeparator(*a,**k): pass
  def insertWidget(*a,**k): pass
  def isAreaAllowed(*a,**k): pass
  def isFloatable(*a,**k): pass
  def isFloating(*a,**k): pass
  def isMovable(*a,**k): pass
  def movableChanged(*a,**k): pass
  def orientation(*a,**k): pass
  def orientationChanged(*a,**k): pass
  def setAllowedAreas(*a,**k): pass
  def setFloatable(*a,**k): pass
  def setIconSize(*a,**k): pass
  def setMovable(*a,**k): pass
  def setOrientation(*a,**k): pass
  def setToolButtonStyle(*a,**k): pass
  def toggleViewAction(*a,**k): pass
  def toolButtonStyle(*a,**k): pass
  def toolButtonStyleChanged(*a,**k): pass
  def topLevelChanged(*a,**k): pass
  def visibilityChanged(*a,**k): pass
  def widgetForAction(*a,**k): pass

class QFocusFrame(QWidget):
  pass

  def initStyleOption(*a,**k): pass
  def setWidget(*a,**k): pass
  def widget(*a,**k): pass

class QGroupBox(QWidget):
  pass

  def alignment(*a,**k): pass
  def clicked(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def isCheckable(*a,**k): pass
  def isChecked(*a,**k): pass
  def isFlat(*a,**k): pass
  def setAlignment(*a,**k): pass
  def setCheckable(*a,**k): pass
  def setChecked(*a,**k): pass
  def setFlat(*a,**k): pass
  def setTitle(*a,**k): pass
  def title(*a,**k): pass
  def toggled(*a,**k): pass

class QLineEdit(QWidget):
  pass
  NoEcho = 1
  Normal = 0
  Password = 2
  PasswordEchoOnEdit = 3
  def alignment(*a,**k): pass
  def backspace(*a,**k): pass
  def clear(*a,**k): pass
  def completer(*a,**k): pass
  def copy(*a,**k): pass
  def createStandardContextMenu(*a,**k): pass
  def cursorBackward(*a,**k): pass
  def cursorForward(*a,**k): pass
  def cursorMoveStyle(*a,**k): pass
  def cursorPosition(*a,**k): pass
  def cursorPositionAt(*a,**k): pass
  def cursorPositionChanged(*a,**k): pass
  def cursorRect(*a,**k): pass
  def cursorWordBackward(*a,**k): pass
  def cursorWordForward(*a,**k): pass
  def cut(*a,**k): pass
  def del_(*a,**k): pass
  def deselect(*a,**k): pass
  def displayText(*a,**k): pass
  def dragEnabled(*a,**k): pass
  def echoMode(*a,**k): pass
  def editingFinished(*a,**k): pass
  def end(*a,**k): pass
  def getTextMargins(*a,**k): pass
  def hasAcceptableInput(*a,**k): pass
  def hasFrame(*a,**k): pass
  def hasSelectedText(*a,**k): pass
  def home(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def inputMask(*a,**k): pass
  def insert(*a,**k): pass
  def isModified(*a,**k): pass
  def isReadOnly(*a,**k): pass
  def isRedoAvailable(*a,**k): pass
  def isUndoAvailable(*a,**k): pass
  def maxLength(*a,**k): pass
  def paste(*a,**k): pass
  def placeholderText(*a,**k): pass
  def redo(*a,**k): pass
  def returnPressed(*a,**k): pass
  def selectAll(*a,**k): pass
  def selectedText(*a,**k): pass
  def selectionChanged(*a,**k): pass
  def selectionStart(*a,**k): pass
  def setAlignment(*a,**k): pass
  def setCompleter(*a,**k): pass
  def setCursorMoveStyle(*a,**k): pass
  def setCursorPosition(*a,**k): pass
  def setDragEnabled(*a,**k): pass
  def setEchoMode(*a,**k): pass
  def setFrame(*a,**k): pass
  def setInputMask(*a,**k): pass
  def setMaxLength(*a,**k): pass
  def setModified(*a,**k): pass
  def setPlaceholderText(*a,**k): pass
  def setReadOnly(*a,**k): pass
  def setSelection(*a,**k): pass
  def setText(*a,**k): pass
  def setTextMargins(*a,**k): pass
  def setValidator(*a,**k): pass
  def text(*a,**k): pass
  def textChanged(*a,**k): pass
  def textEdited(*a,**k): pass
  def textMargins(*a,**k): pass
  def undo(*a,**k): pass
  def validator(*a,**k): pass

class QMainWindow(QWidget):
  pass
  AllowNestedDocks = 2
  AllowTabbedDocks = 4
  AnimatedDocks = 1
  ForceTabbedDocks = 8
  VerticalTabs = 16
  def addDockWidget(*a,**k): pass
  def addToolBar(*a,**k): pass
  def addToolBarBreak(*a,**k): pass
  def centralWidget(*a,**k): pass
  def corner(*a,**k): pass
  def createPopupMenu(*a,**k): pass
  def dockOptions(*a,**k): pass
  def dockWidgetArea(*a,**k): pass
  def documentMode(*a,**k): pass
  def iconSize(*a,**k): pass
  def iconSizeChanged(*a,**k): pass
  def insertToolBar(*a,**k): pass
  def insertToolBarBreak(*a,**k): pass
  def isAnimated(*a,**k): pass
  def isDockNestingEnabled(*a,**k): pass
  def isSeparator(*a,**k): pass
  def menuBar(*a,**k): pass
  def menuWidget(*a,**k): pass
  def removeDockWidget(*a,**k): pass
  def removeToolBar(*a,**k): pass
  def removeToolBarBreak(*a,**k): pass
  def restoreDockWidget(*a,**k): pass
  def restoreState(*a,**k): pass
  def saveState(*a,**k): pass
  def setAnimated(*a,**k): pass
  def setCentralWidget(*a,**k): pass
  def setCorner(*a,**k): pass
  def setDockNestingEnabled(*a,**k): pass
  def setDockOptions(*a,**k): pass
  def setDocumentMode(*a,**k): pass
  def setIconSize(*a,**k): pass
  def setMenuBar(*a,**k): pass
  def setMenuWidget(*a,**k): pass
  def setStatusBar(*a,**k): pass
  def setTabPosition(*a,**k): pass
  def setTabShape(*a,**k): pass
  def setToolButtonStyle(*a,**k): pass
  def setUnifiedTitleAndToolBarOnMac(*a,**k): pass
  def splitDockWidget(*a,**k): pass
  def statusBar(*a,**k): pass
  def tabPosition(*a,**k): pass
  def tabShape(*a,**k): pass
  def tabifiedDockWidgets(*a,**k): pass
  def tabifyDockWidget(*a,**k): pass
  def toolBarArea(*a,**k): pass
  def toolBarBreak(*a,**k): pass
  def toolButtonStyle(*a,**k): pass
  def toolButtonStyleChanged(*a,**k): pass
  def unifiedTitleAndToolBarOnMac(*a,**k): pass

class QMdiSubWindow(QWidget):
  pass
  RubberBandMove = 8
  RubberBandResize = 4
  def aboutToActivate(*a,**k): pass
  def isShaded(*a,**k): pass
  def keyboardPageStep(*a,**k): pass
  def keyboardSingleStep(*a,**k): pass
  def mdiArea(*a,**k): pass
  def setKeyboardPageStep(*a,**k): pass
  def setKeyboardSingleStep(*a,**k): pass
  def setOption(*a,**k): pass
  def setSystemMenu(*a,**k): pass
  def setWidget(*a,**k): pass
  def showShaded(*a,**k): pass
  def showSystemMenu(*a,**k): pass
  def systemMenu(*a,**k): pass
  def testOption(*a,**k): pass
  def widget(*a,**k): pass
  def windowStateChanged(*a,**k): pass

class QMenu(QWidget):
  pass

  def aboutToHide(*a,**k): pass
  def aboutToShow(*a,**k): pass
  def actionAt(*a,**k): pass
  def actionGeometry(*a,**k): pass
  def activeAction(*a,**k): pass
  def addMenu(*a,**k): pass
  def addSeparator(*a,**k): pass
  def clear(*a,**k): pass
  def columnCount(*a,**k): pass
  def defaultAction(*a,**k): pass
  def exec_(*a,**k): pass
  def hideTearOffMenu(*a,**k): pass
  def hovered(*a,**k): pass
  def icon(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def insertMenu(*a,**k): pass
  def insertSeparator(*a,**k): pass
  def isEmpty(*a,**k): pass
  def isTearOffEnabled(*a,**k): pass
  def isTearOffMenuVisible(*a,**k): pass
  def menuAction(*a,**k): pass
  def popup(*a,**k): pass
  def separatorsCollapsible(*a,**k): pass
  def setActiveAction(*a,**k): pass
  def setDefaultAction(*a,**k): pass
  def setIcon(*a,**k): pass
  def setNoReplayFor(*a,**k): pass
  def setSeparatorsCollapsible(*a,**k): pass
  def setTearOffEnabled(*a,**k): pass
  def setTitle(*a,**k): pass
  def title(*a,**k): pass
  def triggered(*a,**k): pass

class QMenuBar(QWidget):
  pass

  def actionAt(*a,**k): pass
  def actionGeometry(*a,**k): pass
  def activeAction(*a,**k): pass
  def addMenu(*a,**k): pass
  def addSeparator(*a,**k): pass
  def clear(*a,**k): pass
  def cornerWidget(*a,**k): pass
  def hovered(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def insertMenu(*a,**k): pass
  def insertSeparator(*a,**k): pass
  def isDefaultUp(*a,**k): pass
  def isNativeMenuBar(*a,**k): pass
  def setActiveAction(*a,**k): pass
  def setCornerWidget(*a,**k): pass
  def setDefaultUp(*a,**k): pass
  def setNativeMenuBar(*a,**k): pass
  def triggered(*a,**k): pass

class QPrintPreviewWidget(QWidget):
  pass
  AllPagesView = 2
  CustomZoom = 0
  FacingPagesView = 1
  FitInView = 2
  FitToWidth = 1
  SinglePageView = 0
  def currentPage(*a,**k): pass
  def fitInView(*a,**k): pass
  def fitToWidth(*a,**k): pass
  def numPages(*a,**k): pass
  def orientation(*a,**k): pass
  def pageCount(*a,**k): pass
  def paintRequested(*a,**k): pass
  def previewChanged(*a,**k): pass
  def print_(*a,**k): pass
  def setAllPagesViewMode(*a,**k): pass
  def setCurrentPage(*a,**k): pass
  def setFacingPagesViewMode(*a,**k): pass
  def setLandscapeOrientation(*a,**k): pass
  def setOrientation(*a,**k): pass
  def setPortraitOrientation(*a,**k): pass
  def setSinglePageViewMode(*a,**k): pass
  def setViewMode(*a,**k): pass
  def setZoomFactor(*a,**k): pass
  def setZoomMode(*a,**k): pass
  def updatePreview(*a,**k): pass
  def viewMode(*a,**k): pass
  def zoomFactor(*a,**k): pass
  def zoomIn(*a,**k): pass
  def zoomMode(*a,**k): pass
  def zoomOut(*a,**k): pass

class QProgressBar(QWidget):
  pass
  BottomToTop = 1
  TopToBottom = 0
  def alignment(*a,**k): pass
  def format(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def invertedAppearance(*a,**k): pass
  def isTextVisible(*a,**k): pass
  def maximum(*a,**k): pass
  def minimum(*a,**k): pass
  def orientation(*a,**k): pass
  def reset(*a,**k): pass
  def setAlignment(*a,**k): pass
  def setFormat(*a,**k): pass
  def setInvertedAppearance(*a,**k): pass
  def setMaximum(*a,**k): pass
  def setMinimum(*a,**k): pass
  def setOrientation(*a,**k): pass
  def setRange(*a,**k): pass
  def setTextDirection(*a,**k): pass
  def setTextVisible(*a,**k): pass
  def setValue(*a,**k): pass
  def text(*a,**k): pass
  def textDirection(*a,**k): pass
  def value(*a,**k): pass
  def valueChanged(*a,**k): pass

class QRubberBand(QWidget):
  pass
  Line = 0
  Rectangle = 1
  def initStyleOption(*a,**k): pass
  def shape(*a,**k): pass

class QSizeGrip(QWidget):
  pass



class QSplashScreen(QWidget):
  pass

  def clearMessage(*a,**k): pass
  def drawContents(*a,**k): pass
  def finish(*a,**k): pass
  def messageChanged(*a,**k): pass
  def pixmap(*a,**k): pass
  def setPixmap(*a,**k): pass
  def showMessage(*a,**k): pass

class QSplitterHandle(QWidget):
  pass

  def closestLegalPosition(*a,**k): pass
  def moveSplitter(*a,**k): pass
  def opaqueResize(*a,**k): pass
  def orientation(*a,**k): pass
  def setOrientation(*a,**k): pass
  def splitter(*a,**k): pass

class QStatusBar(QWidget):
  pass

  def addPermanentWidget(*a,**k): pass
  def addWidget(*a,**k): pass
  def clearMessage(*a,**k): pass
  def currentMessage(*a,**k): pass
  def hideOrShow(*a,**k): pass
  def insertPermanentWidget(*a,**k): pass
  def insertWidget(*a,**k): pass
  def isSizeGripEnabled(*a,**k): pass
  def messageChanged(*a,**k): pass
  def reformat(*a,**k): pass
  def removeWidget(*a,**k): pass
  def setSizeGripEnabled(*a,**k): pass
  def showMessage(*a,**k): pass

class QTabBar(QWidget):
  pass
  LeftSide = 0
  RightSide = 1
  RoundedEast = 3
  RoundedNorth = 0
  RoundedSouth = 1
  RoundedWest = 2
  SelectLeftTab = 0
  SelectPreviousTab = 2
  SelectRightTab = 1
  TriangularEast = 7
  TriangularNorth = 4
  TriangularSouth = 5
  TriangularWest = 6
  def addTab(*a,**k): pass
  def count(*a,**k): pass
  def currentChanged(*a,**k): pass
  def currentIndex(*a,**k): pass
  def documentMode(*a,**k): pass
  def drawBase(*a,**k): pass
  def elideMode(*a,**k): pass
  def expanding(*a,**k): pass
  def iconSize(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def insertTab(*a,**k): pass
  def isMovable(*a,**k): pass
  def isTabEnabled(*a,**k): pass
  def moveTab(*a,**k): pass
  def removeTab(*a,**k): pass
  def selectionBehaviorOnRemove(*a,**k): pass
  def setCurrentIndex(*a,**k): pass
  def setDocumentMode(*a,**k): pass
  def setDrawBase(*a,**k): pass
  def setElideMode(*a,**k): pass
  def setExpanding(*a,**k): pass
  def setIconSize(*a,**k): pass
  def setMovable(*a,**k): pass
  def setSelectionBehaviorOnRemove(*a,**k): pass
  def setShape(*a,**k): pass
  def setTabButton(*a,**k): pass
  def setTabData(*a,**k): pass
  def setTabEnabled(*a,**k): pass
  def setTabIcon(*a,**k): pass
  def setTabText(*a,**k): pass
  def setTabTextColor(*a,**k): pass
  def setTabToolTip(*a,**k): pass
  def setTabWhatsThis(*a,**k): pass
  def setTabsClosable(*a,**k): pass
  def setUsesScrollButtons(*a,**k): pass
  def shape(*a,**k): pass
  def tabAt(*a,**k): pass
  def tabButton(*a,**k): pass
  def tabCloseRequested(*a,**k): pass
  def tabData(*a,**k): pass
  def tabIcon(*a,**k): pass
  def tabInserted(*a,**k): pass
  def tabLayoutChange(*a,**k): pass
  def tabMoved(*a,**k): pass
  def tabRect(*a,**k): pass
  def tabRemoved(*a,**k): pass
  def tabSizeHint(*a,**k): pass
  def tabText(*a,**k): pass
  def tabTextColor(*a,**k): pass
  def tabToolTip(*a,**k): pass
  def tabWhatsThis(*a,**k): pass
  def tabsClosable(*a,**k): pass
  def usesScrollButtons(*a,**k): pass

class QTabWidget(QWidget):
  pass
  East = 3
  North = 0
  Rounded = 0
  South = 1
  Triangular = 1
  West = 2
  def addTab(*a,**k): pass
  def clear(*a,**k): pass
  def cornerWidget(*a,**k): pass
  def count(*a,**k): pass
  def currentChanged(*a,**k): pass
  def currentIndex(*a,**k): pass
  def currentWidget(*a,**k): pass
  def documentMode(*a,**k): pass
  def elideMode(*a,**k): pass
  def iconSize(*a,**k): pass
  def indexOf(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def insertTab(*a,**k): pass
  def isMovable(*a,**k): pass
  def isTabEnabled(*a,**k): pass
  def removeTab(*a,**k): pass
  def setCornerWidget(*a,**k): pass
  def setCurrentIndex(*a,**k): pass
  def setCurrentWidget(*a,**k): pass
  def setDocumentMode(*a,**k): pass
  def setElideMode(*a,**k): pass
  def setIconSize(*a,**k): pass
  def setMovable(*a,**k): pass
  def setTabBar(*a,**k): pass
  def setTabEnabled(*a,**k): pass
  def setTabIcon(*a,**k): pass
  def setTabPosition(*a,**k): pass
  def setTabShape(*a,**k): pass
  def setTabText(*a,**k): pass
  def setTabToolTip(*a,**k): pass
  def setTabWhatsThis(*a,**k): pass
  def setTabsClosable(*a,**k): pass
  def setUsesScrollButtons(*a,**k): pass
  def tabBar(*a,**k): pass
  def tabCloseRequested(*a,**k): pass
  def tabIcon(*a,**k): pass
  def tabInserted(*a,**k): pass
  def tabPosition(*a,**k): pass
  def tabRemoved(*a,**k): pass
  def tabShape(*a,**k): pass
  def tabText(*a,**k): pass
  def tabToolTip(*a,**k): pass
  def tabWhatsThis(*a,**k): pass
  def tabsClosable(*a,**k): pass
  def usesScrollButtons(*a,**k): pass
  def widget(*a,**k): pass

class QWizardPage(QWidget):
  pass

  def buttonText(*a,**k): pass
  def cleanupPage(*a,**k): pass
  def completeChanged(*a,**k): pass
  def field(*a,**k): pass
  def initializePage(*a,**k): pass
  def isCommitPage(*a,**k): pass
  def isComplete(*a,**k): pass
  def isFinalPage(*a,**k): pass
  def nextId(*a,**k): pass
  def pixmap(*a,**k): pass
  def registerField(*a,**k): pass
  def setButtonText(*a,**k): pass
  def setCommitPage(*a,**k): pass
  def setField(*a,**k): pass
  def setFinalPage(*a,**k): pass
  def setPixmap(*a,**k): pass
  def setSubTitle(*a,**k): pass
  def setTitle(*a,**k): pass
  def subTitle(*a,**k): pass
  def title(*a,**k): pass
  def validatePage(*a,**k): pass
  def wizard(*a,**k): pass

class QWorkspace(QWidget):
  pass
  CreationOrder = 0
  StackingOrder = 1
  def activateNextWindow(*a,**k): pass
  def activatePreviousWindow(*a,**k): pass
  def activeWindow(*a,**k): pass
  def addWindow(*a,**k): pass
  def arrangeIcons(*a,**k): pass
  def background(*a,**k): pass
  def cascade(*a,**k): pass
  def closeActiveWindow(*a,**k): pass
  def closeAllWindows(*a,**k): pass
  def scrollBarsEnabled(*a,**k): pass
  def setActiveWindow(*a,**k): pass
  def setBackground(*a,**k): pass
  def setScrollBarsEnabled(*a,**k): pass
  def tile(*a,**k): pass
  def windowActivated(*a,**k): pass
  def windowList(*a,**k): pass

class QX11EmbedContainer(QWidget):
  pass
  Internal = 1
  InvalidWindowID = 2
  Unknown = 0
  def clientClosed(*a,**k): pass
  def clientIsEmbedded(*a,**k): pass
  def clientWinId(*a,**k): pass
  def discardClient(*a,**k): pass
  def embedClient(*a,**k): pass
  def error(*a,**k): pass

class QX11EmbedWidget(QWidget):
  pass
  Internal = 1
  InvalidWindowID = 2
  Unknown = 0
  def containerClosed(*a,**k): pass
  def containerWinId(*a,**k): pass
  def embedInto(*a,**k): pass
  def embedded(*a,**k): pass
  def error(*a,**k): pass

class QFontMetrics(object):
  pass

  def ascent(*a,**k): pass
  def averageCharWidth(*a,**k): pass
  def boundingRect(*a,**k): pass
  def boundingRectChar(*a,**k): pass
  def charWidth(*a,**k): pass
  def descent(*a,**k): pass
  def elidedText(*a,**k): pass
  def height(*a,**k): pass
  def inFont(*a,**k): pass
  def inFontUcs4(*a,**k): pass
  def leading(*a,**k): pass
  def leftBearing(*a,**k): pass
  def lineSpacing(*a,**k): pass
  def lineWidth(*a,**k): pass
  def maxWidth(*a,**k): pass
  def minLeftBearing(*a,**k): pass
  def minRightBearing(*a,**k): pass
  def overlinePos(*a,**k): pass
  def rightBearing(*a,**k): pass
  def size(*a,**k): pass
  def strikeOutPos(*a,**k): pass
  def tightBoundingRect(*a,**k): pass
  def underlinePos(*a,**k): pass
  def width(*a,**k): pass
  def widthChar(*a,**k): pass
  def xHeight(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QBrush(object):
  pass

  def color(*a,**k): pass
  def gradient(*a,**k): pass
  def isOpaque(*a,**k): pass
  def matrix(*a,**k): pass
  def setColor(*a,**k): pass
  def setMatrix(*a,**k): pass
  def setStyle(*a,**k): pass
  def setTexture(*a,**k): pass
  def setTextureImage(*a,**k): pass
  def setTransform(*a,**k): pass
  def style(*a,**k): pass
  def swap(*a,**k): pass
  def texture(*a,**k): pass
  def textureImage(*a,**k): pass
  def transform(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QColor(object):
  pass
  Cmyk = 3
  Hsl = 4
  Hsv = 2
  Invalid = 0
  Rgb = 1
  def allowX11ColorNames(*a,**k): pass
  def alpha(*a,**k): pass
  def alphaF(*a,**k): pass
  def black(*a,**k): pass
  def blackF(*a,**k): pass
  def blue(*a,**k): pass
  def blueF(*a,**k): pass
  def colorNames(*a,**k): pass
  def convertTo(*a,**k): pass
  def cyan(*a,**k): pass
  def cyanF(*a,**k): pass
  def dark(*a,**k): pass
  def darker(*a,**k): pass
  def fromCmyk(*a,**k): pass
  def fromCmykF(*a,**k): pass
  def fromHsl(*a,**k): pass
  def fromHslF(*a,**k): pass
  def fromHsv(*a,**k): pass
  def fromHsvF(*a,**k): pass
  def fromRgb(*a,**k): pass
  def fromRgbF(*a,**k): pass
  def fromRgba(*a,**k): pass
  def getCmyk(*a,**k): pass
  def getCmykF(*a,**k): pass
  def getHsl(*a,**k): pass
  def getHslF(*a,**k): pass
  def getHsv(*a,**k): pass
  def getHsvF(*a,**k): pass
  def getRgb(*a,**k): pass
  def getRgbF(*a,**k): pass
  def green(*a,**k): pass
  def greenF(*a,**k): pass
  def hslHue(*a,**k): pass
  def hslHueF(*a,**k): pass
  def hslSaturation(*a,**k): pass
  def hslSaturationF(*a,**k): pass
  def hsvHue(*a,**k): pass
  def hsvHueF(*a,**k): pass
  def hsvSaturation(*a,**k): pass
  def hsvSaturationF(*a,**k): pass
  def hue(*a,**k): pass
  def hueF(*a,**k): pass
  def isValid(*a,**k): pass
  def isValidColor(*a,**k): pass
  def light(*a,**k): pass
  def lighter(*a,**k): pass
  def lightness(*a,**k): pass
  def lightnessF(*a,**k): pass
  def magenta(*a,**k): pass
  def magentaF(*a,**k): pass
  def name(*a,**k): pass
  def red(*a,**k): pass
  def redF(*a,**k): pass
  def rgb(*a,**k): pass
  def rgba(*a,**k): pass
  def saturation(*a,**k): pass
  def saturationF(*a,**k): pass
  def setAllowX11ColorNames(*a,**k): pass
  def setAlpha(*a,**k): pass
  def setAlphaF(*a,**k): pass
  def setBlue(*a,**k): pass
  def setBlueF(*a,**k): pass
  def setCmyk(*a,**k): pass
  def setCmykF(*a,**k): pass
  def setGreen(*a,**k): pass
  def setGreenF(*a,**k): pass
  def setHsl(*a,**k): pass
  def setHslF(*a,**k): pass
  def setHsv(*a,**k): pass
  def setHsvF(*a,**k): pass
  def setNamedColor(*a,**k): pass
  def setRed(*a,**k): pass
  def setRedF(*a,**k): pass
  def setRgb(*a,**k): pass
  def setRgbF(*a,**k): pass
  def setRgba(*a,**k): pass
  def spec(*a,**k): pass
  def toCmyk(*a,**k): pass
  def toHsl(*a,**k): pass
  def toHsv(*a,**k): pass
  def toRgb(*a,**k): pass
  def value(*a,**k): pass
  def valueF(*a,**k): pass
  def yellow(*a,**k): pass
  def yellowF(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGradient(object):
  pass
  ConicalGradient = 2
  LinearGradient = 0
  LogicalMode = 0
  NoGradient = 3
  ObjectBoundingMode = 2
  PadSpread = 0
  RadialGradient = 1
  ReflectSpread = 1
  RepeatSpread = 2
  StretchToDeviceMode = 1
  def coordinateMode(*a,**k): pass
  def setColorAt(*a,**k): pass
  def setCoordinateMode(*a,**k): pass
  def setSpread(*a,**k): pass
  def setStops(*a,**k): pass
  def spread(*a,**k): pass
  def stops(*a,**k): pass
  def type(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QConicalGradient(QGradient):
  pass

  def angle(*a,**k): pass
  def center(*a,**k): pass
  def setAngle(*a,**k): pass
  def setCenter(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QLinearGradient(QGradient):
  pass

  def finalStop(*a,**k): pass
  def setFinalStop(*a,**k): pass
  def setStart(*a,**k): pass
  def start(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QRadialGradient(QGradient):
  pass

  def center(*a,**k): pass
  def centerRadius(*a,**k): pass
  def focalPoint(*a,**k): pass
  def focalRadius(*a,**k): pass
  def radius(*a,**k): pass
  def setCenter(*a,**k): pass
  def setCenterRadius(*a,**k): pass
  def setFocalPoint(*a,**k): pass
  def setFocalRadius(*a,**k): pass
  def setRadius(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QCursor(object):
  pass

  def bitmap(*a,**k): pass
  def hotSpot(*a,**k): pass
  def mask(*a,**k): pass
  def pixmap(*a,**k): pass
  def pos(*a,**k): pass
  def setPos(*a,**k): pass
  def setShape(*a,**k): pass
  def shape(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QDesktopServices(object):
  pass
  ApplicationsLocation = 3
  CacheLocation = 10
  DataLocation = 9
  DesktopLocation = 0
  DocumentsLocation = 1
  FontsLocation = 2
  HomeLocation = 8
  MoviesLocation = 5
  MusicLocation = 4
  PicturesLocation = 6
  TempLocation = 7
  def displayName(*a,**k): pass
  def openUrl(*a,**k): pass
  def setUrlHandler(*a,**k): pass
  def storageLocation(*a,**k): pass
  def unsetUrlHandler(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMimeSource(object):
  pass

  def encodedData(*a,**k): pass
  def format(*a,**k): pass
  def provides(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QDropEvent(PyQt4.QtCore.QEvent):
  pass

  def acceptProposedAction(*a,**k): pass
  def dropAction(*a,**k): pass
  def encodedData(*a,**k): pass
  def format(*a,**k): pass
  def keyboardModifiers(*a,**k): pass
  def mimeData(*a,**k): pass
  def mouseButtons(*a,**k): pass
  def pos(*a,**k): pass
  def possibleActions(*a,**k): pass
  def proposedAction(*a,**k): pass
  def provides(*a,**k): pass
  def setDropAction(*a,**k): pass
  def source(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QDragMoveEvent(QDropEvent):
  pass

  def answerRect(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QDragEnterEvent(QDragMoveEvent):
  pass


  def __init__(self, *args, **kwargs): pass


class QToolTip(object):
  pass

  def font(*a,**k): pass
  def hideText(*a,**k): pass
  def isVisible(*a,**k): pass
  def palette(*a,**k): pass
  def setFont(*a,**k): pass
  def setPalette(*a,**k): pass
  def showText(*a,**k): pass
  def text(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QFileIconProvider(object):
  pass
  Computer = 0
  Desktop = 1
  Drive = 4
  File = 6
  Folder = 5
  Network = 3
  Trashcan = 2
  def icon(*a,**k): pass
  def type(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QFont(object):
  pass
  AbsoluteSpacing = 1
  AllLowercase = 2
  AllUppercase = 1
  AnyStyle = 5
  Black = 87
  Bold = 75
  Capitalize = 4
  Condensed = 75
  Courier = 2
  Cursive = 6
  Decorative = 3
  DemiBold = 63
  Expanded = 125
  ExtraCondensed = 62
  ExtraExpanded = 150
  Fantasy = 8
  ForceIntegerMetrics = 1024
  ForceOutline = 16
  Helvetica = 0
  Light = 25
  MixedCase = 0
  Monospace = 7
  NoAntialias = 256
  NoFontMerging = 32768
  Normal = 50
  OldEnglish = 3
  OpenGLCompatible = 512
  PercentageSpacing = 0
  PreferAntialias = 128
  PreferBitmap = 2
  PreferDefault = 1
  PreferDefaultHinting = 0
  PreferDevice = 4
  PreferFullHinting = 3
  PreferMatch = 32
  PreferNoHinting = 1
  PreferOutline = 8
  PreferQuality = 64
  PreferVerticalHinting = 2
  SansSerif = 0
  SemiCondensed = 87
  SemiExpanded = 112
  Serif = 1
  SmallCaps = 3
  StyleItalic = 1
  StyleNormal = 0
  StyleOblique = 2
  System = 4
  Times = 1
  TypeWriter = 2
  UltraCondensed = 50
  UltraExpanded = 200
  Unstretched = 100
  def bold(*a,**k): pass
  def cacheStatistics(*a,**k): pass
  def capitalization(*a,**k): pass
  def cleanup(*a,**k): pass
  def defaultFamily(*a,**k): pass
  def exactMatch(*a,**k): pass
  def family(*a,**k): pass
  def fixedPitch(*a,**k): pass
  def fromString(*a,**k): pass
  def handle(*a,**k): pass
  def hintingPreference(*a,**k): pass
  def initialize(*a,**k): pass
  def insertSubstitution(*a,**k): pass
  def insertSubstitutions(*a,**k): pass
  def isCopyOf(*a,**k): pass
  def italic(*a,**k): pass
  def kerning(*a,**k): pass
  def key(*a,**k): pass
  def lastResortFamily(*a,**k): pass
  def lastResortFont(*a,**k): pass
  def letterSpacing(*a,**k): pass
  def letterSpacingType(*a,**k): pass
  def overline(*a,**k): pass
  def pixelSize(*a,**k): pass
  def pointSize(*a,**k): pass
  def pointSizeF(*a,**k): pass
  def rawMode(*a,**k): pass
  def rawName(*a,**k): pass
  def removeSubstitution(*a,**k): pass
  def resolve(*a,**k): pass
  def setBold(*a,**k): pass
  def setCapitalization(*a,**k): pass
  def setFamily(*a,**k): pass
  def setFixedPitch(*a,**k): pass
  def setHintingPreference(*a,**k): pass
  def setItalic(*a,**k): pass
  def setKerning(*a,**k): pass
  def setLetterSpacing(*a,**k): pass
  def setOverline(*a,**k): pass
  def setPixelSize(*a,**k): pass
  def setPointSize(*a,**k): pass
  def setPointSizeF(*a,**k): pass
  def setRawMode(*a,**k): pass
  def setRawName(*a,**k): pass
  def setStretch(*a,**k): pass
  def setStrikeOut(*a,**k): pass
  def setStyle(*a,**k): pass
  def setStyleHint(*a,**k): pass
  def setStyleName(*a,**k): pass
  def setStyleStrategy(*a,**k): pass
  def setUnderline(*a,**k): pass
  def setWeight(*a,**k): pass
  def setWordSpacing(*a,**k): pass
  def stretch(*a,**k): pass
  def strikeOut(*a,**k): pass
  def style(*a,**k): pass
  def styleHint(*a,**k): pass
  def styleName(*a,**k): pass
  def styleStrategy(*a,**k): pass
  def substitute(*a,**k): pass
  def substitutes(*a,**k): pass
  def substitutions(*a,**k): pass
  def toString(*a,**k): pass
  def underline(*a,**k): pass
  def weight(*a,**k): pass
  def wordSpacing(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QFontDatabase(object):
  pass
  Any = 0
  Arabic = 6
  Armenian = 4
  Bengali = 10
  Cyrillic = 3
  Devanagari = 9
  Georgian = 23
  Greek = 2
  Gujarati = 12
  Gurmukhi = 11
  Hebrew = 5
  Japanese = 27
  Kannada = 16
  Khmer = 24
  Korean = 28
  Lao = 20
  Latin = 1
  Malayalam = 17
  Myanmar = 22
  Nko = 33
  Ogham = 31
  Oriya = 13
  Other = 30
  Runic = 32
  SimplifiedChinese = 25
  Sinhala = 18
  Symbol = 30
  Syriac = 7
  Tamil = 14
  Telugu = 15
  Thaana = 8
  Thai = 19
  Tibetan = 21
  TraditionalChinese = 26
  Vietnamese = 29
  def addApplicationFont(*a,**k): pass
  def addApplicationFontFromData(*a,**k): pass
  def applicationFontFamilies(*a,**k): pass
  def bold(*a,**k): pass
  def families(*a,**k): pass
  def font(*a,**k): pass
  def isBitmapScalable(*a,**k): pass
  def isFixedPitch(*a,**k): pass
  def isScalable(*a,**k): pass
  def isSmoothlyScalable(*a,**k): pass
  def italic(*a,**k): pass
  def pointSizes(*a,**k): pass
  def removeAllApplicationFonts(*a,**k): pass
  def removeApplicationFont(*a,**k): pass
  def smoothSizes(*a,**k): pass
  def standardSizes(*a,**k): pass
  def styleString(*a,**k): pass
  def styles(*a,**k): pass
  def supportsThreadedFontRendering(*a,**k): pass
  def weight(*a,**k): pass
  def writingSystemName(*a,**k): pass
  def writingSystemSample(*a,**k): pass
  def writingSystems(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QFontInfo(object):
  pass

  def bold(*a,**k): pass
  def exactMatch(*a,**k): pass
  def family(*a,**k): pass
  def fixedPitch(*a,**k): pass
  def italic(*a,**k): pass
  def pixelSize(*a,**k): pass
  def pointSize(*a,**k): pass
  def pointSizeF(*a,**k): pass
  def rawMode(*a,**k): pass
  def style(*a,**k): pass
  def styleHint(*a,**k): pass
  def styleName(*a,**k): pass
  def weight(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMatrix(object):
  pass

  def det(*a,**k): pass
  def determinant(*a,**k): pass
  def dx(*a,**k): pass
  def dy(*a,**k): pass
  def inverted(*a,**k): pass
  def isIdentity(*a,**k): pass
  def isInvertible(*a,**k): pass
  def m11(*a,**k): pass
  def m12(*a,**k): pass
  def m21(*a,**k): pass
  def m22(*a,**k): pass
  def map(*a,**k): pass
  def mapRect(*a,**k): pass
  def mapToPolygon(*a,**k): pass
  def reset(*a,**k): pass
  def rotate(*a,**k): pass
  def scale(*a,**k): pass
  def setMatrix(*a,**k): pass
  def shear(*a,**k): pass
  def translate(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QFontMetricsF(object):
  pass

  def ascent(*a,**k): pass
  def averageCharWidth(*a,**k): pass
  def boundingRect(*a,**k): pass
  def boundingRectChar(*a,**k): pass
  def descent(*a,**k): pass
  def elidedText(*a,**k): pass
  def height(*a,**k): pass
  def inFont(*a,**k): pass
  def inFontUcs4(*a,**k): pass
  def leading(*a,**k): pass
  def leftBearing(*a,**k): pass
  def lineSpacing(*a,**k): pass
  def lineWidth(*a,**k): pass
  def maxWidth(*a,**k): pass
  def minLeftBearing(*a,**k): pass
  def minRightBearing(*a,**k): pass
  def overlinePos(*a,**k): pass
  def rightBearing(*a,**k): pass
  def size(*a,**k): pass
  def strikeOutPos(*a,**k): pass
  def tightBoundingRect(*a,**k): pass
  def underlinePos(*a,**k): pass
  def width(*a,**k): pass
  def widthChar(*a,**k): pass
  def xHeight(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGlyphRun(object):
  pass

  def clear(*a,**k): pass
  def glyphIndexes(*a,**k): pass
  def overline(*a,**k): pass
  def positions(*a,**k): pass
  def rawFont(*a,**k): pass
  def setGlyphIndexes(*a,**k): pass
  def setOverline(*a,**k): pass
  def setPositions(*a,**k): pass
  def setRawFont(*a,**k): pass
  def setStrikeOut(*a,**k): pass
  def setUnderline(*a,**k): pass
  def strikeOut(*a,**k): pass
  def underline(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QImageIOHandler(object):
  pass
  Animation = 12
  BackgroundColor = 13
  ClipRect = 1
  CompressionRatio = 5
  Description = 2
  Endianness = 11
  Gamma = 6
  IncrementalReading = 10
  Name = 8
  Quality = 7
  ScaledClipRect = 3
  ScaledSize = 4
  Size = 0
  SubType = 9
  def canRead(*a,**k): pass
  def currentImageNumber(*a,**k): pass
  def currentImageRect(*a,**k): pass
  def device(*a,**k): pass
  def format(*a,**k): pass
  def imageCount(*a,**k): pass
  def jumpToImage(*a,**k): pass
  def jumpToNextImage(*a,**k): pass
  def loopCount(*a,**k): pass
  def name(*a,**k): pass
  def nextImageDelay(*a,**k): pass
  def option(*a,**k): pass
  def read(*a,**k): pass
  def setDevice(*a,**k): pass
  def setFormat(*a,**k): pass
  def setOption(*a,**k): pass
  def supportsOption(*a,**k): pass
  def write(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QImageReader(object):
  pass
  DeviceError = 2
  FileNotFoundError = 1
  InvalidDataError = 4
  UnknownError = 0
  UnsupportedFormatError = 3
  def autoDetectImageFormat(*a,**k): pass
  def backgroundColor(*a,**k): pass
  def canRead(*a,**k): pass
  def clipRect(*a,**k): pass
  def currentImageNumber(*a,**k): pass
  def currentImageRect(*a,**k): pass
  def decideFormatFromContent(*a,**k): pass
  def device(*a,**k): pass
  def error(*a,**k): pass
  def errorString(*a,**k): pass
  def fileName(*a,**k): pass
  def format(*a,**k): pass
  def imageCount(*a,**k): pass
  def imageFormat(*a,**k): pass
  def jumpToImage(*a,**k): pass
  def jumpToNextImage(*a,**k): pass
  def loopCount(*a,**k): pass
  def nextImageDelay(*a,**k): pass
  def quality(*a,**k): pass
  def read(*a,**k): pass
  def scaledClipRect(*a,**k): pass
  def scaledSize(*a,**k): pass
  def setAutoDetectImageFormat(*a,**k): pass
  def setBackgroundColor(*a,**k): pass
  def setClipRect(*a,**k): pass
  def setDecideFormatFromContent(*a,**k): pass
  def setDevice(*a,**k): pass
  def setFileName(*a,**k): pass
  def setFormat(*a,**k): pass
  def setQuality(*a,**k): pass
  def setScaledClipRect(*a,**k): pass
  def setScaledSize(*a,**k): pass
  def size(*a,**k): pass
  def supportedImageFormats(*a,**k): pass
  def supportsAnimation(*a,**k): pass
  def supportsOption(*a,**k): pass
  def text(*a,**k): pass
  def textKeys(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QImageWriter(object):
  pass
  DeviceError = 1
  UnknownError = 0
  UnsupportedFormatError = 2
  def canWrite(*a,**k): pass
  def compression(*a,**k): pass
  def description(*a,**k): pass
  def device(*a,**k): pass
  def error(*a,**k): pass
  def errorString(*a,**k): pass
  def fileName(*a,**k): pass
  def format(*a,**k): pass
  def gamma(*a,**k): pass
  def quality(*a,**k): pass
  def setCompression(*a,**k): pass
  def setDescription(*a,**k): pass
  def setDevice(*a,**k): pass
  def setFileName(*a,**k): pass
  def setFormat(*a,**k): pass
  def setGamma(*a,**k): pass
  def setQuality(*a,**k): pass
  def setText(*a,**k): pass
  def supportedImageFormats(*a,**k): pass
  def supportsOption(*a,**k): pass
  def write(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QInputContextFactory(object):
  pass

  def create(*a,**k): pass
  def description(*a,**k): pass
  def displayName(*a,**k): pass
  def keys(*a,**k): pass
  def languages(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QItemSelection(object):
  pass

  def append(*a,**k): pass
  def clear(*a,**k): pass
  def contains(*a,**k): pass
  def count(*a,**k): pass
  def first(*a,**k): pass
  def indexOf(*a,**k): pass
  def indexes(*a,**k): pass
  def insert(*a,**k): pass
  def isEmpty(*a,**k): pass
  def last(*a,**k): pass
  def lastIndexOf(*a,**k): pass
  def merge(*a,**k): pass
  def move(*a,**k): pass
  def prepend(*a,**k): pass
  def removeAll(*a,**k): pass
  def removeAt(*a,**k): pass
  def replace(*a,**k): pass
  def select(*a,**k): pass
  def split(*a,**k): pass
  def swap(*a,**k): pass
  def takeAt(*a,**k): pass
  def takeFirst(*a,**k): pass
  def takeLast(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QItemSelectionRange(object):
  pass

  def bottom(*a,**k): pass
  def bottomRight(*a,**k): pass
  def contains(*a,**k): pass
  def height(*a,**k): pass
  def indexes(*a,**k): pass
  def intersect(*a,**k): pass
  def intersected(*a,**k): pass
  def intersects(*a,**k): pass
  def isEmpty(*a,**k): pass
  def isValid(*a,**k): pass
  def left(*a,**k): pass
  def model(*a,**k): pass
  def parent(*a,**k): pass
  def right(*a,**k): pass
  def top(*a,**k): pass
  def topLeft(*a,**k): pass
  def width(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QKeySequence(object):
  pass
  AddTab = 19
  Back = 13
  Bold = 27
  Close = 4
  Copy = 9
  Cut = 8
  Delete = 7
  DeleteEndOfLine = 60
  DeleteEndOfWord = 59
  DeleteStartOfWord = 58
  ExactMatch = 2
  Find = 22
  FindNext = 23
  FindPrevious = 24
  Forward = 14
  HelpContents = 1
  InsertLineSeparator = 62
  InsertParagraphSeparator = 61
  Italic = 28
  MoveToEndOfBlock = 41
  MoveToEndOfDocument = 43
  MoveToEndOfLine = 39
  MoveToNextChar = 30
  MoveToNextLine = 34
  MoveToNextPage = 36
  MoveToNextWord = 32
  MoveToPreviousChar = 31
  MoveToPreviousLine = 35
  MoveToPreviousPage = 37
  MoveToPreviousWord = 33
  MoveToStartOfBlock = 40
  MoveToStartOfDocument = 42
  MoveToStartOfLine = 38
  NativeText = 0
  New = 6
  NextChild = 20
  NoMatch = 0
  Open = 3
  PartialMatch = 1
  Paste = 10
  PortableText = 1
  Preferences = 64
  PreviousChild = 21
  Print = 18
  Quit = 65
  Redo = 12
  Refresh = 15
  Replace = 25
  Save = 5
  SaveAs = 63
  SelectAll = 26
  SelectEndOfBlock = 55
  SelectEndOfDocument = 57
  SelectEndOfLine = 53
  SelectNextChar = 44
  SelectNextLine = 48
  SelectNextPage = 50
  SelectNextWord = 46
  SelectPreviousChar = 45
  SelectPreviousLine = 49
  SelectPreviousPage = 51
  SelectPreviousWord = 47
  SelectStartOfBlock = 54
  SelectStartOfDocument = 56
  SelectStartOfLine = 52
  Underline = 29
  Undo = 11
  UnknownKey = 0
  WhatsThis = 2
  ZoomIn = 16
  ZoomOut = 17
  def count(*a,**k): pass
  def fromString(*a,**k): pass
  def isDetached(*a,**k): pass
  def isEmpty(*a,**k): pass
  def keyBindings(*a,**k): pass
  def matches(*a,**k): pass
  def mnemonic(*a,**k): pass
  def swap(*a,**k): pass
  def toString(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPalette(object):
  pass
  Active = 0
  All = 5
  AlternateBase = 16
  Background = 10
  Base = 9
  BrightText = 7
  Button = 1
  ButtonText = 8
  Current = 4
  Dark = 4
  Disabled = 1
  Foreground = 0
  Highlight = 12
  HighlightedText = 13
  Inactive = 2
  Light = 2
  Link = 14
  LinkVisited = 15
  Mid = 5
  Midlight = 3
  NColorGroups = 3
  NColorRoles = 20
  NoRole = 17
  Normal = 0
  Shadow = 11
  Text = 6
  ToolTipBase = 18
  ToolTipText = 19
  Window = 10
  WindowText = 0
  def alternateBase(*a,**k): pass
  def background(*a,**k): pass
  def base(*a,**k): pass
  def brightText(*a,**k): pass
  def brush(*a,**k): pass
  def button(*a,**k): pass
  def buttonText(*a,**k): pass
  def cacheKey(*a,**k): pass
  def color(*a,**k): pass
  def currentColorGroup(*a,**k): pass
  def dark(*a,**k): pass
  def foreground(*a,**k): pass
  def highlight(*a,**k): pass
  def highlightedText(*a,**k): pass
  def isBrushSet(*a,**k): pass
  def isCopyOf(*a,**k): pass
  def isEqual(*a,**k): pass
  def light(*a,**k): pass
  def link(*a,**k): pass
  def linkVisited(*a,**k): pass
  def mid(*a,**k): pass
  def midlight(*a,**k): pass
  def resolve(*a,**k): pass
  def serialNumber(*a,**k): pass
  def setBrush(*a,**k): pass
  def setColor(*a,**k): pass
  def setColorGroup(*a,**k): pass
  def setCurrentColorGroup(*a,**k): pass
  def shadow(*a,**k): pass
  def text(*a,**k): pass
  def toolTipBase(*a,**k): pass
  def toolTipText(*a,**k): pass
  def window(*a,**k): pass
  def windowText(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMatrix2x2(object):
  pass

  def copyDataTo(*a,**k): pass
  def data(*a,**k): pass
  def fill(*a,**k): pass
  def isIdentity(*a,**k): pass
  def setToIdentity(*a,**k): pass
  def transposed(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMatrix2x3(object):
  pass

  def copyDataTo(*a,**k): pass
  def data(*a,**k): pass
  def fill(*a,**k): pass
  def isIdentity(*a,**k): pass
  def setToIdentity(*a,**k): pass
  def transposed(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMatrix2x4(object):
  pass

  def copyDataTo(*a,**k): pass
  def data(*a,**k): pass
  def fill(*a,**k): pass
  def isIdentity(*a,**k): pass
  def setToIdentity(*a,**k): pass
  def transposed(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMatrix3x2(object):
  pass

  def copyDataTo(*a,**k): pass
  def data(*a,**k): pass
  def fill(*a,**k): pass
  def isIdentity(*a,**k): pass
  def setToIdentity(*a,**k): pass
  def transposed(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMatrix3x3(object):
  pass

  def copyDataTo(*a,**k): pass
  def data(*a,**k): pass
  def fill(*a,**k): pass
  def isIdentity(*a,**k): pass
  def setToIdentity(*a,**k): pass
  def transposed(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMatrix3x4(object):
  pass

  def copyDataTo(*a,**k): pass
  def data(*a,**k): pass
  def fill(*a,**k): pass
  def isIdentity(*a,**k): pass
  def setToIdentity(*a,**k): pass
  def transposed(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMatrix4x2(object):
  pass

  def copyDataTo(*a,**k): pass
  def data(*a,**k): pass
  def fill(*a,**k): pass
  def isIdentity(*a,**k): pass
  def setToIdentity(*a,**k): pass
  def transposed(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMatrix4x3(object):
  pass

  def copyDataTo(*a,**k): pass
  def data(*a,**k): pass
  def fill(*a,**k): pass
  def isIdentity(*a,**k): pass
  def setToIdentity(*a,**k): pass
  def transposed(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMatrix4x4(object):
  pass

  def column(*a,**k): pass
  def copyDataTo(*a,**k): pass
  def data(*a,**k): pass
  def determinant(*a,**k): pass
  def fill(*a,**k): pass
  def flipCoordinates(*a,**k): pass
  def frustum(*a,**k): pass
  def inverted(*a,**k): pass
  def isIdentity(*a,**k): pass
  def lookAt(*a,**k): pass
  def map(*a,**k): pass
  def mapRect(*a,**k): pass
  def mapVector(*a,**k): pass
  def normalMatrix(*a,**k): pass
  def optimize(*a,**k): pass
  def ortho(*a,**k): pass
  def perspective(*a,**k): pass
  def rotate(*a,**k): pass
  def row(*a,**k): pass
  def scale(*a,**k): pass
  def setColumn(*a,**k): pass
  def setRow(*a,**k): pass
  def setToIdentity(*a,**k): pass
  def toAffine(*a,**k): pass
  def toTransform(*a,**k): pass
  def translate(*a,**k): pass
  def transposed(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPaintEngine(object):
  pass
  AllDirty = 65535
  AllFeatures = -1
  AlphaBlend = 128
  Antialiasing = 1024
  BlendModes = 32768
  Blitter = 16
  BrushStroke = 2048
  ConicalGradientFill = 64
  ConstantOpacity = 4096
  ConvexMode = 2
  CoreGraphics = 3
  Direct3D = 11
  DirtyBackground = 16
  DirtyBackgroundMode = 32
  DirtyBrush = 2
  DirtyBrushOrigin = 4
  DirtyClipEnabled = 2048
  DirtyClipPath = 256
  DirtyClipRegion = 128
  DirtyCompositionMode = 1024
  DirtyFont = 8
  DirtyHints = 512
  DirtyOpacity = 4096
  DirtyPen = 1
  DirtyTransform = 64
  LinearGradientFill = 16
  MacPrinter = 4
  MaskedBrush = 8192
  MaxUser = 100
  ObjectBoundingModeGradients = 65536
  OddEvenMode = 0
  OpenGL = 7
  OpenGL2 = 14
  OpenVG = 13
  PaintBuffer = 15
  PaintOutsidePaintEvent = 536870912
  PainterPaths = 512
  PatternBrush = 8
  PatternTransform = 2
  Pdf = 12
  PerspectiveTransform = 16384
  Picture = 8
  PixmapTransform = 4
  PolylineMode = 3
  PorterDuff = 256
  PostScript = 6
  PrimitiveTransform = 1
  QWindowSystem = 5
  QuickDraw = 2
  RadialGradientFill = 32
  Raster = 10
  RasterOpModes = 131072
  SVG = 9
  User = 50
  WindingMode = 1
  Windows = 1
  X11 = 0
  def begin(*a,**k): pass
  def drawEllipse(*a,**k): pass
  def drawImage(*a,**k): pass
  def drawLines(*a,**k): pass
  def drawPath(*a,**k): pass
  def drawPixmap(*a,**k): pass
  def drawPoints(*a,**k): pass
  def drawPolygon(*a,**k): pass
  def drawRects(*a,**k): pass
  def drawTextItem(*a,**k): pass
  def drawTiledPixmap(*a,**k): pass
  def end(*a,**k): pass
  def hasFeature(*a,**k): pass
  def isActive(*a,**k): pass
  def paintDevice(*a,**k): pass
  def painter(*a,**k): pass
  def setActive(*a,**k): pass
  def setPaintDevice(*a,**k): pass
  def type(*a,**k): pass
  def updateState(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPaintEngineState(object):
  pass

  def backgroundBrush(*a,**k): pass
  def backgroundMode(*a,**k): pass
  def brush(*a,**k): pass
  def brushNeedsResolving(*a,**k): pass
  def brushOrigin(*a,**k): pass
  def clipOperation(*a,**k): pass
  def clipPath(*a,**k): pass
  def clipRegion(*a,**k): pass
  def compositionMode(*a,**k): pass
  def font(*a,**k): pass
  def isClipEnabled(*a,**k): pass
  def matrix(*a,**k): pass
  def opacity(*a,**k): pass
  def painter(*a,**k): pass
  def pen(*a,**k): pass
  def penNeedsResolving(*a,**k): pass
  def renderHints(*a,**k): pass
  def state(*a,**k): pass
  def transform(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPainter(object):
  pass
  Antialiasing = 1
  CompositionMode_Clear = 2
  CompositionMode_ColorBurn = 19
  CompositionMode_ColorDodge = 18
  CompositionMode_Darken = 16
  CompositionMode_Destination = 4
  CompositionMode_DestinationAtop = 10
  CompositionMode_DestinationIn = 6
  CompositionMode_DestinationOut = 8
  CompositionMode_DestinationOver = 1
  CompositionMode_Difference = 22
  CompositionMode_Exclusion = 23
  CompositionMode_HardLight = 20
  CompositionMode_Lighten = 17
  CompositionMode_Multiply = 13
  CompositionMode_Overlay = 15
  CompositionMode_Plus = 12
  CompositionMode_Screen = 14
  CompositionMode_SoftLight = 21
  CompositionMode_Source = 3
  CompositionMode_SourceAtop = 9
  CompositionMode_SourceIn = 5
  CompositionMode_SourceOut = 7
  CompositionMode_SourceOver = 0
  CompositionMode_Xor = 11
  HighQualityAntialiasing = 8
  NonCosmeticDefaultPen = 16
  OpaqueHint = 1
  RasterOp_NotSource = 30
  RasterOp_NotSourceAndDestination = 31
  RasterOp_NotSourceAndNotDestination = 27
  RasterOp_NotSourceOrNotDestination = 28
  RasterOp_NotSourceXorDestination = 29
  RasterOp_SourceAndDestination = 25
  RasterOp_SourceAndNotDestination = 32
  RasterOp_SourceOrDestination = 24
  RasterOp_SourceXorDestination = 26
  SmoothPixmapTransform = 4
  TextAntialiasing = 2
  def background(*a,**k): pass
  def backgroundMode(*a,**k): pass
  def begin(*a,**k): pass
  def beginNativePainting(*a,**k): pass
  def boundingRect(*a,**k): pass
  def brush(*a,**k): pass
  def brushOrigin(*a,**k): pass
  def clipBoundingRect(*a,**k): pass
  def clipPath(*a,**k): pass
  def clipRegion(*a,**k): pass
  def combinedMatrix(*a,**k): pass
  def combinedTransform(*a,**k): pass
  def compositionMode(*a,**k): pass
  def device(*a,**k): pass
  def deviceMatrix(*a,**k): pass
  def deviceTransform(*a,**k): pass
  def drawArc(*a,**k): pass
  def drawChord(*a,**k): pass
  def drawConvexPolygon(*a,**k): pass
  def drawEllipse(*a,**k): pass
  def drawGlyphRun(*a,**k): pass
  def drawImage(*a,**k): pass
  def drawLine(*a,**k): pass
  def drawLines(*a,**k): pass
  def drawPath(*a,**k): pass
  def drawPicture(*a,**k): pass
  def drawPie(*a,**k): pass
  def drawPixmap(*a,**k): pass
  def drawPixmapFragments(*a,**k): pass
  def drawPoint(*a,**k): pass
  def drawPoints(*a,**k): pass
  def drawPolygon(*a,**k): pass
  def drawPolyline(*a,**k): pass
  def drawRect(*a,**k): pass
  def drawRects(*a,**k): pass
  def drawRoundRect(*a,**k): pass
  def drawRoundedRect(*a,**k): pass
  def drawStaticText(*a,**k): pass
  def drawText(*a,**k): pass
  def drawTiledPixmap(*a,**k): pass
  def end(*a,**k): pass
  def endNativePainting(*a,**k): pass
  def eraseRect(*a,**k): pass
  def fillPath(*a,**k): pass
  def fillRect(*a,**k): pass
  def font(*a,**k): pass
  def fontInfo(*a,**k): pass
  def fontMetrics(*a,**k): pass
  def hasClipping(*a,**k): pass
  def initFrom(*a,**k): pass
  def isActive(*a,**k): pass
  def layoutDirection(*a,**k): pass
  def matrix(*a,**k): pass
  def matrixEnabled(*a,**k): pass
  def opacity(*a,**k): pass
  def paintEngine(*a,**k): pass
  def pen(*a,**k): pass
  def redirected(*a,**k): pass
  def renderHints(*a,**k): pass
  def resetMatrix(*a,**k): pass
  def resetTransform(*a,**k): pass
  def restore(*a,**k): pass
  def restoreRedirected(*a,**k): pass
  def rotate(*a,**k): pass
  def save(*a,**k): pass
  def scale(*a,**k): pass
  def setBackground(*a,**k): pass
  def setBackgroundMode(*a,**k): pass
  def setBrush(*a,**k): pass
  def setBrushOrigin(*a,**k): pass
  def setClipPath(*a,**k): pass
  def setClipRect(*a,**k): pass
  def setClipRegion(*a,**k): pass
  def setClipping(*a,**k): pass
  def setCompositionMode(*a,**k): pass
  def setFont(*a,**k): pass
  def setLayoutDirection(*a,**k): pass
  def setMatrix(*a,**k): pass
  def setMatrixEnabled(*a,**k): pass
  def setOpacity(*a,**k): pass
  def setPen(*a,**k): pass
  def setRedirected(*a,**k): pass
  def setRenderHint(*a,**k): pass
  def setRenderHints(*a,**k): pass
  def setTransform(*a,**k): pass
  def setViewTransformEnabled(*a,**k): pass
  def setViewport(*a,**k): pass
  def setWindow(*a,**k): pass
  def setWorldMatrix(*a,**k): pass
  def setWorldMatrixEnabled(*a,**k): pass
  def setWorldTransform(*a,**k): pass
  def shear(*a,**k): pass
  def strokePath(*a,**k): pass
  def testRenderHint(*a,**k): pass
  def transform(*a,**k): pass
  def translate(*a,**k): pass
  def viewTransformEnabled(*a,**k): pass
  def viewport(*a,**k): pass
  def window(*a,**k): pass
  def worldMatrix(*a,**k): pass
  def worldMatrixEnabled(*a,**k): pass
  def worldTransform(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QStylePainter(QPainter):
  pass

  def drawComplexControl(*a,**k): pass
  def drawControl(*a,**k): pass
  def drawItemPixmap(*a,**k): pass
  def drawItemText(*a,**k): pass
  def drawPrimitive(*a,**k): pass
  def style(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPainterPath(object):
  pass
  CurveToDataElement = 3
  CurveToElement = 2
  LineToElement = 1
  MoveToElement = 0
  def addEllipse(*a,**k): pass
  def addPath(*a,**k): pass
  def addPolygon(*a,**k): pass
  def addRect(*a,**k): pass
  def addRegion(*a,**k): pass
  def addRoundRect(*a,**k): pass
  def addRoundedRect(*a,**k): pass
  def addText(*a,**k): pass
  def angleAtPercent(*a,**k): pass
  def arcMoveTo(*a,**k): pass
  def arcTo(*a,**k): pass
  def boundingRect(*a,**k): pass
  def closeSubpath(*a,**k): pass
  def connectPath(*a,**k): pass
  def contains(*a,**k): pass
  def controlPointRect(*a,**k): pass
  def cubicTo(*a,**k): pass
  def currentPosition(*a,**k): pass
  def elementAt(*a,**k): pass
  def elementCount(*a,**k): pass
  def fillRule(*a,**k): pass
  def intersected(*a,**k): pass
  def intersects(*a,**k): pass
  def isEmpty(*a,**k): pass
  def length(*a,**k): pass
  def lineTo(*a,**k): pass
  def moveTo(*a,**k): pass
  def percentAtLength(*a,**k): pass
  def pointAtPercent(*a,**k): pass
  def quadTo(*a,**k): pass
  def setElementPositionAt(*a,**k): pass
  def setFillRule(*a,**k): pass
  def simplified(*a,**k): pass
  def slopeAtPercent(*a,**k): pass
  def subtracted(*a,**k): pass
  def subtractedInverted(*a,**k): pass
  def swap(*a,**k): pass
  def toFillPolygon(*a,**k): pass
  def toFillPolygons(*a,**k): pass
  def toReversed(*a,**k): pass
  def toSubpathPolygons(*a,**k): pass
  def translate(*a,**k): pass
  def translated(*a,**k): pass
  def united(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPainterPathStroker(object):
  pass

  def capStyle(*a,**k): pass
  def createStroke(*a,**k): pass
  def curveThreshold(*a,**k): pass
  def dashOffset(*a,**k): pass
  def dashPattern(*a,**k): pass
  def joinStyle(*a,**k): pass
  def miterLimit(*a,**k): pass
  def setCapStyle(*a,**k): pass
  def setCurveThreshold(*a,**k): pass
  def setDashOffset(*a,**k): pass
  def setDashPattern(*a,**k): pass
  def setJoinStyle(*a,**k): pass
  def setMiterLimit(*a,**k): pass
  def setWidth(*a,**k): pass
  def width(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPen(object):
  pass

  def brush(*a,**k): pass
  def capStyle(*a,**k): pass
  def color(*a,**k): pass
  def dashOffset(*a,**k): pass
  def dashPattern(*a,**k): pass
  def isCosmetic(*a,**k): pass
  def isSolid(*a,**k): pass
  def joinStyle(*a,**k): pass
  def miterLimit(*a,**k): pass
  def setBrush(*a,**k): pass
  def setCapStyle(*a,**k): pass
  def setColor(*a,**k): pass
  def setCosmetic(*a,**k): pass
  def setDashOffset(*a,**k): pass
  def setDashPattern(*a,**k): pass
  def setJoinStyle(*a,**k): pass
  def setMiterLimit(*a,**k): pass
  def setStyle(*a,**k): pass
  def setWidth(*a,**k): pass
  def setWidthF(*a,**k): pass
  def style(*a,**k): pass
  def swap(*a,**k): pass
  def width(*a,**k): pass
  def widthF(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPictureIO(object):
  pass

  def defineIOHandler(*a,**k): pass
  def description(*a,**k): pass
  def fileName(*a,**k): pass
  def format(*a,**k): pass
  def gamma(*a,**k): pass
  def inputFormats(*a,**k): pass
  def ioDevice(*a,**k): pass
  def outputFormats(*a,**k): pass
  def parameters(*a,**k): pass
  def picture(*a,**k): pass
  def pictureFormat(*a,**k): pass
  def quality(*a,**k): pass
  def read(*a,**k): pass
  def setDescription(*a,**k): pass
  def setFileName(*a,**k): pass
  def setFormat(*a,**k): pass
  def setGamma(*a,**k): pass
  def setIODevice(*a,**k): pass
  def setParameters(*a,**k): pass
  def setPicture(*a,**k): pass
  def setQuality(*a,**k): pass
  def setStatus(*a,**k): pass
  def status(*a,**k): pass
  def write(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPixmapCache(object):
  pass

  def cacheLimit(*a,**k): pass
  def clear(*a,**k): pass
  def find(*a,**k): pass
  def insert(*a,**k): pass
  def remove(*a,**k): pass
  def replace(*a,**k): pass
  def setCacheLimit(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPolygon(object):
  pass

  def append(*a,**k): pass
  def at(*a,**k): pass
  def boundingRect(*a,**k): pass
  def clear(*a,**k): pass
  def contains(*a,**k): pass
  def containsPoint(*a,**k): pass
  def count(*a,**k): pass
  def data(*a,**k): pass
  def fill(*a,**k): pass
  def first(*a,**k): pass
  def indexOf(*a,**k): pass
  def insert(*a,**k): pass
  def intersected(*a,**k): pass
  def isEmpty(*a,**k): pass
  def last(*a,**k): pass
  def lastIndexOf(*a,**k): pass
  def mid(*a,**k): pass
  def point(*a,**k): pass
  def prepend(*a,**k): pass
  def putPoints(*a,**k): pass
  def remove(*a,**k): pass
  def replace(*a,**k): pass
  def setPoint(*a,**k): pass
  def setPoints(*a,**k): pass
  def size(*a,**k): pass
  def subtracted(*a,**k): pass
  def swap(*a,**k): pass
  def translate(*a,**k): pass
  def translated(*a,**k): pass
  def united(*a,**k): pass
  def value(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPolygonF(object):
  pass

  def append(*a,**k): pass
  def at(*a,**k): pass
  def boundingRect(*a,**k): pass
  def clear(*a,**k): pass
  def contains(*a,**k): pass
  def containsPoint(*a,**k): pass
  def count(*a,**k): pass
  def data(*a,**k): pass
  def fill(*a,**k): pass
  def first(*a,**k): pass
  def indexOf(*a,**k): pass
  def insert(*a,**k): pass
  def intersected(*a,**k): pass
  def isClosed(*a,**k): pass
  def isEmpty(*a,**k): pass
  def last(*a,**k): pass
  def lastIndexOf(*a,**k): pass
  def mid(*a,**k): pass
  def prepend(*a,**k): pass
  def remove(*a,**k): pass
  def replace(*a,**k): pass
  def size(*a,**k): pass
  def subtracted(*a,**k): pass
  def swap(*a,**k): pass
  def toPolygon(*a,**k): pass
  def translate(*a,**k): pass
  def translated(*a,**k): pass
  def united(*a,**k): pass
  def value(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPrintEngine(object):
  pass
  PPK_CollateCopies = 0
  PPK_ColorMode = 1
  PPK_CopyCount = 25
  PPK_Creator = 2
  PPK_CustomBase = 65280
  PPK_CustomPaperSize = 23
  PPK_DocumentName = 3
  PPK_Duplex = 21
  PPK_FontEmbedding = 19
  PPK_FullPage = 4
  PPK_NumberOfCopies = 5
  PPK_Orientation = 6
  PPK_OutputFileName = 7
  PPK_PageMargins = 24
  PPK_PageOrder = 8
  PPK_PageRect = 9
  PPK_PageSize = 10
  PPK_PaperRect = 11
  PPK_PaperSize = 10
  PPK_PaperSource = 12
  PPK_PaperSources = 22
  PPK_PrinterName = 13
  PPK_PrinterProgram = 14
  PPK_Resolution = 15
  PPK_SelectionOption = 16
  PPK_SupportedResolutions = 17
  PPK_SupportsMultipleCopies = 26
  PPK_SuppressSystemPrintStatus = 20
  PPK_WindowsPageSize = 18
  def abort(*a,**k): pass
  def metric(*a,**k): pass
  def newPage(*a,**k): pass
  def printerState(*a,**k): pass
  def property(*a,**k): pass
  def setProperty(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPrinterInfo(object):
  pass

  def availablePrinters(*a,**k): pass
  def defaultPrinter(*a,**k): pass
  def isDefault(*a,**k): pass
  def isNull(*a,**k): pass
  def printerName(*a,**k): pass
  def supportedPaperSizes(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextObjectInterface(object):
  pass

  def drawObject(*a,**k): pass
  def intrinsicSize(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPyTextObject(PyQt4.QtCore.QObject):
  pass

  def drawObject(*a,**k): pass
  def intrinsicSize(*a,**k): pass

class QQuaternion(object):
  pass

  def conjugate(*a,**k): pass
  def fromAxisAndAngle(*a,**k): pass
  def isIdentity(*a,**k): pass
  def isNull(*a,**k): pass
  def length(*a,**k): pass
  def lengthSquared(*a,**k): pass
  def nlerp(*a,**k): pass
  def normalize(*a,**k): pass
  def normalized(*a,**k): pass
  def rotatedVector(*a,**k): pass
  def scalar(*a,**k): pass
  def setScalar(*a,**k): pass
  def setVector(*a,**k): pass
  def setX(*a,**k): pass
  def setY(*a,**k): pass
  def setZ(*a,**k): pass
  def slerp(*a,**k): pass
  def toVector4D(*a,**k): pass
  def vector(*a,**k): pass
  def x(*a,**k): pass
  def y(*a,**k): pass
  def z(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QRawFont(object):
  pass
  PixelAntialiasing = 0
  SubPixelAntialiasing = 1
  def advancesForGlyphIndexes(*a,**k): pass
  def alphaMapForGlyph(*a,**k): pass
  def ascent(*a,**k): pass
  def averageCharWidth(*a,**k): pass
  def descent(*a,**k): pass
  def familyName(*a,**k): pass
  def fontTable(*a,**k): pass
  def fromFont(*a,**k): pass
  def glyphIndexesForString(*a,**k): pass
  def hintingPreference(*a,**k): pass
  def isValid(*a,**k): pass
  def leading(*a,**k): pass
  def loadFromData(*a,**k): pass
  def loadFromFile(*a,**k): pass
  def maxCharWidth(*a,**k): pass
  def pathForGlyph(*a,**k): pass
  def pixelSize(*a,**k): pass
  def setPixelSize(*a,**k): pass
  def style(*a,**k): pass
  def styleName(*a,**k): pass
  def supportedWritingSystems(*a,**k): pass
  def supportsCharacter(*a,**k): pass
  def unitsPerEm(*a,**k): pass
  def weight(*a,**k): pass
  def xHeight(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QRegion(object):
  pass
  Ellipse = 1
  Rectangle = 0
  def boundingRect(*a,**k): pass
  def contains(*a,**k): pass
  def eor(*a,**k): pass
  def intersect(*a,**k): pass
  def intersected(*a,**k): pass
  def intersects(*a,**k): pass
  def isEmpty(*a,**k): pass
  def numRects(*a,**k): pass
  def rectCount(*a,**k): pass
  def rects(*a,**k): pass
  def subtract(*a,**k): pass
  def subtracted(*a,**k): pass
  def swap(*a,**k): pass
  def translate(*a,**k): pass
  def translated(*a,**k): pass
  def unite(*a,**k): pass
  def united(*a,**k): pass
  def xored(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QSizePolicy(object):
  pass
  ButtonBox = 2
  CheckBox = 4
  ComboBox = 8
  DefaultType = 1
  ExpandFlag = 2
  Expanding = 7
  Fixed = 0
  Frame = 16
  GroupBox = 32
  GrowFlag = 1
  IgnoreFlag = 8
  Ignored = 13
  Label = 64
  Line = 128
  LineEdit = 256
  Maximum = 4
  Minimum = 1
  MinimumExpanding = 3
  Preferred = 5
  PushButton = 512
  RadioButton = 1024
  ShrinkFlag = 4
  Slider = 2048
  SpinBox = 4096
  TabWidget = 8192
  ToolButton = 16384
  def controlType(*a,**k): pass
  def expandingDirections(*a,**k): pass
  def hasHeightForWidth(*a,**k): pass
  def hasWidthForHeight(*a,**k): pass
  def horizontalPolicy(*a,**k): pass
  def horizontalStretch(*a,**k): pass
  def setControlType(*a,**k): pass
  def setHeightForWidth(*a,**k): pass
  def setHorizontalPolicy(*a,**k): pass
  def setHorizontalStretch(*a,**k): pass
  def setVerticalPolicy(*a,**k): pass
  def setVerticalStretch(*a,**k): pass
  def setWidthForHeight(*a,**k): pass
  def transpose(*a,**k): pass
  def verticalPolicy(*a,**k): pass
  def verticalStretch(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QStaticText(object):
  pass
  AggressiveCaching = 1
  ModerateCaching = 0
  def performanceHint(*a,**k): pass
  def prepare(*a,**k): pass
  def setPerformanceHint(*a,**k): pass
  def setText(*a,**k): pass
  def setTextFormat(*a,**k): pass
  def setTextOption(*a,**k): pass
  def setTextWidth(*a,**k): pass
  def size(*a,**k): pass
  def text(*a,**k): pass
  def textFormat(*a,**k): pass
  def textOption(*a,**k): pass
  def textWidth(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QStyleFactory(object):
  pass

  def create(*a,**k): pass
  def keys(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QStyleHintReturn(object):
  pass
  SH_Default = 61440
  SH_Mask = 61441
  SH_Variant = 61442
  Type = 61440
  Version = 1

  def __init__(self, *args, **kwargs): pass


class QStyleHintReturnMask(QStyleHintReturn):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleHintReturnVariant(QStyleHintReturn):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOption(object):
  pass
  SO_Button = 2
  SO_ComboBox = 983044
  SO_Complex = 983040
  SO_ComplexCustomBase = 251658240
  SO_CustomBase = 3840
  SO_Default = 0
  SO_DockWidget = 10
  SO_FocusRect = 1
  SO_Frame = 5
  SO_GraphicsItem = 17
  SO_GroupBox = 983047
  SO_Header = 8
  SO_MenuItem = 4
  SO_ProgressBar = 6
  SO_Q3DockWindow = 9
  SO_Q3ListView = 983045
  SO_Q3ListViewItem = 11
  SO_RubberBand = 15
  SO_SizeGrip = 983048
  SO_Slider = 983041
  SO_SpinBox = 983042
  SO_Tab = 3
  SO_TabBarBase = 14
  SO_TabWidgetFrame = 13
  SO_TitleBar = 983046
  SO_ToolBar = 16
  SO_ToolBox = 7
  SO_ToolButton = 983043
  SO_ViewItem = 12
  Type = 0
  Version = 1
  def init(*a,**k): pass
  def initFrom(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QStyleOptionButton(QStyleOption):
  pass
  AutoDefaultButton = 8
  CommandLinkButton = 16
  DefaultButton = 4
  Flat = 1
  HasMenu = 2

  def __init__(self, *args, **kwargs): pass


class QStyleOptionTabWidgetFrame(QStyleOption):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionTabWidgetFrameV2(QStyleOptionTabWidgetFrame):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionComplex(QStyleOption):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionComboBox(QStyleOptionComplex):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionGroupBox(QStyleOptionComplex):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionSizeGrip(QStyleOptionComplex):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionSlider(QStyleOptionComplex):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionSpinBox(QStyleOptionComplex):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionTitleBar(QStyleOptionComplex):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionToolButton(QStyleOptionComplex):
  pass
  Arrow = 1
  HasMenu = 16
  Menu = 4
  MenuButtonPopup = 4
  PopupDelay = 8

  def __init__(self, *args, **kwargs): pass


class QStyleOptionDockWidget(QStyleOption):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionDockWidgetV2(QStyleOptionDockWidget):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionFocusRect(QStyleOption):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionFrame(QStyleOption):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionFrameV2(QStyleOptionFrame):
  pass
  Flat = 1

  def __init__(self, *args, **kwargs): pass


class QStyleOptionFrameV3(QStyleOptionFrameV2):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionGraphicsItem(QStyleOption):
  pass

  def levelOfDetailFromTransform(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QStyleOptionHeader(QStyleOption):
  pass
  Beginning = 0
  End = 2
  Middle = 1
  NextAndPreviousAreSelected = 3
  NextIsSelected = 1
  NotAdjacent = 0
  OnlyOneSection = 3
  PreviousIsSelected = 2
  SortDown = 2
  SortUp = 1

  def __init__(self, *args, **kwargs): pass


class QStyleOptionMenuItem(QStyleOption):
  pass
  DefaultItem = 1
  EmptyArea = 7
  Exclusive = 1
  Margin = 6
  NonExclusive = 2
  Normal = 0
  NotCheckable = 0
  Scroller = 4
  Separator = 2
  SubMenu = 3
  TearOff = 5

  def __init__(self, *args, **kwargs): pass


class QStyleOptionProgressBar(QStyleOption):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionProgressBarV2(QStyleOptionProgressBar):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionRubberBand(QStyleOption):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionTab(QStyleOption):
  pass
  Beginning = 0
  End = 2
  LeftCornerWidget = 1
  Middle = 1
  NextIsSelected = 1
  NoCornerWidgets = 0
  NotAdjacent = 0
  OnlyOneTab = 3
  PreviousIsSelected = 2
  RightCornerWidget = 2

  def __init__(self, *args, **kwargs): pass


class QStyleOptionTabV2(QStyleOptionTab):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionTabV3(QStyleOptionTabV2):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionTabBarBase(QStyleOption):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionTabBarBaseV2(QStyleOptionTabBarBase):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionToolBar(QStyleOption):
  pass
  Beginning = 0
  End = 2
  Middle = 1
  Movable = 1
  OnlyOne = 3

  def __init__(self, *args, **kwargs): pass


class QStyleOptionToolBox(QStyleOption):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionToolBoxV2(QStyleOptionToolBox):
  pass
  Beginning = 0
  End = 2
  Middle = 1
  NextIsSelected = 1
  NotAdjacent = 0
  OnlyOneTab = 3
  PreviousIsSelected = 2

  def __init__(self, *args, **kwargs): pass


class QStyleOptionViewItem(QStyleOption):
  pass
  Bottom = 3
  Left = 0
  Right = 1
  Top = 2

  def __init__(self, *args, **kwargs): pass


class QStyleOptionViewItemV2(QStyleOptionViewItem):
  pass
  Alternate = 2
  HasCheckIndicator = 4
  HasDecoration = 16
  HasDisplay = 8
  WrapText = 1

  def __init__(self, *args, **kwargs): pass


class QStyleOptionViewItemV3(QStyleOptionViewItemV2):
  pass


  def __init__(self, *args, **kwargs): pass


class QStyleOptionViewItemV4(QStyleOptionViewItemV3):
  pass
  Beginning = 1
  End = 3
  Invalid = 0
  Middle = 2
  OnlyOne = 4

  def __init__(self, *args, **kwargs): pass


class QTextLine(object):
  pass
  CursorBetweenCharacters = 0
  CursorOnCharacter = 1
  Leading = 0
  Trailing = 1
  def ascent(*a,**k): pass
  def cursorToX(*a,**k): pass
  def descent(*a,**k): pass
  def draw(*a,**k): pass
  def height(*a,**k): pass
  def horizontalAdvance(*a,**k): pass
  def isValid(*a,**k): pass
  def leading(*a,**k): pass
  def leadingIncluded(*a,**k): pass
  def lineNumber(*a,**k): pass
  def naturalTextRect(*a,**k): pass
  def naturalTextWidth(*a,**k): pass
  def position(*a,**k): pass
  def rect(*a,**k): pass
  def setLeadingIncluded(*a,**k): pass
  def setLineWidth(*a,**k): pass
  def setNumColumns(*a,**k): pass
  def setPosition(*a,**k): pass
  def textLength(*a,**k): pass
  def textStart(*a,**k): pass
  def width(*a,**k): pass
  def x(*a,**k): pass
  def xToCursor(*a,**k): pass
  def y(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTableWidgetSelectionRange(object):
  pass

  def bottomRow(*a,**k): pass
  def columnCount(*a,**k): pass
  def leftColumn(*a,**k): pass
  def rightColumn(*a,**k): pass
  def rowCount(*a,**k): pass
  def topRow(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextFormat(object):
  pass
  AnchorHref = 8241
  AnchorName = 8242
  BackgroundBrush = 2080
  BackgroundImageUrl = 2083
  BlockAlignment = 4112
  BlockBottomMargin = 4145
  BlockFormat = 1
  BlockIndent = 4160
  BlockLeftMargin = 4146
  BlockNonBreakableLines = 4176
  BlockRightMargin = 4147
  BlockTopMargin = 4144
  BlockTrailingHorizontalRulerWidth = 4192
  CharFormat = 2
  CssFloat = 2048
  FirstFontProperty = 8160
  FontCapitalization = 8160
  FontFamily = 8192
  FontFixedPitch = 8200
  FontHintingPreference = 8166
  FontItalic = 8196
  FontKerning = 8165
  FontLetterSpacing = 8161
  FontOverline = 8198
  FontPixelSize = 8201
  FontPointSize = 8193
  FontSizeAdjustment = 8194
  FontSizeIncrement = 8194
  FontStrikeOut = 8199
  FontStyleHint = 8163
  FontStyleStrategy = 8164
  FontUnderline = 8197
  FontWeight = 8195
  FontWordSpacing = 8162
  ForegroundBrush = 2081
  FrameBorder = 16384
  FrameBorderBrush = 16393
  FrameBorderStyle = 16400
  FrameBottomMargin = 16390
  FrameFormat = 5
  FrameHeight = 16388
  FrameLeftMargin = 16391
  FrameMargin = 16385
  FramePadding = 16386
  FrameRightMargin = 16392
  FrameTopMargin = 16389
  FrameWidth = 16387
  FullWidthSelection = 24576
  ImageHeight = 20497
  ImageName = 20480
  ImageObject = 1
  ImageWidth = 20496
  InvalidFormat = -1
  IsAnchor = 8240
  LastFontProperty = 8201
  LayoutDirection = 2049
  LineHeight = 4168
  LineHeightType = 4169
  ListFormat = 3
  ListIndent = 12289
  ListNumberPrefix = 12290
  ListNumberSuffix = 12291
  ListStyle = 12288
  NoObject = 0
  ObjectIndex = 0
  ObjectType = 12032
  OutlinePen = 2064
  PageBreakPolicy = 28672
  PageBreak_AlwaysAfter = 16
  PageBreak_AlwaysBefore = 1
  PageBreak_Auto = 0
  TabPositions = 4149
  TableCellBottomPadding = 18451
  TableCellColumnSpan = 18449
  TableCellLeftPadding = 18452
  TableCellObject = 3
  TableCellPadding = 16643
  TableCellRightPadding = 18453
  TableCellRowSpan = 18448
  TableCellSpacing = 16642
  TableCellTopPadding = 18450
  TableColumnWidthConstraints = 16641
  TableColumns = 16640
  TableFormat = 4
  TableHeaderRowCount = 16644
  TableObject = 2
  TextIndent = 4148
  TextOutline = 8226
  TextToolTip = 8228
  TextUnderlineColor = 8208
  TextUnderlineStyle = 8227
  TextVerticalAlignment = 8225
  UserFormat = 100
  UserObject = 4096
  UserProperty = 1048576
  def background(*a,**k): pass
  def boolProperty(*a,**k): pass
  def brushProperty(*a,**k): pass
  def clearBackground(*a,**k): pass
  def clearForeground(*a,**k): pass
  def clearProperty(*a,**k): pass
  def colorProperty(*a,**k): pass
  def doubleProperty(*a,**k): pass
  def foreground(*a,**k): pass
  def hasProperty(*a,**k): pass
  def intProperty(*a,**k): pass
  def isBlockFormat(*a,**k): pass
  def isCharFormat(*a,**k): pass
  def isFrameFormat(*a,**k): pass
  def isImageFormat(*a,**k): pass
  def isListFormat(*a,**k): pass
  def isTableCellFormat(*a,**k): pass
  def isTableFormat(*a,**k): pass
  def isValid(*a,**k): pass
  def layoutDirection(*a,**k): pass
  def lengthProperty(*a,**k): pass
  def lengthVectorProperty(*a,**k): pass
  def merge(*a,**k): pass
  def objectIndex(*a,**k): pass
  def objectType(*a,**k): pass
  def penProperty(*a,**k): pass
  def properties(*a,**k): pass
  def property(*a,**k): pass
  def propertyCount(*a,**k): pass
  def setBackground(*a,**k): pass
  def setForeground(*a,**k): pass
  def setLayoutDirection(*a,**k): pass
  def setObjectIndex(*a,**k): pass
  def setObjectType(*a,**k): pass
  def setProperty(*a,**k): pass
  def stringProperty(*a,**k): pass
  def toBlockFormat(*a,**k): pass
  def toCharFormat(*a,**k): pass
  def toFrameFormat(*a,**k): pass
  def toImageFormat(*a,**k): pass
  def toListFormat(*a,**k): pass
  def toTableCellFormat(*a,**k): pass
  def toTableFormat(*a,**k): pass
  def type(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextBlockFormat(QTextFormat):
  pass
  FixedHeight = 2
  LineDistanceHeight = 4
  MinimumHeight = 3
  ProportionalHeight = 1
  SingleHeight = 0
  def alignment(*a,**k): pass
  def bottomMargin(*a,**k): pass
  def indent(*a,**k): pass
  def leftMargin(*a,**k): pass
  def lineHeight(*a,**k): pass
  def lineHeightType(*a,**k): pass
  def nonBreakableLines(*a,**k): pass
  def pageBreakPolicy(*a,**k): pass
  def rightMargin(*a,**k): pass
  def setAlignment(*a,**k): pass
  def setBottomMargin(*a,**k): pass
  def setIndent(*a,**k): pass
  def setLeftMargin(*a,**k): pass
  def setLineHeight(*a,**k): pass
  def setNonBreakableLines(*a,**k): pass
  def setPageBreakPolicy(*a,**k): pass
  def setRightMargin(*a,**k): pass
  def setTabPositions(*a,**k): pass
  def setTextIndent(*a,**k): pass
  def setTopMargin(*a,**k): pass
  def tabPositions(*a,**k): pass
  def textIndent(*a,**k): pass
  def topMargin(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextCharFormat(QTextFormat):
  pass
  AlignBaseline = 6
  AlignBottom = 5
  AlignMiddle = 3
  AlignNormal = 0
  AlignSubScript = 2
  AlignSuperScript = 1
  AlignTop = 4
  DashDotDotLine = 5
  DashDotLine = 4
  DashUnderline = 2
  DotLine = 3
  NoUnderline = 0
  SingleUnderline = 1
  SpellCheckUnderline = 7
  WaveUnderline = 6
  def anchorHref(*a,**k): pass
  def anchorName(*a,**k): pass
  def anchorNames(*a,**k): pass
  def font(*a,**k): pass
  def fontCapitalization(*a,**k): pass
  def fontFamily(*a,**k): pass
  def fontFixedPitch(*a,**k): pass
  def fontHintingPreference(*a,**k): pass
  def fontItalic(*a,**k): pass
  def fontKerning(*a,**k): pass
  def fontLetterSpacing(*a,**k): pass
  def fontOverline(*a,**k): pass
  def fontPointSize(*a,**k): pass
  def fontStrikeOut(*a,**k): pass
  def fontStyleHint(*a,**k): pass
  def fontStyleStrategy(*a,**k): pass
  def fontUnderline(*a,**k): pass
  def fontWeight(*a,**k): pass
  def fontWordSpacing(*a,**k): pass
  def isAnchor(*a,**k): pass
  def setAnchor(*a,**k): pass
  def setAnchorHref(*a,**k): pass
  def setAnchorName(*a,**k): pass
  def setAnchorNames(*a,**k): pass
  def setFont(*a,**k): pass
  def setFontCapitalization(*a,**k): pass
  def setFontFamily(*a,**k): pass
  def setFontFixedPitch(*a,**k): pass
  def setFontHintingPreference(*a,**k): pass
  def setFontItalic(*a,**k): pass
  def setFontKerning(*a,**k): pass
  def setFontLetterSpacing(*a,**k): pass
  def setFontOverline(*a,**k): pass
  def setFontPointSize(*a,**k): pass
  def setFontStrikeOut(*a,**k): pass
  def setFontStyleHint(*a,**k): pass
  def setFontStyleStrategy(*a,**k): pass
  def setFontUnderline(*a,**k): pass
  def setFontWeight(*a,**k): pass
  def setFontWordSpacing(*a,**k): pass
  def setTableCellColumnSpan(*a,**k): pass
  def setTableCellRowSpan(*a,**k): pass
  def setTextOutline(*a,**k): pass
  def setToolTip(*a,**k): pass
  def setUnderlineColor(*a,**k): pass
  def setUnderlineStyle(*a,**k): pass
  def setVerticalAlignment(*a,**k): pass
  def tableCellColumnSpan(*a,**k): pass
  def tableCellRowSpan(*a,**k): pass
  def textOutline(*a,**k): pass
  def toolTip(*a,**k): pass
  def underlineColor(*a,**k): pass
  def underlineStyle(*a,**k): pass
  def verticalAlignment(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextImageFormat(QTextCharFormat):
  pass

  def height(*a,**k): pass
  def name(*a,**k): pass
  def setHeight(*a,**k): pass
  def setName(*a,**k): pass
  def setWidth(*a,**k): pass
  def width(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextTableCellFormat(QTextCharFormat):
  pass

  def bottomPadding(*a,**k): pass
  def leftPadding(*a,**k): pass
  def rightPadding(*a,**k): pass
  def setBottomPadding(*a,**k): pass
  def setLeftPadding(*a,**k): pass
  def setPadding(*a,**k): pass
  def setRightPadding(*a,**k): pass
  def setTopPadding(*a,**k): pass
  def topPadding(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextFrameFormat(QTextFormat):
  pass
  BorderStyle_Dashed = 2
  BorderStyle_DotDash = 5
  BorderStyle_DotDotDash = 6
  BorderStyle_Dotted = 1
  BorderStyle_Double = 4
  BorderStyle_Groove = 7
  BorderStyle_Inset = 9
  BorderStyle_None = 0
  BorderStyle_Outset = 10
  BorderStyle_Ridge = 8
  BorderStyle_Solid = 3
  FloatLeft = 1
  FloatRight = 2
  InFlow = 0
  def border(*a,**k): pass
  def borderBrush(*a,**k): pass
  def borderStyle(*a,**k): pass
  def bottomMargin(*a,**k): pass
  def height(*a,**k): pass
  def leftMargin(*a,**k): pass
  def margin(*a,**k): pass
  def padding(*a,**k): pass
  def pageBreakPolicy(*a,**k): pass
  def position(*a,**k): pass
  def rightMargin(*a,**k): pass
  def setBorder(*a,**k): pass
  def setBorderBrush(*a,**k): pass
  def setBorderStyle(*a,**k): pass
  def setBottomMargin(*a,**k): pass
  def setHeight(*a,**k): pass
  def setLeftMargin(*a,**k): pass
  def setMargin(*a,**k): pass
  def setPadding(*a,**k): pass
  def setPageBreakPolicy(*a,**k): pass
  def setPosition(*a,**k): pass
  def setRightMargin(*a,**k): pass
  def setTopMargin(*a,**k): pass
  def setWidth(*a,**k): pass
  def topMargin(*a,**k): pass
  def width(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextTableFormat(QTextFrameFormat):
  pass

  def alignment(*a,**k): pass
  def cellPadding(*a,**k): pass
  def cellSpacing(*a,**k): pass
  def clearColumnWidthConstraints(*a,**k): pass
  def columnWidthConstraints(*a,**k): pass
  def columns(*a,**k): pass
  def headerRowCount(*a,**k): pass
  def setAlignment(*a,**k): pass
  def setCellPadding(*a,**k): pass
  def setCellSpacing(*a,**k): pass
  def setColumnWidthConstraints(*a,**k): pass
  def setColumns(*a,**k): pass
  def setHeaderRowCount(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextListFormat(QTextFormat):
  pass
  ListCircle = -2
  ListDecimal = -4
  ListDisc = -1
  ListLowerAlpha = -5
  ListLowerRoman = -7
  ListSquare = -3
  ListUpperAlpha = -6
  ListUpperRoman = -8
  def indent(*a,**k): pass
  def numberPrefix(*a,**k): pass
  def numberSuffix(*a,**k): pass
  def setIndent(*a,**k): pass
  def setNumberPrefix(*a,**k): pass
  def setNumberSuffix(*a,**k): pass
  def setStyle(*a,**k): pass
  def style(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextCursor(object):
  pass
  BlockUnderCursor = 2
  Document = 3
  Down = 12
  End = 11
  EndOfBlock = 15
  EndOfLine = 13
  EndOfWord = 14
  KeepAnchor = 1
  Left = 9
  LineUnderCursor = 1
  MoveAnchor = 0
  NextBlock = 16
  NextCell = 21
  NextCharacter = 17
  NextRow = 23
  NextWord = 18
  NoMove = 0
  PreviousBlock = 6
  PreviousCell = 22
  PreviousCharacter = 7
  PreviousRow = 24
  PreviousWord = 8
  Right = 19
  Start = 1
  StartOfBlock = 4
  StartOfLine = 3
  StartOfWord = 5
  Up = 2
  WordLeft = 10
  WordRight = 20
  WordUnderCursor = 0
  def anchor(*a,**k): pass
  def atBlockEnd(*a,**k): pass
  def atBlockStart(*a,**k): pass
  def atEnd(*a,**k): pass
  def atStart(*a,**k): pass
  def beginEditBlock(*a,**k): pass
  def block(*a,**k): pass
  def blockCharFormat(*a,**k): pass
  def blockFormat(*a,**k): pass
  def blockNumber(*a,**k): pass
  def charFormat(*a,**k): pass
  def clearSelection(*a,**k): pass
  def columnNumber(*a,**k): pass
  def createList(*a,**k): pass
  def currentFrame(*a,**k): pass
  def currentList(*a,**k): pass
  def currentTable(*a,**k): pass
  def deleteChar(*a,**k): pass
  def deletePreviousChar(*a,**k): pass
  def document(*a,**k): pass
  def endEditBlock(*a,**k): pass
  def hasComplexSelection(*a,**k): pass
  def hasSelection(*a,**k): pass
  def insertBlock(*a,**k): pass
  def insertFragment(*a,**k): pass
  def insertFrame(*a,**k): pass
  def insertHtml(*a,**k): pass
  def insertImage(*a,**k): pass
  def insertList(*a,**k): pass
  def insertTable(*a,**k): pass
  def insertText(*a,**k): pass
  def isCopyOf(*a,**k): pass
  def isNull(*a,**k): pass
  def joinPreviousEditBlock(*a,**k): pass
  def keepPositionOnInsert(*a,**k): pass
  def mergeBlockCharFormat(*a,**k): pass
  def mergeBlockFormat(*a,**k): pass
  def mergeCharFormat(*a,**k): pass
  def movePosition(*a,**k): pass
  def position(*a,**k): pass
  def positionInBlock(*a,**k): pass
  def removeSelectedText(*a,**k): pass
  def select(*a,**k): pass
  def selectedTableCells(*a,**k): pass
  def selectedText(*a,**k): pass
  def selection(*a,**k): pass
  def selectionEnd(*a,**k): pass
  def selectionStart(*a,**k): pass
  def setBlockCharFormat(*a,**k): pass
  def setBlockFormat(*a,**k): pass
  def setCharFormat(*a,**k): pass
  def setKeepPositionOnInsert(*a,**k): pass
  def setPosition(*a,**k): pass
  def setVerticalMovementX(*a,**k): pass
  def setVisualNavigation(*a,**k): pass
  def verticalMovementX(*a,**k): pass
  def visualNavigation(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextDocumentFragment(object):
  pass

  def fromHtml(*a,**k): pass
  def fromPlainText(*a,**k): pass
  def isEmpty(*a,**k): pass
  def toHtml(*a,**k): pass
  def toPlainText(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextDocumentWriter(object):
  pass

  def codec(*a,**k): pass
  def device(*a,**k): pass
  def fileName(*a,**k): pass
  def format(*a,**k): pass
  def setCodec(*a,**k): pass
  def setDevice(*a,**k): pass
  def setFileName(*a,**k): pass
  def setFormat(*a,**k): pass
  def supportedDocumentFormats(*a,**k): pass
  def write(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextFragment(object):
  pass

  def charFormat(*a,**k): pass
  def charFormatIndex(*a,**k): pass
  def contains(*a,**k): pass
  def glyphRuns(*a,**k): pass
  def isValid(*a,**k): pass
  def length(*a,**k): pass
  def position(*a,**k): pass
  def text(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextInlineObject(object):
  pass

  def ascent(*a,**k): pass
  def descent(*a,**k): pass
  def format(*a,**k): pass
  def formatIndex(*a,**k): pass
  def height(*a,**k): pass
  def isValid(*a,**k): pass
  def rect(*a,**k): pass
  def setAscent(*a,**k): pass
  def setDescent(*a,**k): pass
  def setWidth(*a,**k): pass
  def textDirection(*a,**k): pass
  def textPosition(*a,**k): pass
  def width(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextItem(object):
  pass
  Overline = 16
  RightToLeft = 1
  StrikeOut = 64
  Underline = 32
  def ascent(*a,**k): pass
  def descent(*a,**k): pass
  def font(*a,**k): pass
  def renderFlags(*a,**k): pass
  def text(*a,**k): pass
  def width(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextLayout(object):
  pass
  SkipCharacters = 0
  SkipWords = 1
  def additionalFormats(*a,**k): pass
  def beginLayout(*a,**k): pass
  def boundingRect(*a,**k): pass
  def cacheEnabled(*a,**k): pass
  def clearAdditionalFormats(*a,**k): pass
  def clearLayout(*a,**k): pass
  def createLine(*a,**k): pass
  def cursorMoveStyle(*a,**k): pass
  def draw(*a,**k): pass
  def drawCursor(*a,**k): pass
  def endLayout(*a,**k): pass
  def font(*a,**k): pass
  def glyphRuns(*a,**k): pass
  def isValidCursorPosition(*a,**k): pass
  def leftCursorPosition(*a,**k): pass
  def lineAt(*a,**k): pass
  def lineCount(*a,**k): pass
  def lineForTextPosition(*a,**k): pass
  def maximumWidth(*a,**k): pass
  def minimumWidth(*a,**k): pass
  def nextCursorPosition(*a,**k): pass
  def position(*a,**k): pass
  def preeditAreaPosition(*a,**k): pass
  def preeditAreaText(*a,**k): pass
  def previousCursorPosition(*a,**k): pass
  def rightCursorPosition(*a,**k): pass
  def setAdditionalFormats(*a,**k): pass
  def setCacheEnabled(*a,**k): pass
  def setCursorMoveStyle(*a,**k): pass
  def setFont(*a,**k): pass
  def setPosition(*a,**k): pass
  def setPreeditArea(*a,**k): pass
  def setText(*a,**k): pass
  def setTextOption(*a,**k): pass
  def text(*a,**k): pass
  def textOption(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextLength(object):
  pass
  FixedLength = 1
  PercentageLength = 2
  VariableLength = 0
  def rawValue(*a,**k): pass
  def type(*a,**k): pass
  def value(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextOption(object):
  pass
  AddSpaceForLineAndParagraphSeparators = 4
  CenterTab = 2
  DelimiterTab = 3
  IncludeTrailingSpaces = -2147483648
  LeftTab = 0
  ManualWrap = 2
  NoWrap = 0
  RightTab = 1
  ShowLineAndParagraphSeparators = 2
  ShowTabsAndSpaces = 1
  SuppressColors = 8
  WordWrap = 1
  WrapAnywhere = 3
  WrapAtWordBoundaryOrAnywhere = 4
  def alignment(*a,**k): pass
  def flags(*a,**k): pass
  def setAlignment(*a,**k): pass
  def setFlags(*a,**k): pass
  def setTabArray(*a,**k): pass
  def setTabStop(*a,**k): pass
  def setTabs(*a,**k): pass
  def setTextDirection(*a,**k): pass
  def setUseDesignMetrics(*a,**k): pass
  def setWrapMode(*a,**k): pass
  def tabArray(*a,**k): pass
  def tabStop(*a,**k): pass
  def tabs(*a,**k): pass
  def textDirection(*a,**k): pass
  def useDesignMetrics(*a,**k): pass
  def wrapMode(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextTableCell(object):
  pass

  def column(*a,**k): pass
  def columnSpan(*a,**k): pass
  def firstCursorPosition(*a,**k): pass
  def format(*a,**k): pass
  def isValid(*a,**k): pass
  def lastCursorPosition(*a,**k): pass
  def row(*a,**k): pass
  def rowSpan(*a,**k): pass
  def setFormat(*a,**k): pass
  def tableCellFormatIndex(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTransform(object):
  pass
  TxNone = 0
  TxProject = 16
  TxRotate = 4
  TxScale = 2
  TxShear = 8
  TxTranslate = 1
  def adjoint(*a,**k): pass
  def det(*a,**k): pass
  def determinant(*a,**k): pass
  def dx(*a,**k): pass
  def dy(*a,**k): pass
  def fromScale(*a,**k): pass
  def fromTranslate(*a,**k): pass
  def inverted(*a,**k): pass
  def isAffine(*a,**k): pass
  def isIdentity(*a,**k): pass
  def isInvertible(*a,**k): pass
  def isRotating(*a,**k): pass
  def isScaling(*a,**k): pass
  def isTranslating(*a,**k): pass
  def m11(*a,**k): pass
  def m12(*a,**k): pass
  def m13(*a,**k): pass
  def m21(*a,**k): pass
  def m22(*a,**k): pass
  def m23(*a,**k): pass
  def m31(*a,**k): pass
  def m32(*a,**k): pass
  def m33(*a,**k): pass
  def map(*a,**k): pass
  def mapRect(*a,**k): pass
  def mapToPolygon(*a,**k): pass
  def quadToQuad(*a,**k): pass
  def quadToSquare(*a,**k): pass
  def reset(*a,**k): pass
  def rotate(*a,**k): pass
  def rotateRadians(*a,**k): pass
  def scale(*a,**k): pass
  def setMatrix(*a,**k): pass
  def shear(*a,**k): pass
  def squareToQuad(*a,**k): pass
  def toAffine(*a,**k): pass
  def translate(*a,**k): pass
  def transposed(*a,**k): pass
  def type(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTreeWidgetItemIterator(object):
  pass
  All = 0
  Checked = 4096
  Disabled = 32768
  DragDisabled = 128
  DragEnabled = 64
  DropDisabled = 512
  DropEnabled = 256
  Editable = 65536
  Enabled = 16384
  HasChildren = 1024
  Hidden = 1
  NoChildren = 2048
  NotChecked = 8192
  NotEditable = 131072
  NotHidden = 2
  NotSelectable = 32
  Selectable = 16
  Selected = 4
  Unselected = 8
  UserFlag = 16777216
  def value(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QVector2D(object):
  pass

  def dotProduct(*a,**k): pass
  def isNull(*a,**k): pass
  def length(*a,**k): pass
  def lengthSquared(*a,**k): pass
  def normalize(*a,**k): pass
  def normalized(*a,**k): pass
  def setX(*a,**k): pass
  def setY(*a,**k): pass
  def toPoint(*a,**k): pass
  def toPointF(*a,**k): pass
  def toVector3D(*a,**k): pass
  def toVector4D(*a,**k): pass
  def x(*a,**k): pass
  def y(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QVector3D(object):
  pass

  def crossProduct(*a,**k): pass
  def distanceToLine(*a,**k): pass
  def distanceToPlane(*a,**k): pass
  def dotProduct(*a,**k): pass
  def isNull(*a,**k): pass
  def length(*a,**k): pass
  def lengthSquared(*a,**k): pass
  def normal(*a,**k): pass
  def normalize(*a,**k): pass
  def normalized(*a,**k): pass
  def setX(*a,**k): pass
  def setY(*a,**k): pass
  def setZ(*a,**k): pass
  def toPoint(*a,**k): pass
  def toPointF(*a,**k): pass
  def toVector2D(*a,**k): pass
  def toVector4D(*a,**k): pass
  def x(*a,**k): pass
  def y(*a,**k): pass
  def z(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QVector4D(object):
  pass

  def dotProduct(*a,**k): pass
  def isNull(*a,**k): pass
  def length(*a,**k): pass
  def lengthSquared(*a,**k): pass
  def normalize(*a,**k): pass
  def normalized(*a,**k): pass
  def setW(*a,**k): pass
  def setX(*a,**k): pass
  def setY(*a,**k): pass
  def setZ(*a,**k): pass
  def toPoint(*a,**k): pass
  def toPointF(*a,**k): pass
  def toVector2D(*a,**k): pass
  def toVector2DAffine(*a,**k): pass
  def toVector3D(*a,**k): pass
  def toVector3DAffine(*a,**k): pass
  def w(*a,**k): pass
  def x(*a,**k): pass
  def y(*a,**k): pass
  def z(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QWhatsThis(object):
  pass

  def createAction(*a,**k): pass
  def enterWhatsThisMode(*a,**k): pass
  def hideText(*a,**k): pass
  def inWhatsThisMode(*a,**k): pass
  def leaveWhatsThisMode(*a,**k): pass
  def showText(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QX11Info(object):
  pass

  def appCells(*a,**k): pass
  def appClass(*a,**k): pass
  def appColormap(*a,**k): pass
  def appDefaultColormap(*a,**k): pass
  def appDefaultVisual(*a,**k): pass
  def appDepth(*a,**k): pass
  def appDpiX(*a,**k): pass
  def appDpiY(*a,**k): pass
  def appRootWindow(*a,**k): pass
  def appScreen(*a,**k): pass
  def appTime(*a,**k): pass
  def appUserTime(*a,**k): pass
  def appVisual(*a,**k): pass
  def cells(*a,**k): pass
  def colormap(*a,**k): pass
  def defaultColormap(*a,**k): pass
  def defaultVisual(*a,**k): pass
  def depth(*a,**k): pass
  def display(*a,**k): pass
  def isCompositingManagerRunning(*a,**k): pass
  def screen(*a,**k): pass
  def setAppDpiX(*a,**k): pass
  def setAppDpiY(*a,**k): pass
  def setAppTime(*a,**k): pass
  def setAppUserTime(*a,**k): pass
  def visual(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QStringListModel(PyQt4.QtCore.QAbstractListModel):
  pass

  def setStringList(*a,**k): pass
  def stringList(*a,**k): pass

class QAbstractProxyModel(PyQt4.QtCore.QAbstractItemModel):
  pass

  def mapFromSource(*a,**k): pass
  def mapSelectionFromSource(*a,**k): pass
  def mapSelectionToSource(*a,**k): pass
  def mapToSource(*a,**k): pass
  def setSourceModel(*a,**k): pass
  def sourceModel(*a,**k): pass

class QIdentityProxyModel(QAbstractProxyModel):
  pass



class QSortFilterProxyModel(QAbstractProxyModel):
  pass

  def clear(*a,**k): pass
  def dynamicSortFilter(*a,**k): pass
  def filterAcceptsColumn(*a,**k): pass
  def filterAcceptsRow(*a,**k): pass
  def filterCaseSensitivity(*a,**k): pass
  def filterChanged(*a,**k): pass
  def filterKeyColumn(*a,**k): pass
  def filterRegExp(*a,**k): pass
  def filterRole(*a,**k): pass
  def invalidate(*a,**k): pass
  def invalidateFilter(*a,**k): pass
  def isSortLocaleAware(*a,**k): pass
  def lessThan(*a,**k): pass
  def setDynamicSortFilter(*a,**k): pass
  def setFilterCaseSensitivity(*a,**k): pass
  def setFilterFixedString(*a,**k): pass
  def setFilterKeyColumn(*a,**k): pass
  def setFilterRegExp(*a,**k): pass
  def setFilterRole(*a,**k): pass
  def setFilterWildcard(*a,**k): pass
  def setSortCaseSensitivity(*a,**k): pass
  def setSortLocaleAware(*a,**k): pass
  def setSortRole(*a,**k): pass
  def sortCaseSensitivity(*a,**k): pass
  def sortColumn(*a,**k): pass
  def sortOrder(*a,**k): pass
  def sortRole(*a,**k): pass

class QDirModel(PyQt4.QtCore.QAbstractItemModel):
  pass
  FileIconRole = 1
  FileNameRole = 34
  FilePathRole = 33
  def fileIcon(*a,**k): pass
  def fileInfo(*a,**k): pass
  def fileName(*a,**k): pass
  def filePath(*a,**k): pass
  def filter(*a,**k): pass
  def iconProvider(*a,**k): pass
  def isDir(*a,**k): pass
  def isReadOnly(*a,**k): pass
  def lazyChildCount(*a,**k): pass
  def mkdir(*a,**k): pass
  def nameFilters(*a,**k): pass
  def refresh(*a,**k): pass
  def remove(*a,**k): pass
  def resolveSymlinks(*a,**k): pass
  def rmdir(*a,**k): pass
  def setFilter(*a,**k): pass
  def setIconProvider(*a,**k): pass
  def setLazyChildCount(*a,**k): pass
  def setNameFilters(*a,**k): pass
  def setReadOnly(*a,**k): pass
  def setResolveSymlinks(*a,**k): pass
  def setSorting(*a,**k): pass
  def sorting(*a,**k): pass

class QFileSystemModel(PyQt4.QtCore.QAbstractItemModel):
  pass
  FileIconRole = 1
  FileNameRole = 34
  FilePathRole = 33
  FilePermissions = 35
  def directoryLoaded(*a,**k): pass
  def fileIcon(*a,**k): pass
  def fileInfo(*a,**k): pass
  def fileName(*a,**k): pass
  def filePath(*a,**k): pass
  def fileRenamed(*a,**k): pass
  def filter(*a,**k): pass
  def iconProvider(*a,**k): pass
  def isDir(*a,**k): pass
  def isReadOnly(*a,**k): pass
  def lastModified(*a,**k): pass
  def mkdir(*a,**k): pass
  def myComputer(*a,**k): pass
  def nameFilterDisables(*a,**k): pass
  def nameFilters(*a,**k): pass
  def permissions(*a,**k): pass
  def remove(*a,**k): pass
  def resolveSymlinks(*a,**k): pass
  def rmdir(*a,**k): pass
  def rootDirectory(*a,**k): pass
  def rootPath(*a,**k): pass
  def rootPathChanged(*a,**k): pass
  def setFilter(*a,**k): pass
  def setIconProvider(*a,**k): pass
  def setNameFilterDisables(*a,**k): pass
  def setNameFilters(*a,**k): pass
  def setReadOnly(*a,**k): pass
  def setResolveSymlinks(*a,**k): pass
  def setRootPath(*a,**k): pass
  def size(*a,**k): pass
  def type(*a,**k): pass

class QProxyModel(PyQt4.QtCore.QAbstractItemModel):
  pass

  def model(*a,**k): pass
  def setModel(*a,**k): pass

class QStandardItemModel(PyQt4.QtCore.QAbstractItemModel):
  pass

  def appendColumn(*a,**k): pass
  def appendRow(*a,**k): pass
  def clear(*a,**k): pass
  def findItems(*a,**k): pass
  def horizontalHeaderItem(*a,**k): pass
  def indexFromItem(*a,**k): pass
  def invisibleRootItem(*a,**k): pass
  def item(*a,**k): pass
  def itemChanged(*a,**k): pass
  def itemFromIndex(*a,**k): pass
  def itemPrototype(*a,**k): pass
  def setColumnCount(*a,**k): pass
  def setHorizontalHeaderItem(*a,**k): pass
  def setHorizontalHeaderLabels(*a,**k): pass
  def setItem(*a,**k): pass
  def setItemPrototype(*a,**k): pass
  def setRowCount(*a,**k): pass
  def setSortRole(*a,**k): pass
  def setVerticalHeaderItem(*a,**k): pass
  def setVerticalHeaderLabels(*a,**k): pass
  def sortRole(*a,**k): pass
  def takeColumn(*a,**k): pass
  def takeHorizontalHeaderItem(*a,**k): pass
  def takeItem(*a,**k): pass
  def takeRow(*a,**k): pass
  def takeVerticalHeaderItem(*a,**k): pass
  def verticalHeaderItem(*a,**k): pass

class QKeyEventTransition(PyQt4.QtCore.QEventTransition):
  pass

  def key(*a,**k): pass
  def modifierMask(*a,**k): pass
  def setKey(*a,**k): pass
  def setModifierMask(*a,**k): pass

class QMouseEventTransition(PyQt4.QtCore.QEventTransition):
  pass

  def button(*a,**k): pass
  def hitTestPath(*a,**k): pass
  def modifierMask(*a,**k): pass
  def setButton(*a,**k): pass
  def setHitTestPath(*a,**k): pass
  def setModifierMask(*a,**k): pass

class QApplication(PyQt4.QtCore.QCoreApplication):
  pass
  CustomColor = 1
  GuiClient = 1
  GuiServer = 2
  ManyColor = 2
  NormalColor = 0
  Tty = 0
  def aboutQt(*a,**k): pass
  def activeModalWidget(*a,**k): pass
  def activePopupWidget(*a,**k): pass
  def activeWindow(*a,**k): pass
  def alert(*a,**k): pass
  def allWidgets(*a,**k): pass
  def autoSipEnabled(*a,**k): pass
  def beep(*a,**k): pass
  def changeOverrideCursor(*a,**k): pass
  def clipboard(*a,**k): pass
  def closeAllWindows(*a,**k): pass
  def colorSpec(*a,**k): pass
  def commitData(*a,**k): pass
  def commitDataRequest(*a,**k): pass
  def cursorFlashTime(*a,**k): pass
  def desktop(*a,**k): pass
  def desktopSettingsAware(*a,**k): pass
  def doubleClickInterval(*a,**k): pass
  def focusChanged(*a,**k): pass
  def focusWidget(*a,**k): pass
  def font(*a,**k): pass
  def fontDatabaseChanged(*a,**k): pass
  def fontMetrics(*a,**k): pass
  def globalStrut(*a,**k): pass
  def inputContext(*a,**k): pass
  def isEffectEnabled(*a,**k): pass
  def isLeftToRight(*a,**k): pass
  def isRightToLeft(*a,**k): pass
  def isSessionRestored(*a,**k): pass
  def keyboardInputDirection(*a,**k): pass
  def keyboardInputInterval(*a,**k): pass
  def keyboardInputLocale(*a,**k): pass
  def keyboardModifiers(*a,**k): pass
  def lastWindowClosed(*a,**k): pass
  def layoutDirection(*a,**k): pass
  def mouseButtons(*a,**k): pass
  def overrideCursor(*a,**k): pass
  def palette(*a,**k): pass
  def queryKeyboardModifiers(*a,**k): pass
  def quitOnLastWindowClosed(*a,**k): pass
  def restoreOverrideCursor(*a,**k): pass
  def saveState(*a,**k): pass
  def saveStateRequest(*a,**k): pass
  def sessionId(*a,**k): pass
  def sessionKey(*a,**k): pass
  def setActiveWindow(*a,**k): pass
  def setAutoSipEnabled(*a,**k): pass
  def setColorSpec(*a,**k): pass
  def setCursorFlashTime(*a,**k): pass
  def setDesktopSettingsAware(*a,**k): pass
  def setDoubleClickInterval(*a,**k): pass
  def setEffectEnabled(*a,**k): pass
  def setFont(*a,**k): pass
  def setGlobalStrut(*a,**k): pass
  def setGraphicsSystem(*a,**k): pass
  def setInputContext(*a,**k): pass
  def setKeyboardInputInterval(*a,**k): pass
  def setLayoutDirection(*a,**k): pass
  def setOverrideCursor(*a,**k): pass
  def setPalette(*a,**k): pass
  def setQuitOnLastWindowClosed(*a,**k): pass
  def setStartDragDistance(*a,**k): pass
  def setStartDragTime(*a,**k): pass
  def setStyle(*a,**k): pass
  def setStyleSheet(*a,**k): pass
  def setWheelScrollLines(*a,**k): pass
  def setWindowIcon(*a,**k): pass
  def startDragDistance(*a,**k): pass
  def startDragTime(*a,**k): pass
  def style(*a,**k): pass
  def styleSheet(*a,**k): pass
  def syncX(*a,**k): pass
  def topLevelAt(*a,**k): pass
  def topLevelWidgets(*a,**k): pass
  def type(*a,**k): pass
  def wheelScrollLines(*a,**k): pass
  def widgetAt(*a,**k): pass
  def windowIcon(*a,**k): pass
  def x11EventFilter(*a,**k): pass
  def x11ProcessEvent(*a,**k): pass

class QAbstractItemDelegate(PyQt4.QtCore.QObject):
  pass
  EditNextItem = 1
  EditPreviousItem = 2
  NoHint = 0
  RevertModelCache = 4
  SubmitModelCache = 3
  def closeEditor(*a,**k): pass
  def commitData(*a,**k): pass
  def createEditor(*a,**k): pass
  def editorEvent(*a,**k): pass
  def elidedText(*a,**k): pass
  def helpEvent(*a,**k): pass
  def paint(*a,**k): pass
  def setEditorData(*a,**k): pass
  def setModelData(*a,**k): pass
  def sizeHint(*a,**k): pass
  def sizeHintChanged(*a,**k): pass
  def updateEditorGeometry(*a,**k): pass

class QItemDelegate(QAbstractItemDelegate):
  pass

  def drawBackground(*a,**k): pass
  def drawCheck(*a,**k): pass
  def drawDecoration(*a,**k): pass
  def drawDisplay(*a,**k): pass
  def drawFocus(*a,**k): pass
  def hasClipping(*a,**k): pass
  def itemEditorFactory(*a,**k): pass
  def setClipping(*a,**k): pass
  def setItemEditorFactory(*a,**k): pass

class QStyledItemDelegate(QAbstractItemDelegate):
  pass

  def displayText(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def itemEditorFactory(*a,**k): pass
  def setItemEditorFactory(*a,**k): pass

class QAbstractTextDocumentLayout(PyQt4.QtCore.QObject):
  pass

  def anchorAt(*a,**k): pass
  def blockBoundingRect(*a,**k): pass
  def document(*a,**k): pass
  def documentChanged(*a,**k): pass
  def documentSize(*a,**k): pass
  def documentSizeChanged(*a,**k): pass
  def draw(*a,**k): pass
  def drawInlineObject(*a,**k): pass
  def format(*a,**k): pass
  def frameBoundingRect(*a,**k): pass
  def handlerForObject(*a,**k): pass
  def hitTest(*a,**k): pass
  def pageCount(*a,**k): pass
  def pageCountChanged(*a,**k): pass
  def paintDevice(*a,**k): pass
  def positionInlineObject(*a,**k): pass
  def registerHandler(*a,**k): pass
  def resizeInlineObject(*a,**k): pass
  def setPaintDevice(*a,**k): pass
  def update(*a,**k): pass
  def updateBlock(*a,**k): pass

class QPlainTextDocumentLayout(QAbstractTextDocumentLayout):
  pass

  def cursorWidth(*a,**k): pass
  def ensureBlockLayout(*a,**k): pass
  def requestUpdate(*a,**k): pass
  def setCursorWidth(*a,**k): pass

class QAction(PyQt4.QtCore.QObject):
  pass
  AboutQtRole = 3
  AboutRole = 4
  ApplicationSpecificRole = 2
  HighPriority = 256
  Hover = 1
  LowPriority = 0
  NegativeSoftKey = 2
  NoRole = 0
  NoSoftKey = 0
  NormalPriority = 128
  PositiveSoftKey = 1
  PreferencesRole = 5
  QuitRole = 6
  SelectSoftKey = 3
  TextHeuristicRole = 1
  Trigger = 0
  def actionGroup(*a,**k): pass
  def activate(*a,**k): pass
  def associatedGraphicsWidgets(*a,**k): pass
  def associatedWidgets(*a,**k): pass
  def autoRepeat(*a,**k): pass
  def changed(*a,**k): pass
  def data(*a,**k): pass
  def font(*a,**k): pass
  def hover(*a,**k): pass
  def hovered(*a,**k): pass
  def icon(*a,**k): pass
  def iconText(*a,**k): pass
  def isCheckable(*a,**k): pass
  def isChecked(*a,**k): pass
  def isEnabled(*a,**k): pass
  def isIconVisibleInMenu(*a,**k): pass
  def isSeparator(*a,**k): pass
  def isVisible(*a,**k): pass
  def menu(*a,**k): pass
  def menuRole(*a,**k): pass
  def parentWidget(*a,**k): pass
  def priority(*a,**k): pass
  def setActionGroup(*a,**k): pass
  def setAutoRepeat(*a,**k): pass
  def setCheckable(*a,**k): pass
  def setChecked(*a,**k): pass
  def setData(*a,**k): pass
  def setDisabled(*a,**k): pass
  def setEnabled(*a,**k): pass
  def setFont(*a,**k): pass
  def setIcon(*a,**k): pass
  def setIconText(*a,**k): pass
  def setIconVisibleInMenu(*a,**k): pass
  def setMenu(*a,**k): pass
  def setMenuRole(*a,**k): pass
  def setPriority(*a,**k): pass
  def setSeparator(*a,**k): pass
  def setShortcut(*a,**k): pass
  def setShortcutContext(*a,**k): pass
  def setShortcuts(*a,**k): pass
  def setSoftKeyRole(*a,**k): pass
  def setStatusTip(*a,**k): pass
  def setText(*a,**k): pass
  def setToolTip(*a,**k): pass
  def setVisible(*a,**k): pass
  def setWhatsThis(*a,**k): pass
  def shortcut(*a,**k): pass
  def shortcutContext(*a,**k): pass
  def shortcuts(*a,**k): pass
  def showStatusText(*a,**k): pass
  def softKeyRole(*a,**k): pass
  def statusTip(*a,**k): pass
  def text(*a,**k): pass
  def toggle(*a,**k): pass
  def toggled(*a,**k): pass
  def toolTip(*a,**k): pass
  def trigger(*a,**k): pass
  def triggered(*a,**k): pass
  def whatsThis(*a,**k): pass

class QWidgetAction(QAction):
  pass

  def createWidget(*a,**k): pass
  def createdWidgets(*a,**k): pass
  def defaultWidget(*a,**k): pass
  def deleteWidget(*a,**k): pass
  def releaseWidget(*a,**k): pass
  def requestWidget(*a,**k): pass
  def setDefaultWidget(*a,**k): pass

class QActionGroup(PyQt4.QtCore.QObject):
  pass

  def actions(*a,**k): pass
  def addAction(*a,**k): pass
  def checkedAction(*a,**k): pass
  def hovered(*a,**k): pass
  def isEnabled(*a,**k): pass
  def isExclusive(*a,**k): pass
  def isVisible(*a,**k): pass
  def removeAction(*a,**k): pass
  def selected(*a,**k): pass
  def setDisabled(*a,**k): pass
  def setEnabled(*a,**k): pass
  def setExclusive(*a,**k): pass
  def setVisible(*a,**k): pass
  def triggered(*a,**k): pass

class QButtonGroup(PyQt4.QtCore.QObject):
  pass

  def addButton(*a,**k): pass
  def button(*a,**k): pass
  def buttonClicked(*a,**k): pass
  def buttonPressed(*a,**k): pass
  def buttonReleased(*a,**k): pass
  def buttons(*a,**k): pass
  def checkedButton(*a,**k): pass
  def checkedId(*a,**k): pass
  def exclusive(*a,**k): pass
  def id(*a,**k): pass
  def removeButton(*a,**k): pass
  def setExclusive(*a,**k): pass
  def setId(*a,**k): pass

class QClipboard(PyQt4.QtCore.QObject):
  pass
  Clipboard = 0
  FindBuffer = 2
  Selection = 1
  def changed(*a,**k): pass
  def clear(*a,**k): pass
  def dataChanged(*a,**k): pass
  def findBufferChanged(*a,**k): pass
  def image(*a,**k): pass
  def mimeData(*a,**k): pass
  def ownsClipboard(*a,**k): pass
  def ownsFindBuffer(*a,**k): pass
  def ownsSelection(*a,**k): pass
  def pixmap(*a,**k): pass
  def selectionChanged(*a,**k): pass
  def setImage(*a,**k): pass
  def setMimeData(*a,**k): pass
  def setPixmap(*a,**k): pass
  def setText(*a,**k): pass
  def supportsFindBuffer(*a,**k): pass
  def supportsSelection(*a,**k): pass
  def text(*a,**k): pass

class QStyle(PyQt4.QtCore.QObject):
  pass
  CC_ComboBox = 1
  CC_CustomBase = -268435456
  CC_Dial = 7
  CC_GroupBox = 8
  CC_MdiControls = 9
  CC_Q3ListView = 6
  CC_ScrollBar = 2
  CC_Slider = 3
  CC_SpinBox = 0
  CC_TitleBar = 5
  CC_ToolButton = 4
  CE_CheckBox = 3
  CE_CheckBoxLabel = 4
  CE_ColumnViewGrip = 45
  CE_ComboBoxLabel = 40
  CE_CustomBase = -268435456
  CE_DockWidgetTitle = 31
  CE_FocusFrame = 39
  CE_Header = 23
  CE_HeaderEmptyArea = 44
  CE_HeaderLabel = 25
  CE_HeaderSection = 24
  CE_ItemViewItem = 46
  CE_MenuBarEmptyArea = 21
  CE_MenuBarItem = 20
  CE_MenuEmptyArea = 19
  CE_MenuHMargin = 17
  CE_MenuItem = 14
  CE_MenuScroller = 15
  CE_MenuTearoff = 18
  CE_MenuVMargin = 16
  CE_ProgressBar = 10
  CE_ProgressBarContents = 12
  CE_ProgressBarGroove = 11
  CE_ProgressBarLabel = 13
  CE_PushButton = 0
  CE_PushButtonBevel = 1
  CE_PushButtonLabel = 2
  CE_Q3DockWindowEmptyArea = 26
  CE_RadioButton = 5
  CE_RadioButtonLabel = 6
  CE_RubberBand = 30
  CE_ScrollBarAddLine = 32
  CE_ScrollBarAddPage = 34
  CE_ScrollBarFirst = 37
  CE_ScrollBarLast = 38
  CE_ScrollBarSlider = 36
  CE_ScrollBarSubLine = 33
  CE_ScrollBarSubPage = 35
  CE_ShapedFrame = 47
  CE_SizeGrip = 28
  CE_Splitter = 29
  CE_TabBarTab = 7
  CE_TabBarTabLabel = 9
  CE_TabBarTabShape = 8
  CE_ToolBar = 41
  CE_ToolBoxTab = 27
  CE_ToolBoxTabLabel = 43
  CE_ToolBoxTabShape = 42
  CE_ToolButtonLabel = 22
  CT_CheckBox = 1
  CT_ComboBox = 4
  CT_CustomBase = -268435456
  CT_DialogButtons = 20
  CT_GroupBox = 22
  CT_HeaderSection = 21
  CT_ItemViewItem = 24
  CT_LineEdit = 16
  CT_MdiControls = 23
  CT_Menu = 11
  CT_MenuBar = 10
  CT_MenuBarItem = 9
  CT_MenuItem = 8
  CT_ProgressBar = 7
  CT_PushButton = 0
  CT_Q3DockWindow = 6
  CT_Q3Header = 15
  CT_RadioButton = 2
  CT_ScrollBar = 14
  CT_SizeGrip = 18
  CT_Slider = 13
  CT_SpinBox = 17
  CT_Splitter = 5
  CT_TabBarTab = 12
  CT_TabWidget = 19
  CT_ToolButton = 3
  PE_CustomBase = 251658240
  PE_Frame = 5
  PE_FrameButtonBevel = 15
  PE_FrameButtonTool = 16
  PE_FrameDefaultButton = 6
  PE_FrameDockWidget = 7
  PE_FrameFocusRect = 8
  PE_FrameGroupBox = 9
  PE_FrameLineEdit = 10
  PE_FrameMenu = 11
  PE_FrameStatusBar = 12
  PE_FrameStatusBarItem = 12
  PE_FrameTabBarBase = 17
  PE_FrameTabWidget = 13
  PE_FrameWindow = 14
  PE_IndicatorArrowDown = 24
  PE_IndicatorArrowLeft = 25
  PE_IndicatorArrowRight = 26
  PE_IndicatorArrowUp = 27
  PE_IndicatorBranch = 28
  PE_IndicatorButtonDropDown = 29
  PE_IndicatorCheckBox = 31
  PE_IndicatorColumnViewArrow = 47
  PE_IndicatorDockWidgetResizeHandle = 32
  PE_IndicatorHeaderArrow = 33
  PE_IndicatorItemViewItemCheck = 30
  PE_IndicatorItemViewItemDrop = 48
  PE_IndicatorMenuCheckMark = 34
  PE_IndicatorProgressChunk = 35
  PE_IndicatorRadioButton = 36
  PE_IndicatorSpinDown = 37
  PE_IndicatorSpinMinus = 38
  PE_IndicatorSpinPlus = 39
  PE_IndicatorSpinUp = 40
  PE_IndicatorTabClose = 52
  PE_IndicatorTabTear = 44
  PE_IndicatorToolBarHandle = 41
  PE_IndicatorToolBarSeparator = 42
  PE_IndicatorViewItemCheck = 30
  PE_PanelButtonBevel = 19
  PE_PanelButtonCommand = 18
  PE_PanelButtonTool = 20
  PE_PanelItemViewItem = 49
  PE_PanelItemViewRow = 50
  PE_PanelLineEdit = 23
  PE_PanelMenu = 53
  PE_PanelMenuBar = 21
  PE_PanelScrollAreaCorner = 45
  PE_PanelStatusBar = 51
  PE_PanelTipLabel = 43
  PE_PanelToolBar = 22
  PE_Q3CheckListController = 0
  PE_Q3CheckListExclusiveIndicator = 1
  PE_Q3CheckListIndicator = 2
  PE_Q3DockWindowSeparator = 3
  PE_Q3Separator = 4
  PE_Widget = 46
  PM_ButtonDefaultIndicator = 1
  PM_ButtonIconSize = 77
  PM_ButtonMargin = 0
  PM_ButtonShiftHorizontal = 3
  PM_ButtonShiftVertical = 4
  PM_CheckBoxLabelSpacing = 72
  PM_CheckListButtonSize = 41
  PM_CheckListControllerSize = 42
  PM_ComboBoxFrameWidth = 7
  PM_CustomBase = -268435456
  PM_DefaultChildMargin = 62
  PM_DefaultFrameWidth = 5
  PM_DefaultLayoutSpacing = 63
  PM_DefaultTopLevelMargin = 61
  PM_DialogButtonsButtonHeight = 45
  PM_DialogButtonsButtonWidth = 44
  PM_DialogButtonsSeparator = 43
  PM_DockWidgetFrameWidth = 18
  PM_DockWidgetHandleExtent = 17
  PM_DockWidgetSeparatorExtent = 16
  PM_DockWidgetTitleBarButtonMargin = 78
  PM_DockWidgetTitleMargin = 75
  PM_ExclusiveIndicatorHeight = 40
  PM_ExclusiveIndicatorWidth = 39
  PM_FocusFrameHMargin = 70
  PM_FocusFrameVMargin = 69
  PM_HeaderGripMargin = 50
  PM_HeaderMargin = 48
  PM_HeaderMarkSize = 49
  PM_IconViewIconSize = 66
  PM_IndicatorHeight = 38
  PM_IndicatorWidth = 37
  PM_LargeIconSize = 68
  PM_LayoutBottomMargin = 83
  PM_LayoutHorizontalSpacing = 84
  PM_LayoutLeftMargin = 80
  PM_LayoutRightMargin = 82
  PM_LayoutTopMargin = 81
  PM_LayoutVerticalSpacing = 85
  PM_ListViewIconSize = 65
  PM_MDIFrameWidth = 46
  PM_MDIMinimizedWidth = 47
  PM_MaximumDragDistance = 8
  PM_MdiSubWindowFrameWidth = 46
  PM_MdiSubWindowMinimizedWidth = 47
  PM_MenuBarHMargin = 36
  PM_MenuBarItemSpacing = 34
  PM_MenuBarPanelWidth = 33
  PM_MenuBarVMargin = 35
  PM_MenuButtonIndicator = 2
  PM_MenuDesktopFrameWidth = 32
  PM_MenuHMargin = 28
  PM_MenuPanelWidth = 30
  PM_MenuScrollerHeight = 27
  PM_MenuTearoffHeight = 31
  PM_MenuVMargin = 29
  PM_MessageBoxIconSize = 76
  PM_ProgressBarChunkWidth = 24
  PM_RadioButtonLabelSpacing = 79
  PM_ScrollBarExtent = 9
  PM_ScrollBarSliderMin = 10
  PM_ScrollView_ScrollBarSpacing = 90
  PM_SizeGripSize = 74
  PM_SliderControlThickness = 12
  PM_SliderLength = 13
  PM_SliderSpaceAvailable = 15
  PM_SliderThickness = 11
  PM_SliderTickmarkOffset = 14
  PM_SmallIconSize = 67
  PM_SpinBoxFrameWidth = 6
  PM_SpinBoxSliderHeight = 60
  PM_SplitterWidth = 25
  PM_SubMenuOverlap = 91
  PM_TabBarBaseHeight = 22
  PM_TabBarBaseOverlap = 23
  PM_TabBarIconSize = 73
  PM_TabBarScrollButtonWidth = 53
  PM_TabBarTabHSpace = 20
  PM_TabBarTabOverlap = 19
  PM_TabBarTabShiftHorizontal = 51
  PM_TabBarTabShiftVertical = 52
  PM_TabBarTabVSpace = 21
  PM_TabBar_ScrollButtonOverlap = 86
  PM_TabCloseIndicatorHeight = 89
  PM_TabCloseIndicatorWidth = 88
  PM_TextCursorWidth = 87
  PM_TitleBarHeight = 26
  PM_ToolBarExtensionExtent = 59
  PM_ToolBarFrameWidth = 54
  PM_ToolBarHandleExtent = 55
  PM_ToolBarIconSize = 64
  PM_ToolBarItemMargin = 57
  PM_ToolBarItemSpacing = 56
  PM_ToolBarSeparatorExtent = 58
  PM_ToolTipLabelFrameWidth = 71
  RSIP_OnMouseClick = 1
  RSIP_OnMouseClickAndAlreadyFocused = 0
  SC_All = -1
  SC_ComboBoxArrow = 4
  SC_ComboBoxEditField = 2
  SC_ComboBoxFrame = 1
  SC_ComboBoxListBoxPopup = 8
  SC_CustomBase = -268435456
  SC_DialGroove = 1
  SC_DialHandle = 2
  SC_DialTickmarks = 4
  SC_GroupBoxCheckBox = 1
  SC_GroupBoxContents = 4
  SC_GroupBoxFrame = 8
  SC_GroupBoxLabel = 2
  SC_MdiCloseButton = 4
  SC_MdiMinButton = 1
  SC_MdiNormalButton = 2
  SC_None = 0
  SC_Q3ListView = 1
  SC_Q3ListViewBranch = 2
  SC_Q3ListViewExpand = 4
  SC_ScrollBarAddLine = 1
  SC_ScrollBarAddPage = 4
  SC_ScrollBarFirst = 16
  SC_ScrollBarGroove = 128
  SC_ScrollBarLast = 32
  SC_ScrollBarSlider = 64
  SC_ScrollBarSubLine = 2
  SC_ScrollBarSubPage = 8
  SC_SliderGroove = 1
  SC_SliderHandle = 2
  SC_SliderTickmarks = 4
  SC_SpinBoxDown = 2
  SC_SpinBoxEditField = 8
  SC_SpinBoxFrame = 4
  SC_SpinBoxUp = 1
  SC_TitleBarCloseButton = 8
  SC_TitleBarContextHelpButton = 128
  SC_TitleBarLabel = 256
  SC_TitleBarMaxButton = 4
  SC_TitleBarMinButton = 2
  SC_TitleBarNormalButton = 16
  SC_TitleBarShadeButton = 32
  SC_TitleBarSysMenu = 1
  SC_TitleBarUnshadeButton = 64
  SC_ToolButton = 1
  SC_ToolButtonMenu = 2
  SE_CheckBoxClickRect = 5
  SE_CheckBoxContents = 3
  SE_CheckBoxFocusRect = 4
  SE_CheckBoxIndicator = 2
  SE_CheckBoxLayoutItem = 42
  SE_ComboBoxFocusRect = 10
  SE_ComboBoxLayoutItem = 43
  SE_CustomBase = -268435456
  SE_DateTimeEditLayoutItem = 44
  SE_DialogButtonAbort = 21
  SE_DialogButtonAccept = 16
  SE_DialogButtonAll = 20
  SE_DialogButtonApply = 18
  SE_DialogButtonBoxLayoutItem = 45
  SE_DialogButtonCustom = 24
  SE_DialogButtonHelp = 19
  SE_DialogButtonIgnore = 22
  SE_DialogButtonReject = 17
  SE_DialogButtonRetry = 23
  SE_DockWidgetCloseButton = 38
  SE_DockWidgetFloatButton = 39
  SE_DockWidgetIcon = 41
  SE_DockWidgetTitleBarText = 40
  SE_FrameContents = 37
  SE_FrameLayoutItem = 53
  SE_GroupBoxLayoutItem = 54
  SE_HeaderArrow = 27
  SE_HeaderLabel = 26
  SE_ItemViewItemCheckIndicator = 33
  SE_ItemViewItemDecoration = 56
  SE_ItemViewItemFocusRect = 58
  SE_ItemViewItemText = 57
  SE_LabelLayoutItem = 46
  SE_LineEditContents = 36
  SE_ProgressBarContents = 14
  SE_ProgressBarGroove = 13
  SE_ProgressBarLabel = 15
  SE_ProgressBarLayoutItem = 47
  SE_PushButtonContents = 0
  SE_PushButtonFocusRect = 1
  SE_PushButtonLayoutItem = 48
  SE_Q3DockWindowHandleRect = 12
  SE_RadioButtonClickRect = 9
  SE_RadioButtonContents = 7
  SE_RadioButtonFocusRect = 8
  SE_RadioButtonIndicator = 6
  SE_RadioButtonLayoutItem = 49
  SE_ShapedFrameContents = 62
  SE_SliderFocusRect = 11
  SE_SliderLayoutItem = 50
  SE_SpinBoxLayoutItem = 51
  SE_TabBarTabLeftButton = 59
  SE_TabBarTabRightButton = 60
  SE_TabBarTabText = 61
  SE_TabBarTearIndicator = 34
  SE_TabWidgetLayoutItem = 55
  SE_TabWidgetLeftCorner = 31
  SE_TabWidgetRightCorner = 32
  SE_TabWidgetTabBar = 28
  SE_TabWidgetTabContents = 30
  SE_TabWidgetTabPane = 29
  SE_ToolBarHandle = 63
  SE_ToolBoxTabContents = 25
  SE_ToolButtonLayoutItem = 52
  SE_TreeViewDisclosureItem = 35
  SE_ViewItemCheckIndicator = 33
  SH_BlinkCursorWhenTextSelected = 28
  SH_Button_FocusPolicy = 49
  SH_ComboBox_LayoutDirection = 59
  SH_ComboBox_ListMouseTracking = 19
  SH_ComboBox_Popup = 25
  SH_ComboBox_PopupFrameStyle = 70
  SH_CustomBase = -268435456
  SH_Dial_BackgroundRole = 58
  SH_DialogButtonBox_ButtonsHaveIcons = 72
  SH_DialogButtonLayout = 69
  SH_DialogButtons_DefaultButton = 36
  SH_DitherDisabledText = 1
  SH_DockWidget_ButtonsHaveFrame = 95
  SH_DrawMenuBarSeparator = 47
  SH_EtchDisabledText = 0
  SH_FocusFrame_AboveWidget = 78
  SH_FocusFrame_Mask = 54
  SH_FontDialog_SelectAssociatedText = 13
  SH_FormLayoutFieldGrowthPolicy = 90
  SH_FormLayoutFormAlignment = 91
  SH_FormLayoutLabelAlignment = 92
  SH_FormLayoutWrapPolicy = 87
  SH_GroupBox_TextLabelColor = 32
  SH_GroupBox_TextLabelVerticalAlignment = 31
  SH_Header_ArrowAlignment = 6
  SH_ItemView_ActivateItemOnSingleClick = 62
  SH_ItemView_ArrowKeysNavigateIntoChildren = 81
  SH_ItemView_ChangeHighlightOnFocus = 22
  SH_ItemView_DrawDelegateFrame = 93
  SH_ItemView_EllipsisLocation = 60
  SH_ItemView_MovementWithoutUpdatingSelection = 76
  SH_ItemView_PaintAlternatingRowColorsForEmptyArea = 86
  SH_ItemView_ShowDecorationSelected = 61
  SH_LineEdit_PasswordCharacter = 35
  SH_MainWindow_SpaceBelowMenuBar = 12
  SH_MenuBar_AltKeyNavigation = 18
  SH_MenuBar_DismissOnSecondClick = 50
  SH_MenuBar_MouseTracking = 21
  SH_Menu_AllowActiveAndDisabled = 14
  SH_Menu_FadeOutOnHide = 84
  SH_Menu_FillScreenWithScroll = 45
  SH_Menu_FlashTriggeredItem = 83
  SH_Menu_KeyboardSearch = 67
  SH_Menu_Mask = 82
  SH_Menu_MouseTracking = 20
  SH_Menu_Scrollable = 30
  SH_Menu_SelectionWrap = 75
  SH_Menu_SloppySubMenus = 33
  SH_Menu_SpaceActivatesItem = 15
  SH_Menu_SubMenuPopupDelay = 16
  SH_MessageBox_CenterButtons = 74
  SH_MessageBox_TextInteractionFlags = 71
  SH_MessageBox_UseBorderForButtonSpacing = 51
  SH_PrintDialog_RightAlignButtons = 11
  SH_ProgressDialog_CenterCancelButton = 9
  SH_ProgressDialog_TextLabelAlignment = 10
  SH_Q3ListViewExpand_SelectMouseType = 40
  SH_RequestSoftwareInputPanel = 97
  SH_RichText_FullWidthSelection = 29
  SH_RubberBand_Mask = 55
  SH_ScrollBar_ContextMenu = 63
  SH_ScrollBar_LeftClickAbsolutePosition = 39
  SH_ScrollBar_MiddleClickAbsolutePosition = 2
  SH_ScrollBar_RollBetweenButtons = 64
  SH_ScrollBar_ScrollWhenPointerLeavesControl = 3
  SH_ScrollBar_StopMouseOverSlider = 27
  SH_ScrollView_FrameOnlyAroundContents = 17
  SH_Slider_AbsoluteSetButtons = 65
  SH_Slider_PageSetButtons = 66
  SH_Slider_SloppyKeyEvents = 8
  SH_Slider_SnapToValue = 7
  SH_Slider_StopMouseOverSlider = 27
  SH_SpellCheckUnderlineStyle = 73
  SH_SpinBox_AnimateButton = 42
  SH_SpinBox_ClickAutoRepeatRate = 44
  SH_SpinBox_ClickAutoRepeatThreshold = 85
  SH_SpinBox_KeyPressAutoRepeatRate = 43
  SH_SpinControls_DisableOnBounds = 57
  SH_TabBar_Alignment = 5
  SH_TabBar_CloseButtonPosition = 94
  SH_TabBar_ElideMode = 68
  SH_TabBar_PreferNoArrows = 38
  SH_TabBar_SelectMouseType = 4
  SH_TabWidget_DefaultTabPosition = 88
  SH_Table_GridLineColor = 34
  SH_TextControl_FocusIndicatorTextCharFormat = 79
  SH_TitleBar_AutoRaise = 52
  SH_TitleBar_ModifyNotification = 48
  SH_TitleBar_NoBorder = 26
  SH_ToolBar_Movable = 89
  SH_ToolBox_SelectedPageTitleBold = 37
  SH_ToolButtonStyle = 96
  SH_ToolButton_PopupDelay = 53
  SH_ToolTipLabel_Opacity = 46
  SH_ToolTip_Mask = 77
  SH_UnderlineShortcut = 41
  SH_Widget_ShareActivation = 23
  SH_WindowFrame_Mask = 56
  SH_WizardStyle = 80
  SH_Workspace_FillSpaceOnMaximize = 24
  SP_ArrowBack = 53
  SP_ArrowDown = 50
  SP_ArrowForward = 54
  SP_ArrowLeft = 51
  SP_ArrowRight = 52
  SP_ArrowUp = 49
  SP_BrowserReload = 58
  SP_BrowserStop = 59
  SP_CommandLink = 56
  SP_ComputerIcon = 15
  SP_CustomBase = -268435456
  SP_DesktopIcon = 13
  SP_DialogApplyButton = 44
  SP_DialogCancelButton = 39
  SP_DialogCloseButton = 43
  SP_DialogDiscardButton = 46
  SP_DialogHelpButton = 40
  SP_DialogNoButton = 48
  SP_DialogOkButton = 38
  SP_DialogOpenButton = 41
  SP_DialogResetButton = 45
  SP_DialogSaveButton = 42
  SP_DialogYesButton = 47
  SP_DirClosedIcon = 22
  SP_DirHomeIcon = 55
  SP_DirIcon = 37
  SP_DirLinkIcon = 23
  SP_DirOpenIcon = 21
  SP_DockWidgetCloseButton = 8
  SP_DriveCDIcon = 18
  SP_DriveDVDIcon = 19
  SP_DriveFDIcon = 16
  SP_DriveHDIcon = 17
  SP_DriveNetIcon = 20
  SP_FileDialogBack = 36
  SP_FileDialogContentsView = 34
  SP_FileDialogDetailedView = 32
  SP_FileDialogEnd = 29
  SP_FileDialogInfoView = 33
  SP_FileDialogListView = 35
  SP_FileDialogNewFolder = 31
  SP_FileDialogStart = 28
  SP_FileDialogToParent = 30
  SP_FileIcon = 24
  SP_FileLinkIcon = 25
  SP_MediaPause = 62
  SP_MediaPlay = 60
  SP_MediaSeekBackward = 66
  SP_MediaSeekForward = 65
  SP_MediaSkipBackward = 64
  SP_MediaSkipForward = 63
  SP_MediaStop = 61
  SP_MediaVolume = 67
  SP_MediaVolumeMuted = 68
  SP_MessageBoxCritical = 11
  SP_MessageBoxInformation = 9
  SP_MessageBoxQuestion = 12
  SP_MessageBoxWarning = 10
  SP_TitleBarCloseButton = 3
  SP_TitleBarContextHelpButton = 7
  SP_TitleBarMaxButton = 2
  SP_TitleBarMenuButton = 0
  SP_TitleBarMinButton = 1
  SP_TitleBarNormalButton = 4
  SP_TitleBarShadeButton = 5
  SP_TitleBarUnshadeButton = 6
  SP_ToolBarHorizontalExtensionButton = 26
  SP_ToolBarVerticalExtensionButton = 27
  SP_TrashIcon = 14
  SP_VistaShield = 57
  State_Active = 65536
  State_AutoRaise = 4096
  State_Bottom = 1024
  State_Children = 524288
  State_DownArrow = 64
  State_Editing = 4194304
  State_Enabled = 1
  State_FocusAtBorder = 2048
  State_HasFocus = 256
  State_Horizontal = 128
  State_Item = 1048576
  State_KeyboardFocusChange = 8388608
  State_Mini = 134217728
  State_MouseOver = 8192
  State_NoChange = 16
  State_None = 0
  State_Off = 8
  State_On = 32
  State_Open = 262144
  State_Raised = 2
  State_ReadOnly = 33554432
  State_Selected = 32768
  State_Sibling = 2097152
  State_Small = 67108864
  State_Sunken = 4
  State_Top = 512
  State_UpArrow = 16384
  State_Window = 131072
  def alignedRect(*a,**k): pass
  def combinedLayoutSpacing(*a,**k): pass
  def drawComplexControl(*a,**k): pass
  def drawControl(*a,**k): pass
  def drawItemPixmap(*a,**k): pass
  def drawItemText(*a,**k): pass
  def drawPrimitive(*a,**k): pass
  def generatedIconPixmap(*a,**k): pass
  def hitTestComplexControl(*a,**k): pass
  def itemPixmapRect(*a,**k): pass
  def itemTextRect(*a,**k): pass
  def layoutSpacing(*a,**k): pass
  def layoutSpacingImplementation(*a,**k): pass
  def pixelMetric(*a,**k): pass
  def polish(*a,**k): pass
  def proxy(*a,**k): pass
  def sizeFromContents(*a,**k): pass
  def sliderPositionFromValue(*a,**k): pass
  def sliderValueFromPosition(*a,**k): pass
  def standardIcon(*a,**k): pass
  def standardIconImplementation(*a,**k): pass
  def standardPalette(*a,**k): pass
  def standardPixmap(*a,**k): pass
  def styleHint(*a,**k): pass
  def subControlRect(*a,**k): pass
  def subElementRect(*a,**k): pass
  def unpolish(*a,**k): pass
  def visualAlignment(*a,**k): pass
  def visualPos(*a,**k): pass
  def visualRect(*a,**k): pass

class QCommonStyle(QStyle):
  pass



class QCompleter(PyQt4.QtCore.QObject):
  pass
  CaseInsensitivelySortedModel = 2
  CaseSensitivelySortedModel = 1
  InlineCompletion = 2
  PopupCompletion = 0
  UnfilteredPopupCompletion = 1
  UnsortedModel = 0
  def activated(*a,**k): pass
  def caseSensitivity(*a,**k): pass
  def complete(*a,**k): pass
  def completionColumn(*a,**k): pass
  def completionCount(*a,**k): pass
  def completionMode(*a,**k): pass
  def completionModel(*a,**k): pass
  def completionPrefix(*a,**k): pass
  def completionRole(*a,**k): pass
  def currentCompletion(*a,**k): pass
  def currentIndex(*a,**k): pass
  def currentRow(*a,**k): pass
  def highlighted(*a,**k): pass
  def maxVisibleItems(*a,**k): pass
  def model(*a,**k): pass
  def modelSorting(*a,**k): pass
  def pathFromIndex(*a,**k): pass
  def popup(*a,**k): pass
  def setCaseSensitivity(*a,**k): pass
  def setCompletionColumn(*a,**k): pass
  def setCompletionMode(*a,**k): pass
  def setCompletionPrefix(*a,**k): pass
  def setCompletionRole(*a,**k): pass
  def setCurrentRow(*a,**k): pass
  def setMaxVisibleItems(*a,**k): pass
  def setModel(*a,**k): pass
  def setModelSorting(*a,**k): pass
  def setPopup(*a,**k): pass
  def setWidget(*a,**k): pass
  def setWrapAround(*a,**k): pass
  def splitPath(*a,**k): pass
  def widget(*a,**k): pass
  def wrapAround(*a,**k): pass

class QDataWidgetMapper(PyQt4.QtCore.QObject):
  pass
  AutoSubmit = 0
  ManualSubmit = 1
  def addMapping(*a,**k): pass
  def clearMapping(*a,**k): pass
  def currentIndex(*a,**k): pass
  def currentIndexChanged(*a,**k): pass
  def itemDelegate(*a,**k): pass
  def mappedPropertyName(*a,**k): pass
  def mappedSection(*a,**k): pass
  def mappedWidgetAt(*a,**k): pass
  def model(*a,**k): pass
  def orientation(*a,**k): pass
  def removeMapping(*a,**k): pass
  def revert(*a,**k): pass
  def rootIndex(*a,**k): pass
  def setCurrentIndex(*a,**k): pass
  def setCurrentModelIndex(*a,**k): pass
  def setItemDelegate(*a,**k): pass
  def setModel(*a,**k): pass
  def setOrientation(*a,**k): pass
  def setRootIndex(*a,**k): pass
  def setSubmitPolicy(*a,**k): pass
  def submit(*a,**k): pass
  def submitPolicy(*a,**k): pass
  def toFirst(*a,**k): pass
  def toLast(*a,**k): pass
  def toNext(*a,**k): pass
  def toPrevious(*a,**k): pass

class QGesture(PyQt4.QtCore.QObject):
  pass
  CancelAllInContext = 1
  CancelNone = 0
  def gestureCancelPolicy(*a,**k): pass
  def gestureType(*a,**k): pass
  def hasHotSpot(*a,**k): pass
  def hotSpot(*a,**k): pass
  def setGestureCancelPolicy(*a,**k): pass
  def setHotSpot(*a,**k): pass
  def state(*a,**k): pass
  def unsetHotSpot(*a,**k): pass

class QPanGesture(QGesture):
  pass

  def acceleration(*a,**k): pass
  def delta(*a,**k): pass
  def lastOffset(*a,**k): pass
  def offset(*a,**k): pass
  def setAcceleration(*a,**k): pass
  def setLastOffset(*a,**k): pass
  def setOffset(*a,**k): pass

class QPinchGesture(QGesture):
  pass
  CenterPointChanged = 4
  RotationAngleChanged = 2
  ScaleFactorChanged = 1
  def centerPoint(*a,**k): pass
  def changeFlags(*a,**k): pass
  def lastCenterPoint(*a,**k): pass
  def lastRotationAngle(*a,**k): pass
  def lastScaleFactor(*a,**k): pass
  def rotationAngle(*a,**k): pass
  def scaleFactor(*a,**k): pass
  def setCenterPoint(*a,**k): pass
  def setChangeFlags(*a,**k): pass
  def setLastCenterPoint(*a,**k): pass
  def setLastRotationAngle(*a,**k): pass
  def setLastScaleFactor(*a,**k): pass
  def setRotationAngle(*a,**k): pass
  def setScaleFactor(*a,**k): pass
  def setStartCenterPoint(*a,**k): pass
  def setTotalChangeFlags(*a,**k): pass
  def setTotalRotationAngle(*a,**k): pass
  def setTotalScaleFactor(*a,**k): pass
  def startCenterPoint(*a,**k): pass
  def totalChangeFlags(*a,**k): pass
  def totalRotationAngle(*a,**k): pass
  def totalScaleFactor(*a,**k): pass

class QSwipeGesture(QGesture):
  pass
  Down = 4
  Left = 1
  NoDirection = 0
  Right = 2
  Up = 3
  def horizontalDirection(*a,**k): pass
  def setSwipeAngle(*a,**k): pass
  def swipeAngle(*a,**k): pass
  def verticalDirection(*a,**k): pass

class QTapAndHoldGesture(QGesture):
  pass

  def position(*a,**k): pass
  def setPosition(*a,**k): pass
  def setTimeout(*a,**k): pass
  def timeout(*a,**k): pass

class QTapGesture(QGesture):
  pass

  def position(*a,**k): pass
  def setPosition(*a,**k): pass

class QValidator(PyQt4.QtCore.QObject):
  pass
  Acceptable = 2
  Intermediate = 1
  Invalid = 0
  def fixup(*a,**k): pass
  def locale(*a,**k): pass
  def setLocale(*a,**k): pass
  def validate(*a,**k): pass

class QDoubleValidator(QValidator):
  pass
  ScientificNotation = 1
  StandardNotation = 0
  def bottom(*a,**k): pass
  def decimals(*a,**k): pass
  def notation(*a,**k): pass
  def setBottom(*a,**k): pass
  def setDecimals(*a,**k): pass
  def setNotation(*a,**k): pass
  def setRange(*a,**k): pass
  def setTop(*a,**k): pass
  def top(*a,**k): pass

class QIntValidator(QValidator):
  pass

  def bottom(*a,**k): pass
  def setBottom(*a,**k): pass
  def setRange(*a,**k): pass
  def setTop(*a,**k): pass
  def top(*a,**k): pass

class QRegExpValidator(QValidator):
  pass

  def regExp(*a,**k): pass
  def setRegExp(*a,**k): pass

class QDrag(PyQt4.QtCore.QObject):
  pass

  def actionChanged(*a,**k): pass
  def exec_(*a,**k): pass
  def hotSpot(*a,**k): pass
  def mimeData(*a,**k): pass
  def pixmap(*a,**k): pass
  def setDragCursor(*a,**k): pass
  def setHotSpot(*a,**k): pass
  def setMimeData(*a,**k): pass
  def setPixmap(*a,**k): pass
  def source(*a,**k): pass
  def start(*a,**k): pass
  def target(*a,**k): pass
  def targetChanged(*a,**k): pass

class QGraphicsAnchor(PyQt4.QtCore.QObject):
  pass

  def setSizePolicy(*a,**k): pass
  def setSpacing(*a,**k): pass
  def sizePolicy(*a,**k): pass
  def spacing(*a,**k): pass
  def unsetSpacing(*a,**k): pass

class QGraphicsEffect(PyQt4.QtCore.QObject):
  pass
  NoPad = 0
  PadToEffectiveBoundingRect = 2
  PadToTransparentBorder = 1
  SourceAttached = 1
  SourceBoundingRectChanged = 4
  SourceDetached = 2
  SourceInvalidated = 8
  def boundingRect(*a,**k): pass
  def boundingRectFor(*a,**k): pass
  def draw(*a,**k): pass
  def drawSource(*a,**k): pass
  def enabledChanged(*a,**k): pass
  def isEnabled(*a,**k): pass
  def setEnabled(*a,**k): pass
  def sourceBoundingRect(*a,**k): pass
  def sourceChanged(*a,**k): pass
  def sourceIsPixmap(*a,**k): pass
  def sourcePixmap(*a,**k): pass
  def update(*a,**k): pass
  def updateBoundingRect(*a,**k): pass

class QGraphicsBlurEffect(QGraphicsEffect):
  pass
  AnimationHint = 2
  PerformanceHint = 0
  QualityHint = 1
  def blurHints(*a,**k): pass
  def blurHintsChanged(*a,**k): pass
  def blurRadius(*a,**k): pass
  def blurRadiusChanged(*a,**k): pass
  def setBlurHints(*a,**k): pass
  def setBlurRadius(*a,**k): pass

class QGraphicsColorizeEffect(QGraphicsEffect):
  pass

  def color(*a,**k): pass
  def colorChanged(*a,**k): pass
  def setColor(*a,**k): pass
  def setStrength(*a,**k): pass
  def strength(*a,**k): pass
  def strengthChanged(*a,**k): pass

class QGraphicsDropShadowEffect(QGraphicsEffect):
  pass

  def blurRadius(*a,**k): pass
  def blurRadiusChanged(*a,**k): pass
  def color(*a,**k): pass
  def colorChanged(*a,**k): pass
  def offset(*a,**k): pass
  def offsetChanged(*a,**k): pass
  def setBlurRadius(*a,**k): pass
  def setColor(*a,**k): pass
  def setOffset(*a,**k): pass
  def setXOffset(*a,**k): pass
  def setYOffset(*a,**k): pass
  def xOffset(*a,**k): pass
  def yOffset(*a,**k): pass

class QGraphicsOpacityEffect(QGraphicsEffect):
  pass

  def opacity(*a,**k): pass
  def opacityChanged(*a,**k): pass
  def opacityMask(*a,**k): pass
  def opacityMaskChanged(*a,**k): pass
  def setOpacity(*a,**k): pass
  def setOpacityMask(*a,**k): pass

class QGraphicsItemAnimation(PyQt4.QtCore.QObject):
  pass

  def afterAnimationStep(*a,**k): pass
  def beforeAnimationStep(*a,**k): pass
  def clear(*a,**k): pass
  def horizontalScaleAt(*a,**k): pass
  def horizontalShearAt(*a,**k): pass
  def item(*a,**k): pass
  def matrixAt(*a,**k): pass
  def posAt(*a,**k): pass
  def posList(*a,**k): pass
  def reset(*a,**k): pass
  def rotationAt(*a,**k): pass
  def rotationList(*a,**k): pass
  def scaleList(*a,**k): pass
  def setItem(*a,**k): pass
  def setPosAt(*a,**k): pass
  def setRotationAt(*a,**k): pass
  def setScaleAt(*a,**k): pass
  def setShearAt(*a,**k): pass
  def setStep(*a,**k): pass
  def setTimeLine(*a,**k): pass
  def setTranslationAt(*a,**k): pass
  def shearList(*a,**k): pass
  def timeLine(*a,**k): pass
  def translationList(*a,**k): pass
  def verticalScaleAt(*a,**k): pass
  def verticalShearAt(*a,**k): pass
  def xTranslationAt(*a,**k): pass
  def yTranslationAt(*a,**k): pass

class QGraphicsTransform(PyQt4.QtCore.QObject):
  pass

  def applyTo(*a,**k): pass
  def update(*a,**k): pass

class QGraphicsRotation(QGraphicsTransform):
  pass

  def angle(*a,**k): pass
  def angleChanged(*a,**k): pass
  def axis(*a,**k): pass
  def axisChanged(*a,**k): pass
  def origin(*a,**k): pass
  def originChanged(*a,**k): pass
  def setAngle(*a,**k): pass
  def setAxis(*a,**k): pass
  def setOrigin(*a,**k): pass

class QGraphicsScale(QGraphicsTransform):
  pass

  def origin(*a,**k): pass
  def originChanged(*a,**k): pass
  def scaleChanged(*a,**k): pass
  def setOrigin(*a,**k): pass
  def setXScale(*a,**k): pass
  def setYScale(*a,**k): pass
  def setZScale(*a,**k): pass
  def xScale(*a,**k): pass
  def xScaleChanged(*a,**k): pass
  def yScale(*a,**k): pass
  def yScaleChanged(*a,**k): pass
  def zScale(*a,**k): pass
  def zScaleChanged(*a,**k): pass

class QGraphicsScene(PyQt4.QtCore.QObject):
  pass
  AllLayers = 65535
  BackgroundLayer = 2
  BspTreeIndex = 0
  ForegroundLayer = 4
  ItemLayer = 1
  NoIndex = -1
  def activePanel(*a,**k): pass
  def activeWindow(*a,**k): pass
  def addEllipse(*a,**k): pass
  def addItem(*a,**k): pass
  def addLine(*a,**k): pass
  def addPath(*a,**k): pass
  def addPixmap(*a,**k): pass
  def addPolygon(*a,**k): pass
  def addRect(*a,**k): pass
  def addSimpleText(*a,**k): pass
  def addText(*a,**k): pass
  def addWidget(*a,**k): pass
  def advance(*a,**k): pass
  def backgroundBrush(*a,**k): pass
  def bspTreeDepth(*a,**k): pass
  def changed(*a,**k): pass
  def clear(*a,**k): pass
  def clearFocus(*a,**k): pass
  def clearSelection(*a,**k): pass
  def collidingItems(*a,**k): pass
  def contextMenuEvent(*a,**k): pass
  def createItemGroup(*a,**k): pass
  def destroyItemGroup(*a,**k): pass
  def dragEnterEvent(*a,**k): pass
  def dragLeaveEvent(*a,**k): pass
  def dragMoveEvent(*a,**k): pass
  def drawBackground(*a,**k): pass
  def drawForeground(*a,**k): pass
  def drawItems(*a,**k): pass
  def dropEvent(*a,**k): pass
  def focusInEvent(*a,**k): pass
  def focusItem(*a,**k): pass
  def focusNextPrevChild(*a,**k): pass
  def focusOutEvent(*a,**k): pass
  def font(*a,**k): pass
  def foregroundBrush(*a,**k): pass
  def hasFocus(*a,**k): pass
  def height(*a,**k): pass
  def helpEvent(*a,**k): pass
  def inputMethodEvent(*a,**k): pass
  def inputMethodQuery(*a,**k): pass
  def invalidate(*a,**k): pass
  def isActive(*a,**k): pass
  def isSortCacheEnabled(*a,**k): pass
  def itemAt(*a,**k): pass
  def itemIndexMethod(*a,**k): pass
  def items(*a,**k): pass
  def itemsBoundingRect(*a,**k): pass
  def keyPressEvent(*a,**k): pass
  def keyReleaseEvent(*a,**k): pass
  def mouseDoubleClickEvent(*a,**k): pass
  def mouseGrabberItem(*a,**k): pass
  def mouseMoveEvent(*a,**k): pass
  def mousePressEvent(*a,**k): pass
  def mouseReleaseEvent(*a,**k): pass
  def palette(*a,**k): pass
  def removeItem(*a,**k): pass
  def render(*a,**k): pass
  def sceneRect(*a,**k): pass
  def sceneRectChanged(*a,**k): pass
  def selectedItems(*a,**k): pass
  def selectionArea(*a,**k): pass
  def selectionChanged(*a,**k): pass
  def sendEvent(*a,**k): pass
  def setActivePanel(*a,**k): pass
  def setActiveWindow(*a,**k): pass
  def setBackgroundBrush(*a,**k): pass
  def setBspTreeDepth(*a,**k): pass
  def setFocus(*a,**k): pass
  def setFocusItem(*a,**k): pass
  def setFont(*a,**k): pass
  def setForegroundBrush(*a,**k): pass
  def setItemIndexMethod(*a,**k): pass
  def setPalette(*a,**k): pass
  def setSceneRect(*a,**k): pass
  def setSelectionArea(*a,**k): pass
  def setSortCacheEnabled(*a,**k): pass
  def setStickyFocus(*a,**k): pass
  def setStyle(*a,**k): pass
  def stickyFocus(*a,**k): pass
  def style(*a,**k): pass
  def update(*a,**k): pass
  def views(*a,**k): pass
  def wheelEvent(*a,**k): pass
  def width(*a,**k): pass

class QInputContext(PyQt4.QtCore.QObject):
  pass
  PreeditFormat = 0
  SelectionFormat = 1
  def actions(*a,**k): pass
  def filterEvent(*a,**k): pass
  def focusWidget(*a,**k): pass
  def font(*a,**k): pass
  def identifierName(*a,**k): pass
  def isComposing(*a,**k): pass
  def language(*a,**k): pass
  def mouseHandler(*a,**k): pass
  def reset(*a,**k): pass
  def sendEvent(*a,**k): pass
  def setFocusWidget(*a,**k): pass
  def standardFormat(*a,**k): pass
  def update(*a,**k): pass
  def widgetDestroyed(*a,**k): pass

class QItemSelectionModel(PyQt4.QtCore.QObject):
  pass
  Clear = 1
  ClearAndSelect = 3
  Columns = 64
  Current = 16
  Deselect = 4
  NoUpdate = 0
  Rows = 32
  Select = 2
  SelectCurrent = 18
  Toggle = 8
  ToggleCurrent = 24
  def clear(*a,**k): pass
  def clearSelection(*a,**k): pass
  def columnIntersectsSelection(*a,**k): pass
  def currentChanged(*a,**k): pass
  def currentColumnChanged(*a,**k): pass
  def currentIndex(*a,**k): pass
  def currentRowChanged(*a,**k): pass
  def emitSelectionChanged(*a,**k): pass
  def hasSelection(*a,**k): pass
  def isColumnSelected(*a,**k): pass
  def isRowSelected(*a,**k): pass
  def isSelected(*a,**k): pass
  def model(*a,**k): pass
  def reset(*a,**k): pass
  def rowIntersectsSelection(*a,**k): pass
  def select(*a,**k): pass
  def selectedColumns(*a,**k): pass
  def selectedIndexes(*a,**k): pass
  def selectedRows(*a,**k): pass
  def selection(*a,**k): pass
  def selectionChanged(*a,**k): pass
  def setCurrentIndex(*a,**k): pass

class QMovie(PyQt4.QtCore.QObject):
  pass
  CacheAll = 1
  CacheNone = 0
  NotRunning = 0
  Paused = 1
  Running = 2
  def backgroundColor(*a,**k): pass
  def cacheMode(*a,**k): pass
  def currentFrameNumber(*a,**k): pass
  def currentImage(*a,**k): pass
  def currentPixmap(*a,**k): pass
  def device(*a,**k): pass
  def error(*a,**k): pass
  def fileName(*a,**k): pass
  def finished(*a,**k): pass
  def format(*a,**k): pass
  def frameChanged(*a,**k): pass
  def frameCount(*a,**k): pass
  def frameRect(*a,**k): pass
  def isValid(*a,**k): pass
  def jumpToFrame(*a,**k): pass
  def jumpToNextFrame(*a,**k): pass
  def loopCount(*a,**k): pass
  def nextFrameDelay(*a,**k): pass
  def resized(*a,**k): pass
  def scaledSize(*a,**k): pass
  def setBackgroundColor(*a,**k): pass
  def setCacheMode(*a,**k): pass
  def setDevice(*a,**k): pass
  def setFileName(*a,**k): pass
  def setFormat(*a,**k): pass
  def setPaused(*a,**k): pass
  def setScaledSize(*a,**k): pass
  def setSpeed(*a,**k): pass
  def speed(*a,**k): pass
  def start(*a,**k): pass
  def started(*a,**k): pass
  def state(*a,**k): pass
  def stateChanged(*a,**k): pass
  def stop(*a,**k): pass
  def supportedFormats(*a,**k): pass
  def updated(*a,**k): pass

class QSessionManager(PyQt4.QtCore.QObject):
  pass
  RestartAnyway = 1
  RestartIfRunning = 0
  RestartImmediately = 2
  RestartNever = 3
  def allowsErrorInteraction(*a,**k): pass
  def allowsInteraction(*a,**k): pass
  def cancel(*a,**k): pass
  def discardCommand(*a,**k): pass
  def isPhase2(*a,**k): pass
  def release(*a,**k): pass
  def requestPhase2(*a,**k): pass
  def restartCommand(*a,**k): pass
  def restartHint(*a,**k): pass
  def sessionId(*a,**k): pass
  def sessionKey(*a,**k): pass
  def setDiscardCommand(*a,**k): pass
  def setManagerProperty(*a,**k): pass
  def setRestartCommand(*a,**k): pass
  def setRestartHint(*a,**k): pass

class QShortcut(PyQt4.QtCore.QObject):
  pass

  def activated(*a,**k): pass
  def activatedAmbiguously(*a,**k): pass
  def autoRepeat(*a,**k): pass
  def context(*a,**k): pass
  def id(*a,**k): pass
  def isEnabled(*a,**k): pass
  def key(*a,**k): pass
  def parentWidget(*a,**k): pass
  def setAutoRepeat(*a,**k): pass
  def setContext(*a,**k): pass
  def setEnabled(*a,**k): pass
  def setKey(*a,**k): pass
  def setWhatsThis(*a,**k): pass
  def whatsThis(*a,**k): pass

class QSound(PyQt4.QtCore.QObject):
  pass

  def fileName(*a,**k): pass
  def isAvailable(*a,**k): pass
  def isFinished(*a,**k): pass
  def loops(*a,**k): pass
  def loopsRemaining(*a,**k): pass
  def play(*a,**k): pass
  def setLoops(*a,**k): pass
  def stop(*a,**k): pass

class QSyntaxHighlighter(PyQt4.QtCore.QObject):
  pass

  def currentBlock(*a,**k): pass
  def currentBlockState(*a,**k): pass
  def currentBlockUserData(*a,**k): pass
  def document(*a,**k): pass
  def format(*a,**k): pass
  def highlightBlock(*a,**k): pass
  def previousBlockState(*a,**k): pass
  def rehighlight(*a,**k): pass
  def rehighlightBlock(*a,**k): pass
  def setCurrentBlockState(*a,**k): pass
  def setCurrentBlockUserData(*a,**k): pass
  def setDocument(*a,**k): pass
  def setFormat(*a,**k): pass

class QSystemTrayIcon(PyQt4.QtCore.QObject):
  pass
  Context = 1
  Critical = 3
  DoubleClick = 2
  Information = 1
  MiddleClick = 4
  NoIcon = 0
  Trigger = 3
  Unknown = 0
  Warning = 2
  def activated(*a,**k): pass
  def contextMenu(*a,**k): pass
  def geometry(*a,**k): pass
  def hide(*a,**k): pass
  def icon(*a,**k): pass
  def isSystemTrayAvailable(*a,**k): pass
  def isVisible(*a,**k): pass
  def messageClicked(*a,**k): pass
  def setContextMenu(*a,**k): pass
  def setIcon(*a,**k): pass
  def setToolTip(*a,**k): pass
  def setVisible(*a,**k): pass
  def show(*a,**k): pass
  def showMessage(*a,**k): pass
  def supportsMessages(*a,**k): pass
  def toolTip(*a,**k): pass

class QTextObject(PyQt4.QtCore.QObject):
  pass

  def document(*a,**k): pass
  def format(*a,**k): pass
  def formatIndex(*a,**k): pass
  def objectIndex(*a,**k): pass
  def setFormat(*a,**k): pass

class QTextBlockGroup(QTextObject):
  pass

  def blockFormatChanged(*a,**k): pass
  def blockInserted(*a,**k): pass
  def blockList(*a,**k): pass
  def blockRemoved(*a,**k): pass

class QTextList(QTextBlockGroup):
  pass

  def add(*a,**k): pass
  def count(*a,**k): pass
  def isEmpty(*a,**k): pass
  def item(*a,**k): pass
  def itemNumber(*a,**k): pass
  def itemText(*a,**k): pass
  def remove(*a,**k): pass
  def removeItem(*a,**k): pass

class QTextFrame(QTextObject):
  pass

  def begin(*a,**k): pass
  def childFrames(*a,**k): pass
  def end(*a,**k): pass
  def firstCursorPosition(*a,**k): pass
  def firstPosition(*a,**k): pass
  def frameFormat(*a,**k): pass
  def lastCursorPosition(*a,**k): pass
  def lastPosition(*a,**k): pass
  def parentFrame(*a,**k): pass
  def setFrameFormat(*a,**k): pass

class QTextTable(QTextFrame):
  pass

  def appendColumns(*a,**k): pass
  def appendRows(*a,**k): pass
  def cellAt(*a,**k): pass
  def columns(*a,**k): pass
  def insertColumns(*a,**k): pass
  def insertRows(*a,**k): pass
  def mergeCells(*a,**k): pass
  def removeColumns(*a,**k): pass
  def removeRows(*a,**k): pass
  def resize(*a,**k): pass
  def rowEnd(*a,**k): pass
  def rowStart(*a,**k): pass
  def rows(*a,**k): pass
  def splitCell(*a,**k): pass

class QTextDocument(PyQt4.QtCore.QObject):
  pass
  DocumentTitle = 0
  DocumentUrl = 1
  FindBackward = 1
  FindCaseSensitively = 2
  FindWholeWords = 4
  HtmlResource = 1
  ImageResource = 2
  RedoStack = 2
  StyleSheetResource = 3
  UndoAndRedoStacks = 3
  UndoStack = 1
  UserResource = 100
  def addResource(*a,**k): pass
  def adjustSize(*a,**k): pass
  def allFormats(*a,**k): pass
  def availableRedoSteps(*a,**k): pass
  def availableUndoSteps(*a,**k): pass
  def begin(*a,**k): pass
  def blockCount(*a,**k): pass
  def blockCountChanged(*a,**k): pass
  def characterAt(*a,**k): pass
  def characterCount(*a,**k): pass
  def clear(*a,**k): pass
  def clearUndoRedoStacks(*a,**k): pass
  def clone(*a,**k): pass
  def contentsChange(*a,**k): pass
  def contentsChanged(*a,**k): pass
  def createObject(*a,**k): pass
  def cursorPositionChanged(*a,**k): pass
  def defaultCursorMoveStyle(*a,**k): pass
  def defaultFont(*a,**k): pass
  def defaultStyleSheet(*a,**k): pass
  def defaultTextOption(*a,**k): pass
  def documentLayout(*a,**k): pass
  def documentLayoutChanged(*a,**k): pass
  def documentMargin(*a,**k): pass
  def drawContents(*a,**k): pass
  def end(*a,**k): pass
  def find(*a,**k): pass
  def findBlock(*a,**k): pass
  def findBlockByLineNumber(*a,**k): pass
  def findBlockByNumber(*a,**k): pass
  def firstBlock(*a,**k): pass
  def idealWidth(*a,**k): pass
  def indentWidth(*a,**k): pass
  def isEmpty(*a,**k): pass
  def isModified(*a,**k): pass
  def isRedoAvailable(*a,**k): pass
  def isUndoAvailable(*a,**k): pass
  def isUndoRedoEnabled(*a,**k): pass
  def lastBlock(*a,**k): pass
  def lineCount(*a,**k): pass
  def loadResource(*a,**k): pass
  def markContentsDirty(*a,**k): pass
  def maximumBlockCount(*a,**k): pass
  def metaInformation(*a,**k): pass
  def modificationChanged(*a,**k): pass
  def object(*a,**k): pass
  def objectForFormat(*a,**k): pass
  def pageCount(*a,**k): pass
  def pageSize(*a,**k): pass
  def print(*a,**k): pass
  def print_(*a,**k): pass
  def redo(*a,**k): pass
  def redoAvailable(*a,**k): pass
  def resource(*a,**k): pass
  def revision(*a,**k): pass
  def rootFrame(*a,**k): pass
  def setDefaultCursorMoveStyle(*a,**k): pass
  def setDefaultFont(*a,**k): pass
  def setDefaultStyleSheet(*a,**k): pass
  def setDefaultTextOption(*a,**k): pass
  def setDocumentLayout(*a,**k): pass
  def setDocumentMargin(*a,**k): pass
  def setHtml(*a,**k): pass
  def setIndentWidth(*a,**k): pass
  def setMaximumBlockCount(*a,**k): pass
  def setMetaInformation(*a,**k): pass
  def setModified(*a,**k): pass
  def setPageSize(*a,**k): pass
  def setPlainText(*a,**k): pass
  def setTextWidth(*a,**k): pass
  def setUndoRedoEnabled(*a,**k): pass
  def setUseDesignMetrics(*a,**k): pass
  def size(*a,**k): pass
  def textWidth(*a,**k): pass
  def toHtml(*a,**k): pass
  def toPlainText(*a,**k): pass
  def undo(*a,**k): pass
  def undoAvailable(*a,**k): pass
  def undoCommandAdded(*a,**k): pass
  def useDesignMetrics(*a,**k): pass

class QUndoGroup(PyQt4.QtCore.QObject):
  pass

  def activeStack(*a,**k): pass
  def activeStackChanged(*a,**k): pass
  def addStack(*a,**k): pass
  def canRedo(*a,**k): pass
  def canRedoChanged(*a,**k): pass
  def canUndo(*a,**k): pass
  def canUndoChanged(*a,**k): pass
  def cleanChanged(*a,**k): pass
  def createRedoAction(*a,**k): pass
  def createUndoAction(*a,**k): pass
  def indexChanged(*a,**k): pass
  def isClean(*a,**k): pass
  def redo(*a,**k): pass
  def redoText(*a,**k): pass
  def redoTextChanged(*a,**k): pass
  def removeStack(*a,**k): pass
  def setActiveStack(*a,**k): pass
  def stacks(*a,**k): pass
  def undo(*a,**k): pass
  def undoText(*a,**k): pass
  def undoTextChanged(*a,**k): pass

class QUndoStack(PyQt4.QtCore.QObject):
  pass

  def beginMacro(*a,**k): pass
  def canRedo(*a,**k): pass
  def canRedoChanged(*a,**k): pass
  def canUndo(*a,**k): pass
  def canUndoChanged(*a,**k): pass
  def cleanChanged(*a,**k): pass
  def cleanIndex(*a,**k): pass
  def clear(*a,**k): pass
  def command(*a,**k): pass
  def count(*a,**k): pass
  def createRedoAction(*a,**k): pass
  def createUndoAction(*a,**k): pass
  def endMacro(*a,**k): pass
  def index(*a,**k): pass
  def indexChanged(*a,**k): pass
  def isActive(*a,**k): pass
  def isClean(*a,**k): pass
  def push(*a,**k): pass
  def redo(*a,**k): pass
  def redoText(*a,**k): pass
  def redoTextChanged(*a,**k): pass
  def setActive(*a,**k): pass
  def setClean(*a,**k): pass
  def setIndex(*a,**k): pass
  def setUndoLimit(*a,**k): pass
  def text(*a,**k): pass
  def undo(*a,**k): pass
  def undoLimit(*a,**k): pass
  def undoText(*a,**k): pass
  def undoTextChanged(*a,**k): pass

class QActionEvent(PyQt4.QtCore.QEvent):
  pass

  def action(*a,**k): pass
  def before(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QCloseEvent(PyQt4.QtCore.QEvent):
  pass


  def __init__(self, *args, **kwargs): pass


class QInputEvent(PyQt4.QtCore.QEvent):
  pass

  def modifiers(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QContextMenuEvent(QInputEvent):
  pass
  Keyboard = 1
  Mouse = 0
  Other = 2
  def globalPos(*a,**k): pass
  def globalX(*a,**k): pass
  def globalY(*a,**k): pass
  def pos(*a,**k): pass
  def reason(*a,**k): pass
  def x(*a,**k): pass
  def y(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTouchEvent(QInputEvent):
  pass
  TouchPad = 1
  TouchScreen = 0
  def deviceType(*a,**k): pass
  def touchPointStates(*a,**k): pass
  def touchPoints(*a,**k): pass
  def widget(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QKeyEvent(QInputEvent):
  pass

  def count(*a,**k): pass
  def isAutoRepeat(*a,**k): pass
  def key(*a,**k): pass
  def matches(*a,**k): pass
  def nativeModifiers(*a,**k): pass
  def nativeScanCode(*a,**k): pass
  def nativeVirtualKey(*a,**k): pass
  def text(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMouseEvent(QInputEvent):
  pass

  def button(*a,**k): pass
  def buttons(*a,**k): pass
  def globalPos(*a,**k): pass
  def globalX(*a,**k): pass
  def globalY(*a,**k): pass
  def hasExtendedInfo(*a,**k): pass
  def pos(*a,**k): pass
  def posF(*a,**k): pass
  def x(*a,**k): pass
  def y(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTabletEvent(QInputEvent):
  pass
  Airbrush = 3
  Cursor = 2
  Eraser = 3
  FourDMouse = 4
  NoDevice = 0
  Pen = 1
  Puck = 1
  RotationStylus = 6
  Stylus = 2
  UnknownPointer = 0
  XFreeEraser = 5
  def device(*a,**k): pass
  def globalPos(*a,**k): pass
  def globalX(*a,**k): pass
  def globalY(*a,**k): pass
  def hiResGlobalPos(*a,**k): pass
  def hiResGlobalX(*a,**k): pass
  def hiResGlobalY(*a,**k): pass
  def pointerType(*a,**k): pass
  def pos(*a,**k): pass
  def pressure(*a,**k): pass
  def rotation(*a,**k): pass
  def tangentialPressure(*a,**k): pass
  def uniqueId(*a,**k): pass
  def x(*a,**k): pass
  def xTilt(*a,**k): pass
  def y(*a,**k): pass
  def yTilt(*a,**k): pass
  def z(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QWheelEvent(QInputEvent):
  pass

  def buttons(*a,**k): pass
  def delta(*a,**k): pass
  def globalPos(*a,**k): pass
  def globalX(*a,**k): pass
  def globalY(*a,**k): pass
  def orientation(*a,**k): pass
  def pos(*a,**k): pass
  def x(*a,**k): pass
  def y(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QDragLeaveEvent(PyQt4.QtCore.QEvent):
  pass


  def __init__(self, *args, **kwargs): pass


class QFileOpenEvent(PyQt4.QtCore.QEvent):
  pass

  def file(*a,**k): pass
  def openFile(*a,**k): pass
  def url(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QFocusEvent(PyQt4.QtCore.QEvent):
  pass

  def gotFocus(*a,**k): pass
  def lostFocus(*a,**k): pass
  def reason(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGestureEvent(PyQt4.QtCore.QEvent):
  pass

  def activeGestures(*a,**k): pass
  def canceledGestures(*a,**k): pass
  def gesture(*a,**k): pass
  def gestures(*a,**k): pass
  def mapToGraphicsScene(*a,**k): pass
  def widget(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsSceneEvent(PyQt4.QtCore.QEvent):
  pass

  def setWidget(*a,**k): pass
  def widget(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsSceneContextMenuEvent(QGraphicsSceneEvent):
  pass
  Keyboard = 1
  Mouse = 0
  Other = 2
  def modifiers(*a,**k): pass
  def pos(*a,**k): pass
  def reason(*a,**k): pass
  def scenePos(*a,**k): pass
  def screenPos(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsSceneDragDropEvent(QGraphicsSceneEvent):
  pass

  def acceptProposedAction(*a,**k): pass
  def buttons(*a,**k): pass
  def dropAction(*a,**k): pass
  def mimeData(*a,**k): pass
  def modifiers(*a,**k): pass
  def pos(*a,**k): pass
  def possibleActions(*a,**k): pass
  def proposedAction(*a,**k): pass
  def scenePos(*a,**k): pass
  def screenPos(*a,**k): pass
  def setDropAction(*a,**k): pass
  def source(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsSceneHelpEvent(QGraphicsSceneEvent):
  pass

  def scenePos(*a,**k): pass
  def screenPos(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsSceneHoverEvent(QGraphicsSceneEvent):
  pass

  def lastPos(*a,**k): pass
  def lastScenePos(*a,**k): pass
  def lastScreenPos(*a,**k): pass
  def modifiers(*a,**k): pass
  def pos(*a,**k): pass
  def scenePos(*a,**k): pass
  def screenPos(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsSceneMouseEvent(QGraphicsSceneEvent):
  pass

  def button(*a,**k): pass
  def buttonDownPos(*a,**k): pass
  def buttonDownScenePos(*a,**k): pass
  def buttonDownScreenPos(*a,**k): pass
  def buttons(*a,**k): pass
  def lastPos(*a,**k): pass
  def lastScenePos(*a,**k): pass
  def lastScreenPos(*a,**k): pass
  def modifiers(*a,**k): pass
  def pos(*a,**k): pass
  def scenePos(*a,**k): pass
  def screenPos(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsSceneMoveEvent(QGraphicsSceneEvent):
  pass

  def newPos(*a,**k): pass
  def oldPos(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsSceneResizeEvent(QGraphicsSceneEvent):
  pass

  def newSize(*a,**k): pass
  def oldSize(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsSceneWheelEvent(QGraphicsSceneEvent):
  pass

  def buttons(*a,**k): pass
  def delta(*a,**k): pass
  def modifiers(*a,**k): pass
  def orientation(*a,**k): pass
  def pos(*a,**k): pass
  def scenePos(*a,**k): pass
  def screenPos(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QHelpEvent(PyQt4.QtCore.QEvent):
  pass

  def globalPos(*a,**k): pass
  def globalX(*a,**k): pass
  def globalY(*a,**k): pass
  def pos(*a,**k): pass
  def x(*a,**k): pass
  def y(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QHideEvent(PyQt4.QtCore.QEvent):
  pass


  def __init__(self, *args, **kwargs): pass


class QHoverEvent(PyQt4.QtCore.QEvent):
  pass

  def oldPos(*a,**k): pass
  def pos(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QIconDragEvent(PyQt4.QtCore.QEvent):
  pass


  def __init__(self, *args, **kwargs): pass


class QInputMethodEvent(PyQt4.QtCore.QEvent):
  pass
  Cursor = 1
  Language = 2
  Ruby = 3
  Selection = 4
  TextFormat = 0
  def attributes(*a,**k): pass
  def commitString(*a,**k): pass
  def preeditString(*a,**k): pass
  def replacementLength(*a,**k): pass
  def replacementStart(*a,**k): pass
  def setCommitString(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMoveEvent(PyQt4.QtCore.QEvent):
  pass

  def oldPos(*a,**k): pass
  def pos(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPaintEvent(PyQt4.QtCore.QEvent):
  pass

  def rect(*a,**k): pass
  def region(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QResizeEvent(PyQt4.QtCore.QEvent):
  pass

  def oldSize(*a,**k): pass
  def size(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QShortcutEvent(PyQt4.QtCore.QEvent):
  pass

  def isAmbiguous(*a,**k): pass
  def key(*a,**k): pass
  def shortcutId(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QShowEvent(PyQt4.QtCore.QEvent):
  pass


  def __init__(self, *args, **kwargs): pass


class QStatusTipEvent(PyQt4.QtCore.QEvent):
  pass

  def tip(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QWhatsThisClickedEvent(PyQt4.QtCore.QEvent):
  pass

  def href(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QWindowStateChangeEvent(PyQt4.QtCore.QEvent):
  pass

  def oldState(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsItem(object):
  pass
  DeviceCoordinateCache = 2
  ItemAcceptsInputMethod = 4096
  ItemChildAddedChange = 6
  ItemChildRemovedChange = 7
  ItemClipsChildrenToShape = 16
  ItemClipsToShape = 8
  ItemCoordinateCache = 1
  ItemCursorChange = 17
  ItemCursorHasChanged = 18
  ItemDoesntPropagateOpacityToChildren = 128
  ItemEnabledChange = 3
  ItemEnabledHasChanged = 13
  ItemFlagsChange = 21
  ItemFlagsHaveChanged = 22
  ItemHasNoContents = 1024
  ItemIgnoresParentOpacity = 64
  ItemIgnoresTransformations = 32
  ItemIsFocusable = 4
  ItemIsMovable = 1
  ItemIsPanel = 16384
  ItemIsSelectable = 2
  ItemMatrixChange = 1
  ItemNegativeZStacksBehindParent = 8192
  ItemOpacityChange = 25
  ItemOpacityHasChanged = 26
  ItemParentChange = 5
  ItemParentHasChanged = 15
  ItemPositionChange = 0
  ItemPositionHasChanged = 9
  ItemRotationChange = 28
  ItemRotationHasChanged = 29
  ItemScaleChange = 30
  ItemScaleHasChanged = 31
  ItemSceneChange = 11
  ItemSceneHasChanged = 16
  ItemScenePositionHasChanged = 27
  ItemSelectedChange = 4
  ItemSelectedHasChanged = 14
  ItemSendsGeometryChanges = 2048
  ItemSendsScenePositionChanges = 65536
  ItemStacksBehindParent = 256
  ItemToolTipChange = 19
  ItemToolTipHasChanged = 20
  ItemTransformChange = 8
  ItemTransformHasChanged = 10
  ItemTransformOriginPointChange = 32
  ItemTransformOriginPointHasChanged = 33
  ItemUsesExtendedStyleOption = 512
  ItemVisibleChange = 2
  ItemVisibleHasChanged = 12
  ItemZValueChange = 23
  ItemZValueHasChanged = 24
  NoCache = 0
  NonModal = 0
  PanelModal = 1
  SceneModal = 2
  UserType = 65536
  def acceptDrops(*a,**k): pass
  def acceptHoverEvents(*a,**k): pass
  def acceptTouchEvents(*a,**k): pass
  def acceptedMouseButtons(*a,**k): pass
  def acceptsHoverEvents(*a,**k): pass
  def advance(*a,**k): pass
  def boundingRect(*a,**k): pass
  def boundingRegion(*a,**k): pass
  def boundingRegionGranularity(*a,**k): pass
  def cacheMode(*a,**k): pass
  def childItems(*a,**k): pass
  def childrenBoundingRect(*a,**k): pass
  def clearFocus(*a,**k): pass
  def clipPath(*a,**k): pass
  def collidesWithItem(*a,**k): pass
  def collidesWithPath(*a,**k): pass
  def collidingItems(*a,**k): pass
  def commonAncestorItem(*a,**k): pass
  def contains(*a,**k): pass
  def contextMenuEvent(*a,**k): pass
  def cursor(*a,**k): pass
  def data(*a,**k): pass
  def deviceTransform(*a,**k): pass
  def dragEnterEvent(*a,**k): pass
  def dragLeaveEvent(*a,**k): pass
  def dragMoveEvent(*a,**k): pass
  def dropEvent(*a,**k): pass
  def effectiveOpacity(*a,**k): pass
  def ensureVisible(*a,**k): pass
  def filtersChildEvents(*a,**k): pass
  def flags(*a,**k): pass
  def focusInEvent(*a,**k): pass
  def focusItem(*a,**k): pass
  def focusOutEvent(*a,**k): pass
  def focusProxy(*a,**k): pass
  def grabKeyboard(*a,**k): pass
  def grabMouse(*a,**k): pass
  def graphicsEffect(*a,**k): pass
  def group(*a,**k): pass
  def handlesChildEvents(*a,**k): pass
  def hasCursor(*a,**k): pass
  def hasFocus(*a,**k): pass
  def hide(*a,**k): pass
  def hoverEnterEvent(*a,**k): pass
  def hoverLeaveEvent(*a,**k): pass
  def hoverMoveEvent(*a,**k): pass
  def inputMethodEvent(*a,**k): pass
  def inputMethodHints(*a,**k): pass
  def inputMethodQuery(*a,**k): pass
  def installSceneEventFilter(*a,**k): pass
  def isActive(*a,**k): pass
  def isAncestorOf(*a,**k): pass
  def isBlockedByModalPanel(*a,**k): pass
  def isClipped(*a,**k): pass
  def isEnabled(*a,**k): pass
  def isObscured(*a,**k): pass
  def isObscuredBy(*a,**k): pass
  def isPanel(*a,**k): pass
  def isSelected(*a,**k): pass
  def isUnderMouse(*a,**k): pass
  def isVisible(*a,**k): pass
  def isVisibleTo(*a,**k): pass
  def isWidget(*a,**k): pass
  def isWindow(*a,**k): pass
  def itemChange(*a,**k): pass
  def itemTransform(*a,**k): pass
  def keyPressEvent(*a,**k): pass
  def keyReleaseEvent(*a,**k): pass
  def mapFromItem(*a,**k): pass
  def mapFromParent(*a,**k): pass
  def mapFromScene(*a,**k): pass
  def mapRectFromItem(*a,**k): pass
  def mapRectFromParent(*a,**k): pass
  def mapRectFromScene(*a,**k): pass
  def mapRectToItem(*a,**k): pass
  def mapRectToParent(*a,**k): pass
  def mapRectToScene(*a,**k): pass
  def mapToItem(*a,**k): pass
  def mapToParent(*a,**k): pass
  def mapToScene(*a,**k): pass
  def matrix(*a,**k): pass
  def mouseDoubleClickEvent(*a,**k): pass
  def mouseMoveEvent(*a,**k): pass
  def mousePressEvent(*a,**k): pass
  def mouseReleaseEvent(*a,**k): pass
  def moveBy(*a,**k): pass
  def opacity(*a,**k): pass
  def opaqueArea(*a,**k): pass
  def paint(*a,**k): pass
  def panel(*a,**k): pass
  def panelModality(*a,**k): pass
  def parentItem(*a,**k): pass
  def parentObject(*a,**k): pass
  def parentWidget(*a,**k): pass
  def pos(*a,**k): pass
  def prepareGeometryChange(*a,**k): pass
  def removeSceneEventFilter(*a,**k): pass
  def resetMatrix(*a,**k): pass
  def resetTransform(*a,**k): pass
  def rotate(*a,**k): pass
  def rotation(*a,**k): pass
  def scale(*a,**k): pass
  def scene(*a,**k): pass
  def sceneBoundingRect(*a,**k): pass
  def sceneEvent(*a,**k): pass
  def sceneEventFilter(*a,**k): pass
  def sceneMatrix(*a,**k): pass
  def scenePos(*a,**k): pass
  def sceneTransform(*a,**k): pass
  def scroll(*a,**k): pass
  def setAcceptDrops(*a,**k): pass
  def setAcceptHoverEvents(*a,**k): pass
  def setAcceptTouchEvents(*a,**k): pass
  def setAcceptedMouseButtons(*a,**k): pass
  def setAcceptsHoverEvents(*a,**k): pass
  def setActive(*a,**k): pass
  def setBoundingRegionGranularity(*a,**k): pass
  def setCacheMode(*a,**k): pass
  def setCursor(*a,**k): pass
  def setData(*a,**k): pass
  def setEnabled(*a,**k): pass
  def setFiltersChildEvents(*a,**k): pass
  def setFlag(*a,**k): pass
  def setFlags(*a,**k): pass
  def setFocus(*a,**k): pass
  def setFocusProxy(*a,**k): pass
  def setGraphicsEffect(*a,**k): pass
  def setGroup(*a,**k): pass
  def setHandlesChildEvents(*a,**k): pass
  def setInputMethodHints(*a,**k): pass
  def setMatrix(*a,**k): pass
  def setOpacity(*a,**k): pass
  def setPanelModality(*a,**k): pass
  def setParentItem(*a,**k): pass
  def setPos(*a,**k): pass
  def setRotation(*a,**k): pass
  def setScale(*a,**k): pass
  def setSelected(*a,**k): pass
  def setToolTip(*a,**k): pass
  def setTransform(*a,**k): pass
  def setTransformOriginPoint(*a,**k): pass
  def setTransformations(*a,**k): pass
  def setVisible(*a,**k): pass
  def setX(*a,**k): pass
  def setY(*a,**k): pass
  def setZValue(*a,**k): pass
  def shape(*a,**k): pass
  def shear(*a,**k): pass
  def show(*a,**k): pass
  def stackBefore(*a,**k): pass
  def toGraphicsObject(*a,**k): pass
  def toolTip(*a,**k): pass
  def topLevelItem(*a,**k): pass
  def topLevelWidget(*a,**k): pass
  def transform(*a,**k): pass
  def transformOriginPoint(*a,**k): pass
  def transformations(*a,**k): pass
  def translate(*a,**k): pass
  def type(*a,**k): pass
  def ungrabKeyboard(*a,**k): pass
  def ungrabMouse(*a,**k): pass
  def unsetCursor(*a,**k): pass
  def update(*a,**k): pass
  def updateMicroFocus(*a,**k): pass
  def wheelEvent(*a,**k): pass
  def window(*a,**k): pass
  def x(*a,**k): pass
  def y(*a,**k): pass
  def zValue(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsObject(PyQt4.QtCore.QObject):
  pass
  DeviceCoordinateCache = 2
  ItemAcceptsInputMethod = 4096
  ItemChildAddedChange = 6
  ItemChildRemovedChange = 7
  ItemClipsChildrenToShape = 16
  ItemClipsToShape = 8
  ItemCoordinateCache = 1
  ItemCursorChange = 17
  ItemCursorHasChanged = 18
  ItemDoesntPropagateOpacityToChildren = 128
  ItemEnabledChange = 3
  ItemEnabledHasChanged = 13
  ItemFlagsChange = 21
  ItemFlagsHaveChanged = 22
  ItemHasNoContents = 1024
  ItemIgnoresParentOpacity = 64
  ItemIgnoresTransformations = 32
  ItemIsFocusable = 4
  ItemIsMovable = 1
  ItemIsPanel = 16384
  ItemIsSelectable = 2
  ItemMatrixChange = 1
  ItemNegativeZStacksBehindParent = 8192
  ItemOpacityChange = 25
  ItemOpacityHasChanged = 26
  ItemParentChange = 5
  ItemParentHasChanged = 15
  ItemPositionChange = 0
  ItemPositionHasChanged = 9
  ItemRotationChange = 28
  ItemRotationHasChanged = 29
  ItemScaleChange = 30
  ItemScaleHasChanged = 31
  ItemSceneChange = 11
  ItemSceneHasChanged = 16
  ItemScenePositionHasChanged = 27
  ItemSelectedChange = 4
  ItemSelectedHasChanged = 14
  ItemSendsGeometryChanges = 2048
  ItemSendsScenePositionChanges = 65536
  ItemStacksBehindParent = 256
  ItemToolTipChange = 19
  ItemToolTipHasChanged = 20
  ItemTransformChange = 8
  ItemTransformHasChanged = 10
  ItemTransformOriginPointChange = 32
  ItemTransformOriginPointHasChanged = 33
  ItemUsesExtendedStyleOption = 512
  ItemVisibleChange = 2
  ItemVisibleHasChanged = 12
  ItemZValueChange = 23
  ItemZValueHasChanged = 24
  NoCache = 0
  NonModal = 0
  PanelModal = 1
  SceneModal = 2
  UserType = 65536
  def acceptDrops(*a,**k): pass
  def acceptHoverEvents(*a,**k): pass
  def acceptTouchEvents(*a,**k): pass
  def acceptedMouseButtons(*a,**k): pass
  def acceptsHoverEvents(*a,**k): pass
  def advance(*a,**k): pass
  def boundingRect(*a,**k): pass
  def boundingRegion(*a,**k): pass
  def boundingRegionGranularity(*a,**k): pass
  def cacheMode(*a,**k): pass
  def childItems(*a,**k): pass
  def childrenBoundingRect(*a,**k): pass
  def clearFocus(*a,**k): pass
  def clipPath(*a,**k): pass
  def collidesWithItem(*a,**k): pass
  def collidesWithPath(*a,**k): pass
  def collidingItems(*a,**k): pass
  def commonAncestorItem(*a,**k): pass
  def contains(*a,**k): pass
  def contextMenuEvent(*a,**k): pass
  def cursor(*a,**k): pass
  def data(*a,**k): pass
  def deviceTransform(*a,**k): pass
  def dragEnterEvent(*a,**k): pass
  def dragLeaveEvent(*a,**k): pass
  def dragMoveEvent(*a,**k): pass
  def dropEvent(*a,**k): pass
  def effectiveOpacity(*a,**k): pass
  def enabledChanged(*a,**k): pass
  def ensureVisible(*a,**k): pass
  def filtersChildEvents(*a,**k): pass
  def flags(*a,**k): pass
  def focusInEvent(*a,**k): pass
  def focusItem(*a,**k): pass
  def focusOutEvent(*a,**k): pass
  def focusProxy(*a,**k): pass
  def grabGesture(*a,**k): pass
  def grabKeyboard(*a,**k): pass
  def grabMouse(*a,**k): pass
  def graphicsEffect(*a,**k): pass
  def group(*a,**k): pass
  def handlesChildEvents(*a,**k): pass
  def hasCursor(*a,**k): pass
  def hasFocus(*a,**k): pass
  def hide(*a,**k): pass
  def hoverEnterEvent(*a,**k): pass
  def hoverLeaveEvent(*a,**k): pass
  def hoverMoveEvent(*a,**k): pass
  def inputMethodEvent(*a,**k): pass
  def inputMethodHints(*a,**k): pass
  def inputMethodQuery(*a,**k): pass
  def installSceneEventFilter(*a,**k): pass
  def isActive(*a,**k): pass
  def isAncestorOf(*a,**k): pass
  def isBlockedByModalPanel(*a,**k): pass
  def isClipped(*a,**k): pass
  def isEnabled(*a,**k): pass
  def isObscured(*a,**k): pass
  def isObscuredBy(*a,**k): pass
  def isPanel(*a,**k): pass
  def isSelected(*a,**k): pass
  def isUnderMouse(*a,**k): pass
  def isVisible(*a,**k): pass
  def isVisibleTo(*a,**k): pass
  def isWidget(*a,**k): pass
  def isWindow(*a,**k): pass
  def itemChange(*a,**k): pass
  def itemTransform(*a,**k): pass
  def keyPressEvent(*a,**k): pass
  def keyReleaseEvent(*a,**k): pass
  def mapFromItem(*a,**k): pass
  def mapFromParent(*a,**k): pass
  def mapFromScene(*a,**k): pass
  def mapRectFromItem(*a,**k): pass
  def mapRectFromParent(*a,**k): pass
  def mapRectFromScene(*a,**k): pass
  def mapRectToItem(*a,**k): pass
  def mapRectToParent(*a,**k): pass
  def mapRectToScene(*a,**k): pass
  def mapToItem(*a,**k): pass
  def mapToParent(*a,**k): pass
  def mapToScene(*a,**k): pass
  def matrix(*a,**k): pass
  def mouseDoubleClickEvent(*a,**k): pass
  def mouseMoveEvent(*a,**k): pass
  def mousePressEvent(*a,**k): pass
  def mouseReleaseEvent(*a,**k): pass
  def moveBy(*a,**k): pass
  def opacity(*a,**k): pass
  def opacityChanged(*a,**k): pass
  def opaqueArea(*a,**k): pass
  def paint(*a,**k): pass
  def panel(*a,**k): pass
  def panelModality(*a,**k): pass
  def parentChanged(*a,**k): pass
  def parentItem(*a,**k): pass
  def parentObject(*a,**k): pass
  def parentWidget(*a,**k): pass
  def pos(*a,**k): pass
  def prepareGeometryChange(*a,**k): pass
  def removeSceneEventFilter(*a,**k): pass
  def resetMatrix(*a,**k): pass
  def resetTransform(*a,**k): pass
  def rotate(*a,**k): pass
  def rotation(*a,**k): pass
  def rotationChanged(*a,**k): pass
  def scale(*a,**k): pass
  def scaleChanged(*a,**k): pass
  def scene(*a,**k): pass
  def sceneBoundingRect(*a,**k): pass
  def sceneEvent(*a,**k): pass
  def sceneEventFilter(*a,**k): pass
  def sceneMatrix(*a,**k): pass
  def scenePos(*a,**k): pass
  def sceneTransform(*a,**k): pass
  def scroll(*a,**k): pass
  def setAcceptDrops(*a,**k): pass
  def setAcceptHoverEvents(*a,**k): pass
  def setAcceptTouchEvents(*a,**k): pass
  def setAcceptedMouseButtons(*a,**k): pass
  def setAcceptsHoverEvents(*a,**k): pass
  def setActive(*a,**k): pass
  def setBoundingRegionGranularity(*a,**k): pass
  def setCacheMode(*a,**k): pass
  def setCursor(*a,**k): pass
  def setData(*a,**k): pass
  def setEnabled(*a,**k): pass
  def setFiltersChildEvents(*a,**k): pass
  def setFlag(*a,**k): pass
  def setFlags(*a,**k): pass
  def setFocus(*a,**k): pass
  def setFocusProxy(*a,**k): pass
  def setGraphicsEffect(*a,**k): pass
  def setGroup(*a,**k): pass
  def setHandlesChildEvents(*a,**k): pass
  def setInputMethodHints(*a,**k): pass
  def setMatrix(*a,**k): pass
  def setOpacity(*a,**k): pass
  def setPanelModality(*a,**k): pass
  def setParentItem(*a,**k): pass
  def setPos(*a,**k): pass
  def setRotation(*a,**k): pass
  def setScale(*a,**k): pass
  def setSelected(*a,**k): pass
  def setToolTip(*a,**k): pass
  def setTransform(*a,**k): pass
  def setTransformOriginPoint(*a,**k): pass
  def setTransformations(*a,**k): pass
  def setVisible(*a,**k): pass
  def setX(*a,**k): pass
  def setY(*a,**k): pass
  def setZValue(*a,**k): pass
  def shape(*a,**k): pass
  def shear(*a,**k): pass
  def show(*a,**k): pass
  def stackBefore(*a,**k): pass
  def toGraphicsObject(*a,**k): pass
  def toolTip(*a,**k): pass
  def topLevelItem(*a,**k): pass
  def topLevelWidget(*a,**k): pass
  def transform(*a,**k): pass
  def transformOriginPoint(*a,**k): pass
  def transformations(*a,**k): pass
  def translate(*a,**k): pass
  def type(*a,**k): pass
  def ungrabGesture(*a,**k): pass
  def ungrabKeyboard(*a,**k): pass
  def ungrabMouse(*a,**k): pass
  def unsetCursor(*a,**k): pass
  def update(*a,**k): pass
  def updateMicroFocus(*a,**k): pass
  def visibleChanged(*a,**k): pass
  def wheelEvent(*a,**k): pass
  def window(*a,**k): pass
  def x(*a,**k): pass
  def xChanged(*a,**k): pass
  def y(*a,**k): pass
  def yChanged(*a,**k): pass
  def zChanged(*a,**k): pass
  def zValue(*a,**k): pass

class QGraphicsTextItem(QGraphicsObject):
  pass

  def adjustSize(*a,**k): pass
  def defaultTextColor(*a,**k): pass
  def document(*a,**k): pass
  def font(*a,**k): pass
  def linkActivated(*a,**k): pass
  def linkHovered(*a,**k): pass
  def openExternalLinks(*a,**k): pass
  def setDefaultTextColor(*a,**k): pass
  def setDocument(*a,**k): pass
  def setFont(*a,**k): pass
  def setHtml(*a,**k): pass
  def setOpenExternalLinks(*a,**k): pass
  def setPlainText(*a,**k): pass
  def setTabChangesFocus(*a,**k): pass
  def setTextCursor(*a,**k): pass
  def setTextInteractionFlags(*a,**k): pass
  def setTextWidth(*a,**k): pass
  def tabChangesFocus(*a,**k): pass
  def textCursor(*a,**k): pass
  def textInteractionFlags(*a,**k): pass
  def textWidth(*a,**k): pass
  def toHtml(*a,**k): pass
  def toPlainText(*a,**k): pass

class QAbstractGraphicsShapeItem(QGraphicsItem):
  pass

  def brush(*a,**k): pass
  def pen(*a,**k): pass
  def setBrush(*a,**k): pass
  def setPen(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsEllipseItem(QAbstractGraphicsShapeItem):
  pass

  def rect(*a,**k): pass
  def setRect(*a,**k): pass
  def setSpanAngle(*a,**k): pass
  def setStartAngle(*a,**k): pass
  def spanAngle(*a,**k): pass
  def startAngle(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsPathItem(QAbstractGraphicsShapeItem):
  pass

  def path(*a,**k): pass
  def setPath(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsPolygonItem(QAbstractGraphicsShapeItem):
  pass

  def fillRule(*a,**k): pass
  def polygon(*a,**k): pass
  def setFillRule(*a,**k): pass
  def setPolygon(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsRectItem(QAbstractGraphicsShapeItem):
  pass

  def rect(*a,**k): pass
  def setRect(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsSimpleTextItem(QAbstractGraphicsShapeItem):
  pass

  def font(*a,**k): pass
  def setFont(*a,**k): pass
  def setText(*a,**k): pass
  def text(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsItemGroup(QGraphicsItem):
  pass

  def addToGroup(*a,**k): pass
  def removeFromGroup(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsLineItem(QGraphicsItem):
  pass

  def line(*a,**k): pass
  def pen(*a,**k): pass
  def setLine(*a,**k): pass
  def setPen(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsPixmapItem(QGraphicsItem):
  pass
  BoundingRectShape = 1
  HeuristicMaskShape = 2
  MaskShape = 0
  def offset(*a,**k): pass
  def pixmap(*a,**k): pass
  def setOffset(*a,**k): pass
  def setPixmap(*a,**k): pass
  def setShapeMode(*a,**k): pass
  def setTransformationMode(*a,**k): pass
  def shapeMode(*a,**k): pass
  def transformationMode(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QLayoutItem(object):
  pass

  def alignment(*a,**k): pass
  def controlTypes(*a,**k): pass
  def expandingDirections(*a,**k): pass
  def geometry(*a,**k): pass
  def hasHeightForWidth(*a,**k): pass
  def heightForWidth(*a,**k): pass
  def invalidate(*a,**k): pass
  def isEmpty(*a,**k): pass
  def layout(*a,**k): pass
  def maximumSize(*a,**k): pass
  def minimumHeightForWidth(*a,**k): pass
  def minimumSize(*a,**k): pass
  def setAlignment(*a,**k): pass
  def setGeometry(*a,**k): pass
  def sizeHint(*a,**k): pass
  def spacerItem(*a,**k): pass
  def widget(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QLayout(PyQt4.QtCore.QObject):
  pass
  SetDefaultConstraint = 0
  SetFixedSize = 3
  SetMaximumSize = 4
  SetMinAndMaxSize = 5
  SetMinimumSize = 2
  SetNoConstraint = 1
  def activate(*a,**k): pass
  def addChildLayout(*a,**k): pass
  def addChildWidget(*a,**k): pass
  def addItem(*a,**k): pass
  def addWidget(*a,**k): pass
  def alignment(*a,**k): pass
  def alignmentRect(*a,**k): pass
  def closestAcceptableSize(*a,**k): pass
  def contentsMargins(*a,**k): pass
  def contentsRect(*a,**k): pass
  def controlTypes(*a,**k): pass
  def count(*a,**k): pass
  def expandingDirections(*a,**k): pass
  def geometry(*a,**k): pass
  def getContentsMargins(*a,**k): pass
  def hasHeightForWidth(*a,**k): pass
  def heightForWidth(*a,**k): pass
  def indexOf(*a,**k): pass
  def invalidate(*a,**k): pass
  def isEmpty(*a,**k): pass
  def isEnabled(*a,**k): pass
  def itemAt(*a,**k): pass
  def layout(*a,**k): pass
  def margin(*a,**k): pass
  def maximumSize(*a,**k): pass
  def menuBar(*a,**k): pass
  def minimumHeightForWidth(*a,**k): pass
  def minimumSize(*a,**k): pass
  def parentWidget(*a,**k): pass
  def removeItem(*a,**k): pass
  def removeWidget(*a,**k): pass
  def setAlignment(*a,**k): pass
  def setContentsMargins(*a,**k): pass
  def setEnabled(*a,**k): pass
  def setGeometry(*a,**k): pass
  def setMargin(*a,**k): pass
  def setMenuBar(*a,**k): pass
  def setSizeConstraint(*a,**k): pass
  def setSpacing(*a,**k): pass
  def sizeConstraint(*a,**k): pass
  def sizeHint(*a,**k): pass
  def spacerItem(*a,**k): pass
  def spacing(*a,**k): pass
  def takeAt(*a,**k): pass
  def totalHeightForWidth(*a,**k): pass
  def totalMaximumSize(*a,**k): pass
  def totalMinimumSize(*a,**k): pass
  def totalSizeHint(*a,**k): pass
  def update(*a,**k): pass
  def widget(*a,**k): pass
  def widgetEvent(*a,**k): pass

class QBoxLayout(QLayout):
  pass
  BottomToTop = 3
  Down = 2
  LeftToRight = 0
  RightToLeft = 1
  TopToBottom = 2
  Up = 3
  def addLayout(*a,**k): pass
  def addSpacerItem(*a,**k): pass
  def addSpacing(*a,**k): pass
  def addStretch(*a,**k): pass
  def addStrut(*a,**k): pass
  def direction(*a,**k): pass
  def insertItem(*a,**k): pass
  def insertLayout(*a,**k): pass
  def insertSpacerItem(*a,**k): pass
  def insertSpacing(*a,**k): pass
  def insertStretch(*a,**k): pass
  def insertWidget(*a,**k): pass
  def setDirection(*a,**k): pass
  def setStretch(*a,**k): pass
  def setStretchFactor(*a,**k): pass
  def stretch(*a,**k): pass

class QHBoxLayout(QBoxLayout):
  pass



class QVBoxLayout(QBoxLayout):
  pass



class QFormLayout(QLayout):
  pass
  AllNonFixedFieldsGrow = 2
  DontWrapRows = 0
  ExpandingFieldsGrow = 1
  FieldRole = 1
  FieldsStayAtSizeHint = 0
  LabelRole = 0
  SpanningRole = 2
  WrapAllRows = 2
  WrapLongRows = 1
  def addRow(*a,**k): pass
  def fieldGrowthPolicy(*a,**k): pass
  def formAlignment(*a,**k): pass
  def getItemPosition(*a,**k): pass
  def getLayoutPosition(*a,**k): pass
  def getWidgetPosition(*a,**k): pass
  def horizontalSpacing(*a,**k): pass
  def insertRow(*a,**k): pass
  def labelAlignment(*a,**k): pass
  def labelForField(*a,**k): pass
  def rowCount(*a,**k): pass
  def rowWrapPolicy(*a,**k): pass
  def setFieldGrowthPolicy(*a,**k): pass
  def setFormAlignment(*a,**k): pass
  def setHorizontalSpacing(*a,**k): pass
  def setItem(*a,**k): pass
  def setLabelAlignment(*a,**k): pass
  def setLayout(*a,**k): pass
  def setRowWrapPolicy(*a,**k): pass
  def setVerticalSpacing(*a,**k): pass
  def setWidget(*a,**k): pass
  def verticalSpacing(*a,**k): pass

class QGridLayout(QLayout):
  pass

  def addLayout(*a,**k): pass
  def cellRect(*a,**k): pass
  def columnCount(*a,**k): pass
  def columnMinimumWidth(*a,**k): pass
  def columnStretch(*a,**k): pass
  def getItemPosition(*a,**k): pass
  def horizontalSpacing(*a,**k): pass
  def itemAtPosition(*a,**k): pass
  def originCorner(*a,**k): pass
  def rowCount(*a,**k): pass
  def rowMinimumHeight(*a,**k): pass
  def rowStretch(*a,**k): pass
  def setColumnMinimumWidth(*a,**k): pass
  def setColumnStretch(*a,**k): pass
  def setDefaultPositioning(*a,**k): pass
  def setHorizontalSpacing(*a,**k): pass
  def setOriginCorner(*a,**k): pass
  def setRowMinimumHeight(*a,**k): pass
  def setRowStretch(*a,**k): pass
  def setVerticalSpacing(*a,**k): pass
  def verticalSpacing(*a,**k): pass

class QStackedLayout(QLayout):
  pass
  StackAll = 1
  StackOne = 0
  def currentChanged(*a,**k): pass
  def currentIndex(*a,**k): pass
  def currentWidget(*a,**k): pass
  def insertWidget(*a,**k): pass
  def setCurrentIndex(*a,**k): pass
  def setCurrentWidget(*a,**k): pass
  def setStackingMode(*a,**k): pass
  def stackingMode(*a,**k): pass
  def widgetRemoved(*a,**k): pass

class QSpacerItem(QLayoutItem):
  pass

  def changeSize(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QWidgetItem(QLayoutItem):
  pass


  def __init__(self, *args, **kwargs): pass


class QGestureRecognizer(object):
  pass
  CancelGesture = 16
  ConsumeEventHint = 256
  FinishGesture = 8
  Ignore = 1
  MayBeGesture = 2
  TriggerGesture = 4
  def create(*a,**k): pass
  def recognize(*a,**k): pass
  def registerRecognizer(*a,**k): pass
  def reset(*a,**k): pass
  def unregisterRecognizer(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsLayoutItem(object):
  pass

  def contentsRect(*a,**k): pass
  def effectiveSizeHint(*a,**k): pass
  def geometry(*a,**k): pass
  def getContentsMargins(*a,**k): pass
  def graphicsItem(*a,**k): pass
  def isLayout(*a,**k): pass
  def maximumHeight(*a,**k): pass
  def maximumSize(*a,**k): pass
  def maximumWidth(*a,**k): pass
  def minimumHeight(*a,**k): pass
  def minimumSize(*a,**k): pass
  def minimumWidth(*a,**k): pass
  def ownedByLayout(*a,**k): pass
  def parentLayoutItem(*a,**k): pass
  def preferredHeight(*a,**k): pass
  def preferredSize(*a,**k): pass
  def preferredWidth(*a,**k): pass
  def setGeometry(*a,**k): pass
  def setGraphicsItem(*a,**k): pass
  def setMaximumHeight(*a,**k): pass
  def setMaximumSize(*a,**k): pass
  def setMaximumWidth(*a,**k): pass
  def setMinimumHeight(*a,**k): pass
  def setMinimumSize(*a,**k): pass
  def setMinimumWidth(*a,**k): pass
  def setOwnedByLayout(*a,**k): pass
  def setParentLayoutItem(*a,**k): pass
  def setPreferredHeight(*a,**k): pass
  def setPreferredSize(*a,**k): pass
  def setPreferredWidth(*a,**k): pass
  def setSizePolicy(*a,**k): pass
  def sizeHint(*a,**k): pass
  def sizePolicy(*a,**k): pass
  def updateGeometry(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsWidget(QGraphicsObject):
  pass

  def actions(*a,**k): pass
  def addAction(*a,**k): pass
  def addActions(*a,**k): pass
  def adjustSize(*a,**k): pass
  def autoFillBackground(*a,**k): pass
  def changeEvent(*a,**k): pass
  def close(*a,**k): pass
  def closeEvent(*a,**k): pass
  def contentsRect(*a,**k): pass
  def effectiveSizeHint(*a,**k): pass
  def focusNextPrevChild(*a,**k): pass
  def focusPolicy(*a,**k): pass
  def focusWidget(*a,**k): pass
  def font(*a,**k): pass
  def geometry(*a,**k): pass
  def geometryChanged(*a,**k): pass
  def getContentsMargins(*a,**k): pass
  def getWindowFrameMargins(*a,**k): pass
  def grabKeyboardEvent(*a,**k): pass
  def grabMouseEvent(*a,**k): pass
  def grabShortcut(*a,**k): pass
  def graphicsItem(*a,**k): pass
  def hideEvent(*a,**k): pass
  def initStyleOption(*a,**k): pass
  def insertAction(*a,**k): pass
  def insertActions(*a,**k): pass
  def isActiveWindow(*a,**k): pass
  def isLayout(*a,**k): pass
  def layout(*a,**k): pass
  def layoutDirection(*a,**k): pass
  def maximumHeight(*a,**k): pass
  def maximumSize(*a,**k): pass
  def maximumWidth(*a,**k): pass
  def minimumHeight(*a,**k): pass
  def minimumSize(*a,**k): pass
  def minimumWidth(*a,**k): pass
  def moveEvent(*a,**k): pass
  def ownedByLayout(*a,**k): pass
  def paintWindowFrame(*a,**k): pass
  def palette(*a,**k): pass
  def parentLayoutItem(*a,**k): pass
  def polishEvent(*a,**k): pass
  def preferredHeight(*a,**k): pass
  def preferredSize(*a,**k): pass
  def preferredWidth(*a,**k): pass
  def rect(*a,**k): pass
  def releaseShortcut(*a,**k): pass
  def removeAction(*a,**k): pass
  def resize(*a,**k): pass
  def resizeEvent(*a,**k): pass
  def setAttribute(*a,**k): pass
  def setAutoFillBackground(*a,**k): pass
  def setContentsMargins(*a,**k): pass
  def setFocusPolicy(*a,**k): pass
  def setFont(*a,**k): pass
  def setGeometry(*a,**k): pass
  def setGraphicsItem(*a,**k): pass
  def setLayout(*a,**k): pass
  def setLayoutDirection(*a,**k): pass
  def setMaximumHeight(*a,**k): pass
  def setMaximumSize(*a,**k): pass
  def setMaximumWidth(*a,**k): pass
  def setMinimumHeight(*a,**k): pass
  def setMinimumSize(*a,**k): pass
  def setMinimumWidth(*a,**k): pass
  def setOwnedByLayout(*a,**k): pass
  def setPalette(*a,**k): pass
  def setParentLayoutItem(*a,**k): pass
  def setPreferredHeight(*a,**k): pass
  def setPreferredSize(*a,**k): pass
  def setPreferredWidth(*a,**k): pass
  def setShortcutAutoRepeat(*a,**k): pass
  def setShortcutEnabled(*a,**k): pass
  def setSizePolicy(*a,**k): pass
  def setStyle(*a,**k): pass
  def setTabOrder(*a,**k): pass
  def setWindowFlags(*a,**k): pass
  def setWindowFrameMargins(*a,**k): pass
  def setWindowTitle(*a,**k): pass
  def showEvent(*a,**k): pass
  def size(*a,**k): pass
  def sizeHint(*a,**k): pass
  def sizePolicy(*a,**k): pass
  def style(*a,**k): pass
  def testAttribute(*a,**k): pass
  def ungrabKeyboardEvent(*a,**k): pass
  def ungrabMouseEvent(*a,**k): pass
  def unsetLayoutDirection(*a,**k): pass
  def unsetWindowFrameMargins(*a,**k): pass
  def updateGeometry(*a,**k): pass
  def windowFlags(*a,**k): pass
  def windowFrameEvent(*a,**k): pass
  def windowFrameGeometry(*a,**k): pass
  def windowFrameRect(*a,**k): pass
  def windowFrameSectionAt(*a,**k): pass
  def windowTitle(*a,**k): pass
  def windowType(*a,**k): pass

class QGraphicsProxyWidget(QGraphicsWidget):
  pass

  def createProxyForChildWidget(*a,**k): pass
  def newProxyWidget(*a,**k): pass
  def setWidget(*a,**k): pass
  def subWidgetRect(*a,**k): pass
  def widget(*a,**k): pass

class QGraphicsLayout(QGraphicsLayoutItem):
  pass

  def activate(*a,**k): pass
  def addChildLayoutItem(*a,**k): pass
  def count(*a,**k): pass
  def invalidate(*a,**k): pass
  def isActivated(*a,**k): pass
  def itemAt(*a,**k): pass
  def removeAt(*a,**k): pass
  def setContentsMargins(*a,**k): pass
  def widgetEvent(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsAnchorLayout(QGraphicsLayout):
  pass

  def addAnchor(*a,**k): pass
  def addAnchors(*a,**k): pass
  def addCornerAnchors(*a,**k): pass
  def anchor(*a,**k): pass
  def horizontalSpacing(*a,**k): pass
  def setHorizontalSpacing(*a,**k): pass
  def setSpacing(*a,**k): pass
  def setVerticalSpacing(*a,**k): pass
  def verticalSpacing(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsGridLayout(QGraphicsLayout):
  pass

  def addItem(*a,**k): pass
  def alignment(*a,**k): pass
  def columnAlignment(*a,**k): pass
  def columnCount(*a,**k): pass
  def columnMaximumWidth(*a,**k): pass
  def columnMinimumWidth(*a,**k): pass
  def columnPreferredWidth(*a,**k): pass
  def columnSpacing(*a,**k): pass
  def columnStretchFactor(*a,**k): pass
  def horizontalSpacing(*a,**k): pass
  def removeItem(*a,**k): pass
  def rowAlignment(*a,**k): pass
  def rowCount(*a,**k): pass
  def rowMaximumHeight(*a,**k): pass
  def rowMinimumHeight(*a,**k): pass
  def rowPreferredHeight(*a,**k): pass
  def rowSpacing(*a,**k): pass
  def rowStretchFactor(*a,**k): pass
  def setAlignment(*a,**k): pass
  def setColumnAlignment(*a,**k): pass
  def setColumnFixedWidth(*a,**k): pass
  def setColumnMaximumWidth(*a,**k): pass
  def setColumnMinimumWidth(*a,**k): pass
  def setColumnPreferredWidth(*a,**k): pass
  def setColumnSpacing(*a,**k): pass
  def setColumnStretchFactor(*a,**k): pass
  def setHorizontalSpacing(*a,**k): pass
  def setRowAlignment(*a,**k): pass
  def setRowFixedHeight(*a,**k): pass
  def setRowMaximumHeight(*a,**k): pass
  def setRowMinimumHeight(*a,**k): pass
  def setRowPreferredHeight(*a,**k): pass
  def setRowSpacing(*a,**k): pass
  def setRowStretchFactor(*a,**k): pass
  def setSpacing(*a,**k): pass
  def setVerticalSpacing(*a,**k): pass
  def verticalSpacing(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGraphicsLinearLayout(QGraphicsLayout):
  pass

  def addItem(*a,**k): pass
  def addStretch(*a,**k): pass
  def alignment(*a,**k): pass
  def insertItem(*a,**k): pass
  def insertStretch(*a,**k): pass
  def itemSpacing(*a,**k): pass
  def orientation(*a,**k): pass
  def removeItem(*a,**k): pass
  def setAlignment(*a,**k): pass
  def setItemSpacing(*a,**k): pass
  def setOrientation(*a,**k): pass
  def setSpacing(*a,**k): pass
  def setStretchFactor(*a,**k): pass
  def spacing(*a,**k): pass
  def stretchFactor(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QIcon(object):
  pass
  Active = 2
  Disabled = 1
  Normal = 0
  Off = 1
  On = 0
  Selected = 3
  def actualSize(*a,**k): pass
  def addFile(*a,**k): pass
  def addPixmap(*a,**k): pass
  def availableSizes(*a,**k): pass
  def cacheKey(*a,**k): pass
  def fromTheme(*a,**k): pass
  def hasThemeIcon(*a,**k): pass
  def isDetached(*a,**k): pass
  def isNull(*a,**k): pass
  def name(*a,**k): pass
  def paint(*a,**k): pass
  def pixmap(*a,**k): pass
  def serialNumber(*a,**k): pass
  def setThemeName(*a,**k): pass
  def setThemeSearchPaths(*a,**k): pass
  def swap(*a,**k): pass
  def themeName(*a,**k): pass
  def themeSearchPaths(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QIconEngine(object):
  pass

  def actualSize(*a,**k): pass
  def addFile(*a,**k): pass
  def addPixmap(*a,**k): pass
  def paint(*a,**k): pass
  def pixmap(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QIconEngineV2(QIconEngine):
  pass
  AvailableSizesHook = 1
  IconNameHook = 2
  def availableSizes(*a,**k): pass
  def clone(*a,**k): pass
  def iconName(*a,**k): pass
  def key(*a,**k): pass
  def read(*a,**k): pass
  def write(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QItemEditorCreatorBase(object):
  pass

  def createWidget(*a,**k): pass
  def valuePropertyName(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QItemEditorFactory(object):
  pass

  def createEditor(*a,**k): pass
  def defaultFactory(*a,**k): pass
  def registerEditor(*a,**k): pass
  def setDefaultFactory(*a,**k): pass
  def valuePropertyName(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QListWidgetItem(object):
  pass
  Type = 0
  UserType = 1000
  def background(*a,**k): pass
  def backgroundColor(*a,**k): pass
  def checkState(*a,**k): pass
  def clone(*a,**k): pass
  def data(*a,**k): pass
  def flags(*a,**k): pass
  def font(*a,**k): pass
  def foreground(*a,**k): pass
  def icon(*a,**k): pass
  def isHidden(*a,**k): pass
  def isSelected(*a,**k): pass
  def listWidget(*a,**k): pass
  def read(*a,**k): pass
  def setBackground(*a,**k): pass
  def setBackgroundColor(*a,**k): pass
  def setCheckState(*a,**k): pass
  def setData(*a,**k): pass
  def setFlags(*a,**k): pass
  def setFont(*a,**k): pass
  def setForeground(*a,**k): pass
  def setHidden(*a,**k): pass
  def setIcon(*a,**k): pass
  def setSelected(*a,**k): pass
  def setSizeHint(*a,**k): pass
  def setStatusTip(*a,**k): pass
  def setText(*a,**k): pass
  def setTextAlignment(*a,**k): pass
  def setTextColor(*a,**k): pass
  def setToolTip(*a,**k): pass
  def setWhatsThis(*a,**k): pass
  def sizeHint(*a,**k): pass
  def statusTip(*a,**k): pass
  def text(*a,**k): pass
  def textAlignment(*a,**k): pass
  def textColor(*a,**k): pass
  def toolTip(*a,**k): pass
  def type(*a,**k): pass
  def whatsThis(*a,**k): pass
  def write(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QStandardItem(object):
  pass
  Type = 0
  UserType = 1000
  def accessibleDescription(*a,**k): pass
  def accessibleText(*a,**k): pass
  def appendColumn(*a,**k): pass
  def appendRow(*a,**k): pass
  def appendRows(*a,**k): pass
  def background(*a,**k): pass
  def checkState(*a,**k): pass
  def child(*a,**k): pass
  def clone(*a,**k): pass
  def column(*a,**k): pass
  def columnCount(*a,**k): pass
  def data(*a,**k): pass
  def emitDataChanged(*a,**k): pass
  def flags(*a,**k): pass
  def font(*a,**k): pass
  def foreground(*a,**k): pass
  def hasChildren(*a,**k): pass
  def icon(*a,**k): pass
  def index(*a,**k): pass
  def insertColumn(*a,**k): pass
  def insertColumns(*a,**k): pass
  def insertRow(*a,**k): pass
  def insertRows(*a,**k): pass
  def isCheckable(*a,**k): pass
  def isDragEnabled(*a,**k): pass
  def isDropEnabled(*a,**k): pass
  def isEditable(*a,**k): pass
  def isEnabled(*a,**k): pass
  def isSelectable(*a,**k): pass
  def isTristate(*a,**k): pass
  def model(*a,**k): pass
  def parent(*a,**k): pass
  def read(*a,**k): pass
  def removeColumn(*a,**k): pass
  def removeColumns(*a,**k): pass
  def removeRow(*a,**k): pass
  def removeRows(*a,**k): pass
  def row(*a,**k): pass
  def rowCount(*a,**k): pass
  def setAccessibleDescription(*a,**k): pass
  def setAccessibleText(*a,**k): pass
  def setBackground(*a,**k): pass
  def setCheckState(*a,**k): pass
  def setCheckable(*a,**k): pass
  def setChild(*a,**k): pass
  def setColumnCount(*a,**k): pass
  def setData(*a,**k): pass
  def setDragEnabled(*a,**k): pass
  def setDropEnabled(*a,**k): pass
  def setEditable(*a,**k): pass
  def setEnabled(*a,**k): pass
  def setFlags(*a,**k): pass
  def setFont(*a,**k): pass
  def setForeground(*a,**k): pass
  def setIcon(*a,**k): pass
  def setRowCount(*a,**k): pass
  def setSelectable(*a,**k): pass
  def setSizeHint(*a,**k): pass
  def setStatusTip(*a,**k): pass
  def setText(*a,**k): pass
  def setTextAlignment(*a,**k): pass
  def setToolTip(*a,**k): pass
  def setTristate(*a,**k): pass
  def setWhatsThis(*a,**k): pass
  def sizeHint(*a,**k): pass
  def sortChildren(*a,**k): pass
  def statusTip(*a,**k): pass
  def takeChild(*a,**k): pass
  def takeColumn(*a,**k): pass
  def takeRow(*a,**k): pass
  def text(*a,**k): pass
  def textAlignment(*a,**k): pass
  def toolTip(*a,**k): pass
  def type(*a,**k): pass
  def whatsThis(*a,**k): pass
  def write(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTableWidgetItem(object):
  pass
  Type = 0
  UserType = 1000
  def background(*a,**k): pass
  def backgroundColor(*a,**k): pass
  def checkState(*a,**k): pass
  def clone(*a,**k): pass
  def column(*a,**k): pass
  def data(*a,**k): pass
  def flags(*a,**k): pass
  def font(*a,**k): pass
  def foreground(*a,**k): pass
  def icon(*a,**k): pass
  def isSelected(*a,**k): pass
  def read(*a,**k): pass
  def row(*a,**k): pass
  def setBackground(*a,**k): pass
  def setBackgroundColor(*a,**k): pass
  def setCheckState(*a,**k): pass
  def setData(*a,**k): pass
  def setFlags(*a,**k): pass
  def setFont(*a,**k): pass
  def setForeground(*a,**k): pass
  def setIcon(*a,**k): pass
  def setSelected(*a,**k): pass
  def setSizeHint(*a,**k): pass
  def setStatusTip(*a,**k): pass
  def setText(*a,**k): pass
  def setTextAlignment(*a,**k): pass
  def setTextColor(*a,**k): pass
  def setToolTip(*a,**k): pass
  def setWhatsThis(*a,**k): pass
  def sizeHint(*a,**k): pass
  def statusTip(*a,**k): pass
  def tableWidget(*a,**k): pass
  def text(*a,**k): pass
  def textAlignment(*a,**k): pass
  def textColor(*a,**k): pass
  def toolTip(*a,**k): pass
  def type(*a,**k): pass
  def whatsThis(*a,**k): pass
  def write(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextBlock(object):
  pass

  def begin(*a,**k): pass
  def blockFormat(*a,**k): pass
  def blockFormatIndex(*a,**k): pass
  def blockNumber(*a,**k): pass
  def charFormat(*a,**k): pass
  def charFormatIndex(*a,**k): pass
  def clearLayout(*a,**k): pass
  def contains(*a,**k): pass
  def document(*a,**k): pass
  def end(*a,**k): pass
  def firstLineNumber(*a,**k): pass
  def isValid(*a,**k): pass
  def isVisible(*a,**k): pass
  def layout(*a,**k): pass
  def length(*a,**k): pass
  def lineCount(*a,**k): pass
  def next(*a,**k): pass
  def position(*a,**k): pass
  def previous(*a,**k): pass
  def revision(*a,**k): pass
  def setLineCount(*a,**k): pass
  def setRevision(*a,**k): pass
  def setUserData(*a,**k): pass
  def setUserState(*a,**k): pass
  def setVisible(*a,**k): pass
  def text(*a,**k): pass
  def textDirection(*a,**k): pass
  def textList(*a,**k): pass
  def userData(*a,**k): pass
  def userState(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextBlockUserData(object):
  pass


  def __init__(self, *args, **kwargs): pass


class QTreeWidgetItem(object):
  pass
  DontShowIndicator = 1
  DontShowIndicatorWhenChildless = 2
  ShowIndicator = 0
  Type = 0
  UserType = 1000
  def addChild(*a,**k): pass
  def addChildren(*a,**k): pass
  def background(*a,**k): pass
  def backgroundColor(*a,**k): pass
  def checkState(*a,**k): pass
  def child(*a,**k): pass
  def childCount(*a,**k): pass
  def childIndicatorPolicy(*a,**k): pass
  def clone(*a,**k): pass
  def columnCount(*a,**k): pass
  def data(*a,**k): pass
  def emitDataChanged(*a,**k): pass
  def flags(*a,**k): pass
  def font(*a,**k): pass
  def foreground(*a,**k): pass
  def icon(*a,**k): pass
  def indexOfChild(*a,**k): pass
  def insertChild(*a,**k): pass
  def insertChildren(*a,**k): pass
  def isDisabled(*a,**k): pass
  def isExpanded(*a,**k): pass
  def isFirstColumnSpanned(*a,**k): pass
  def isHidden(*a,**k): pass
  def isSelected(*a,**k): pass
  def parent(*a,**k): pass
  def read(*a,**k): pass
  def removeChild(*a,**k): pass
  def setBackground(*a,**k): pass
  def setBackgroundColor(*a,**k): pass
  def setCheckState(*a,**k): pass
  def setChildIndicatorPolicy(*a,**k): pass
  def setData(*a,**k): pass
  def setDisabled(*a,**k): pass
  def setExpanded(*a,**k): pass
  def setFirstColumnSpanned(*a,**k): pass
  def setFlags(*a,**k): pass
  def setFont(*a,**k): pass
  def setForeground(*a,**k): pass
  def setHidden(*a,**k): pass
  def setIcon(*a,**k): pass
  def setSelected(*a,**k): pass
  def setSizeHint(*a,**k): pass
  def setStatusTip(*a,**k): pass
  def setText(*a,**k): pass
  def setTextAlignment(*a,**k): pass
  def setTextColor(*a,**k): pass
  def setToolTip(*a,**k): pass
  def setWhatsThis(*a,**k): pass
  def sizeHint(*a,**k): pass
  def sortChildren(*a,**k): pass
  def statusTip(*a,**k): pass
  def takeChild(*a,**k): pass
  def takeChildren(*a,**k): pass
  def text(*a,**k): pass
  def textAlignment(*a,**k): pass
  def textColor(*a,**k): pass
  def toolTip(*a,**k): pass
  def treeWidget(*a,**k): pass
  def type(*a,**k): pass
  def whatsThis(*a,**k): pass
  def write(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QUndoCommand(object):
  pass

  def actionText(*a,**k): pass
  def child(*a,**k): pass
  def childCount(*a,**k): pass
  def id(*a,**k): pass
  def mergeWith(*a,**k): pass
  def redo(*a,**k): pass
  def setText(*a,**k): pass
  def text(*a,**k): pass
  def undo(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


