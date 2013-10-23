from __future__ import print_function

import sip

def _mockf(*args, **kwargs): pass


PYQT_VERSION = 264707

PYQT_VERSION_STR = '4.10.3'

QT_VERSION = 264197

QT_VERSION_STR = '4.8.5'

QtCriticalMsg = 2

QtDebugMsg = 0

QtFatalMsg = 3

QtSystemMsg = 2

QtWarningMsg = 1

def QT_TRANSLATE_NOOP(*a,**k): pass

def QT_TR_NOOP(*a,**k): pass

def QT_TR_NOOP_UTF8(*a,**k): pass

def Q_ARG(*a,**k): pass

def Q_CLASSINFO(*a,**k): pass

def Q_ENUMS(*a,**k): pass

def Q_FLAGS(*a,**k): pass

def Q_RETURN_ARG(*a,**k): pass

def SIGNAL(*a,**k): pass

def SLOT(*a,**k): pass

def bin(*a,**k): pass

def bom(*a,**k): pass

def center(*a,**k): pass

def dec(*a,**k): pass

def endl(*a,**k): pass

def fixed(*a,**k): pass

def flush(*a,**k): pass

def forcepoint(*a,**k): pass

def forcesign(*a,**k): pass

def hex(*a,**k): pass

def left(*a,**k): pass

def lowercasebase(*a,**k): pass

def lowercasedigits(*a,**k): pass

def noforcepoint(*a,**k): pass

def noforcesign(*a,**k): pass

def noshowbase(*a,**k): pass

def oct(*a,**k): pass

def pyqtPickleProtocol(*a,**k): pass

def pyqtRemoveInputHook(*a,**k): pass

def pyqtRestoreInputHook(*a,**k): pass

def pyqtSetPickleProtocol(*a,**k): pass

def pyqtSignature(*a,**k): pass

def pyqtSlot(*a,**k): pass

def qAbs(*a,**k): pass

def qAddPostRoutine(*a,**k): pass

def qChecksum(*a,**k): pass

def qCompress(*a,**k): pass

def qCritical(*a,**k): pass

def qDebug(*a,**k): pass

def qErrnoWarning(*a,**k): pass

def qFatal(*a,**k): pass

def qFuzzyCompare(*a,**k): pass

def qInf(*a,**k): pass

def qInstallMsgHandler(*a,**k): pass

def qIsFinite(*a,**k): pass

def qIsInf(*a,**k): pass

def qIsNaN(*a,**k): pass

def qIsNull(*a,**k): pass

def qQNaN(*a,**k): pass

def qRegisterResourceData(*a,**k): pass

def qRemovePostRoutine(*a,**k): pass

def qRound(*a,**k): pass

def qRound64(*a,**k): pass

def qSNaN(*a,**k): pass

def qSetFieldWidth(*a,**k): pass

def qSetPadChar(*a,**k): pass

def qSetRealNumberPrecision(*a,**k): pass

def qSharedBuild(*a,**k): pass

def qSwap(*a,**k): pass

def qUncompress(*a,**k): pass

def qUnregisterResourceData(*a,**k): pass

def qVersion(*a,**k): pass

def qWarning(*a,**k): pass

def qrand(*a,**k): pass

def qsrand(*a,**k): pass

def reset(*a,**k): pass

def right(*a,**k): pass

def scientific(*a,**k): pass

def showbase(*a,**k): pass

def uppercasebase(*a,**k): pass

def uppercasedigits(*a,**k): pass

def ws(*a,**k): pass

class QtMsgType(int):
  pass


  def __init__(self, *args, **kwargs): pass


class QBasicTimer(object):
  pass

  def isActive(*a,**k): pass
  def start(*a,**k): pass
  def stop(*a,**k): pass
  def timerId(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QAbstractFileEngineHandler(object):
  pass

  def create(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QBitArray(object):
  pass

  def at(*a,**k): pass
  def clear(*a,**k): pass
  def clearBit(*a,**k): pass
  def count(*a,**k): pass
  def detach(*a,**k): pass
  def fill(*a,**k): pass
  def isDetached(*a,**k): pass
  def isEmpty(*a,**k): pass
  def isNull(*a,**k): pass
  def resize(*a,**k): pass
  def setBit(*a,**k): pass
  def size(*a,**k): pass
  def swap(*a,**k): pass
  def testBit(*a,**k): pass
  def toggleBit(*a,**k): pass
  def truncate(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QByteArray(object):
  pass

  def append(*a,**k): pass
  def at(*a,**k): pass
  def capacity(*a,**k): pass
  def chop(*a,**k): pass
  def clear(*a,**k): pass
  def contains(*a,**k): pass
  def count(*a,**k): pass
  def data(*a,**k): pass
  def endsWith(*a,**k): pass
  def fill(*a,**k): pass
  def fromBase64(*a,**k): pass
  def fromHex(*a,**k): pass
  def fromPercentEncoding(*a,**k): pass
  def fromRawData(*a,**k): pass
  def indexOf(*a,**k): pass
  def insert(*a,**k): pass
  def isEmpty(*a,**k): pass
  def isNull(*a,**k): pass
  def lastIndexOf(*a,**k): pass
  def left(*a,**k): pass
  def leftJustified(*a,**k): pass
  def length(*a,**k): pass
  def mid(*a,**k): pass
  def number(*a,**k): pass
  def prepend(*a,**k): pass
  def push_back(*a,**k): pass
  def push_front(*a,**k): pass
  def remove(*a,**k): pass
  def repeated(*a,**k): pass
  def replace(*a,**k): pass
  def reserve(*a,**k): pass
  def resize(*a,**k): pass
  def right(*a,**k): pass
  def rightJustified(*a,**k): pass
  def setNum(*a,**k): pass
  def simplified(*a,**k): pass
  def size(*a,**k): pass
  def split(*a,**k): pass
  def squeeze(*a,**k): pass
  def startsWith(*a,**k): pass
  def swap(*a,**k): pass
  def toBase64(*a,**k): pass
  def toDouble(*a,**k): pass
  def toFloat(*a,**k): pass
  def toHex(*a,**k): pass
  def toInt(*a,**k): pass
  def toLong(*a,**k): pass
  def toLongLong(*a,**k): pass
  def toLower(*a,**k): pass
  def toPercentEncoding(*a,**k): pass
  def toShort(*a,**k): pass
  def toUInt(*a,**k): pass
  def toULong(*a,**k): pass
  def toULongLong(*a,**k): pass
  def toUShort(*a,**k): pass
  def toUpper(*a,**k): pass
  def trimmed(*a,**k): pass
  def truncate(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QByteArrayMatcher(object):
  pass

  def indexIn(*a,**k): pass
  def pattern(*a,**k): pass
  def setPattern(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QChar(object):
  pass
  ByteOrderMark = 65279
  ByteOrderSwapped = 65534
  Canonical = 1
  Center = 3
  Circle = 8
  Combining_Above = 230
  Combining_AboveAttached = 214
  Combining_AboveLeft = 228
  Combining_AboveLeftAttached = 212
  Combining_AboveRight = 232
  Combining_AboveRightAttached = 216
  Combining_Below = 220
  Combining_BelowAttached = 202
  Combining_BelowLeft = 218
  Combining_BelowLeftAttached = 200
  Combining_BelowRight = 222
  Combining_BelowRightAttached = 204
  Combining_DoubleAbove = 234
  Combining_DoubleBelow = 233
  Combining_IotaSubscript = 240
  Combining_Left = 224
  Combining_LeftAttached = 208
  Combining_Right = 226
  Combining_RightAttached = 210
  Compat = 16
  DirAL = 13
  DirAN = 5
  DirB = 7
  DirBN = 18
  DirCS = 6
  DirEN = 2
  DirES = 3
  DirET = 4
  DirL = 0
  DirLRE = 11
  DirLRO = 12
  DirNSM = 17
  DirON = 10
  DirPDF = 16
  DirR = 1
  DirRLE = 14
  DirRLO = 15
  DirS = 8
  DirWS = 9
  Dual = 1
  Final = 6
  Font = 2
  Fraction = 17
  Initial = 4
  Isolated = 7
  Letter_Lowercase = 16
  Letter_Modifier = 18
  Letter_Other = 19
  Letter_Titlecase = 17
  Letter_Uppercase = 15
  LineSeparator = 8232
  Mark_Enclosing = 3
  Mark_NonSpacing = 1
  Mark_SpacingCombining = 2
  Medial = 5
  Narrow = 13
  Nbsp = 160
  NoBreak = 3
  NoCategory = 0
  NoDecomposition = 0
  Null = 0
  Number_DecimalDigit = 4
  Number_Letter = 5
  Number_Other = 6
  ObjectReplacementCharacter = 65532
  OtherJoining = 0
  Other_Control = 10
  Other_Format = 11
  Other_NotAssigned = 14
  Other_PrivateUse = 13
  Other_Surrogate = 12
  ParagraphSeparator = 8233
  Punctuation_Close = 23
  Punctuation_Connector = 20
  Punctuation_Dash = 21
  Punctuation_Dask = 21
  Punctuation_FinalQuote = 25
  Punctuation_InitialQuote = 24
  Punctuation_Open = 22
  Punctuation_Other = 26
  ReplacementCharacter = 65533
  Right = 2
  Separator_Line = 8
  Separator_Paragraph = 9
  Separator_Space = 7
  Small = 14
  Square = 15
  Sub = 10
  Super = 9
  Symbol_Currency = 28
  Symbol_Math = 27
  Symbol_Modifier = 29
  Symbol_Other = 30
  Unicode_1_1 = 1
  Unicode_2_0 = 2
  Unicode_2_1_2 = 3
  Unicode_3_0 = 4
  Unicode_3_1 = 5
  Unicode_3_2 = 6
  Unicode_4_0 = 7
  Unicode_4_1 = 8
  Unicode_5_0 = 9
  Unicode_Unassigned = 0
  Vertical = 11
  Wide = 12
  def category(*a,**k): pass
  def cell(*a,**k): pass
  def combiningClass(*a,**k): pass
  def currentUnicodeVersion(*a,**k): pass
  def decomposition(*a,**k): pass
  def decompositionTag(*a,**k): pass
  def digitValue(*a,**k): pass
  def direction(*a,**k): pass
  def fromAscii(*a,**k): pass
  def fromLatin1(*a,**k): pass
  def hasMirrored(*a,**k): pass
  def highSurrogate(*a,**k): pass
  def isDigit(*a,**k): pass
  def isHighSurrogate(*a,**k): pass
  def isLetter(*a,**k): pass
  def isLetterOrNumber(*a,**k): pass
  def isLowSurrogate(*a,**k): pass
  def isLower(*a,**k): pass
  def isMark(*a,**k): pass
  def isNull(*a,**k): pass
  def isNumber(*a,**k): pass
  def isPrint(*a,**k): pass
  def isPunct(*a,**k): pass
  def isSpace(*a,**k): pass
  def isSymbol(*a,**k): pass
  def isTitleCase(*a,**k): pass
  def isUpper(*a,**k): pass
  def joining(*a,**k): pass
  def lowSurrogate(*a,**k): pass
  def mirroredChar(*a,**k): pass
  def requiresSurrogates(*a,**k): pass
  def row(*a,**k): pass
  def setCell(*a,**k): pass
  def setRow(*a,**k): pass
  def surrogateToUcs4(*a,**k): pass
  def toAscii(*a,**k): pass
  def toCaseFolded(*a,**k): pass
  def toLatin1(*a,**k): pass
  def toLower(*a,**k): pass
  def toTitleCase(*a,**k): pass
  def toUpper(*a,**k): pass
  def unicode(*a,**k): pass
  def unicodeVersion(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QCryptographicHash(object):
  pass
  Md4 = 0
  Md5 = 1
  Sha1 = 2
  def addData(*a,**k): pass
  def hash(*a,**k): pass
  def reset(*a,**k): pass
  def result(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QDataStream(object):
  pass
  BigEndian = 0
  DoublePrecision = 1
  LittleEndian = 1
  Ok = 0
  Qt_1_0 = 1
  Qt_2_0 = 2
  Qt_2_1 = 3
  Qt_3_0 = 4
  Qt_3_1 = 5
  Qt_3_3 = 6
  Qt_4_0 = 7
  Qt_4_1 = 7
  Qt_4_2 = 8
  Qt_4_3 = 9
  Qt_4_4 = 10
  Qt_4_5 = 11
  Qt_4_6 = 12
  Qt_4_7 = 12
  Qt_4_8 = 12
  ReadCorruptData = 2
  ReadPastEnd = 1
  SinglePrecision = 0
  WriteFailed = 3
  def atEnd(*a,**k): pass
  def byteOrder(*a,**k): pass
  def device(*a,**k): pass
  def floatingPointPrecision(*a,**k): pass
  def readBool(*a,**k): pass
  def readBytes(*a,**k): pass
  def readDouble(*a,**k): pass
  def readFloat(*a,**k): pass
  def readInt(*a,**k): pass
  def readInt16(*a,**k): pass
  def readInt32(*a,**k): pass
  def readInt64(*a,**k): pass
  def readInt8(*a,**k): pass
  def readQString(*a,**k): pass
  def readQStringList(*a,**k): pass
  def readQVariant(*a,**k): pass
  def readQVariantHash(*a,**k): pass
  def readQVariantList(*a,**k): pass
  def readQVariantMap(*a,**k): pass
  def readRawData(*a,**k): pass
  def readString(*a,**k): pass
  def readUInt16(*a,**k): pass
  def readUInt32(*a,**k): pass
  def readUInt64(*a,**k): pass
  def readUInt8(*a,**k): pass
  def resetStatus(*a,**k): pass
  def setByteOrder(*a,**k): pass
  def setDevice(*a,**k): pass
  def setFloatingPointPrecision(*a,**k): pass
  def setStatus(*a,**k): pass
  def setVersion(*a,**k): pass
  def skipRawData(*a,**k): pass
  def status(*a,**k): pass
  def unsetDevice(*a,**k): pass
  def version(*a,**k): pass
  def writeBool(*a,**k): pass
  def writeBytes(*a,**k): pass
  def writeDouble(*a,**k): pass
  def writeFloat(*a,**k): pass
  def writeInt(*a,**k): pass
  def writeInt16(*a,**k): pass
  def writeInt32(*a,**k): pass
  def writeInt64(*a,**k): pass
  def writeInt8(*a,**k): pass
  def writeQString(*a,**k): pass
  def writeQStringList(*a,**k): pass
  def writeQVariant(*a,**k): pass
  def writeQVariantHash(*a,**k): pass
  def writeQVariantList(*a,**k): pass
  def writeQVariantMap(*a,**k): pass
  def writeRawData(*a,**k): pass
  def writeString(*a,**k): pass
  def writeUInt16(*a,**k): pass
  def writeUInt32(*a,**k): pass
  def writeUInt64(*a,**k): pass
  def writeUInt8(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QDate(object):
  pass
  DateFormat = 0
  StandaloneFormat = 1
  def addDays(*a,**k): pass
  def addMonths(*a,**k): pass
  def addYears(*a,**k): pass
  def currentDate(*a,**k): pass
  def day(*a,**k): pass
  def dayOfWeek(*a,**k): pass
  def dayOfYear(*a,**k): pass
  def daysInMonth(*a,**k): pass
  def daysInYear(*a,**k): pass
  def daysTo(*a,**k): pass
  def fromJulianDay(*a,**k): pass
  def fromString(*a,**k): pass
  def getDate(*a,**k): pass
  def gregorianToJulian(*a,**k): pass
  def isLeapYear(*a,**k): pass
  def isNull(*a,**k): pass
  def isValid(*a,**k): pass
  def julianToGregorian(*a,**k): pass
  def longDayName(*a,**k): pass
  def longMonthName(*a,**k): pass
  def month(*a,**k): pass
  def setDate(*a,**k): pass
  def setYMD(*a,**k): pass
  def shortDayName(*a,**k): pass
  def shortMonthName(*a,**k): pass
  def toJulianDay(*a,**k): pass
  def toPyDate(*a,**k): pass
  def toString(*a,**k): pass
  def weekNumber(*a,**k): pass
  def year(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QDateTime(object):
  pass

  def addDays(*a,**k): pass
  def addMSecs(*a,**k): pass
  def addMonths(*a,**k): pass
  def addSecs(*a,**k): pass
  def addYears(*a,**k): pass
  def currentDateTime(*a,**k): pass
  def currentDateTimeUtc(*a,**k): pass
  def currentMSecsSinceEpoch(*a,**k): pass
  def date(*a,**k): pass
  def daysTo(*a,**k): pass
  def fromMSecsSinceEpoch(*a,**k): pass
  def fromString(*a,**k): pass
  def fromTime_t(*a,**k): pass
  def isNull(*a,**k): pass
  def isValid(*a,**k): pass
  def msecsTo(*a,**k): pass
  def secsTo(*a,**k): pass
  def setDate(*a,**k): pass
  def setMSecsSinceEpoch(*a,**k): pass
  def setTime(*a,**k): pass
  def setTimeSpec(*a,**k): pass
  def setTime_t(*a,**k): pass
  def time(*a,**k): pass
  def timeSpec(*a,**k): pass
  def toLocalTime(*a,**k): pass
  def toMSecsSinceEpoch(*a,**k): pass
  def toPyDateTime(*a,**k): pass
  def toString(*a,**k): pass
  def toTimeSpec(*a,**k): pass
  def toTime_t(*a,**k): pass
  def toUTC(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QDir(object):
  pass
  AccessMask = 1008
  AllDirs = 1024
  AllEntries = 7
  CaseSensitive = 2048
  Dirs = 1
  DirsFirst = 4
  DirsLast = 32
  Drives = 4
  Executable = 64
  Files = 2
  Hidden = 256
  IgnoreCase = 16
  LocaleAware = 64
  Modified = 128
  Name = 0
  NoDot = 8192
  NoDotAndDotDot = 4096
  NoDotDot = 16384
  NoFilter = -1
  NoSort = -1
  NoSymLinks = 8
  PermissionMask = 112
  Readable = 16
  Reversed = 8
  Size = 2
  SortByMask = 3
  System = 512
  Time = 1
  Type = 128
  TypeMask = 15
  Unsorted = 3
  Writable = 32
  def absoluteFilePath(*a,**k): pass
  def absolutePath(*a,**k): pass
  def addResourceSearchPath(*a,**k): pass
  def addSearchPath(*a,**k): pass
  def canonicalPath(*a,**k): pass
  def cd(*a,**k): pass
  def cdUp(*a,**k): pass
  def cleanPath(*a,**k): pass
  def convertSeparators(*a,**k): pass
  def count(*a,**k): pass
  def current(*a,**k): pass
  def currentPath(*a,**k): pass
  def dirName(*a,**k): pass
  def drives(*a,**k): pass
  def entryInfoList(*a,**k): pass
  def entryList(*a,**k): pass
  def exists(*a,**k): pass
  def filePath(*a,**k): pass
  def filter(*a,**k): pass
  def fromNativeSeparators(*a,**k): pass
  def home(*a,**k): pass
  def homePath(*a,**k): pass
  def isAbsolute(*a,**k): pass
  def isAbsolutePath(*a,**k): pass
  def isReadable(*a,**k): pass
  def isRelative(*a,**k): pass
  def isRelativePath(*a,**k): pass
  def isRoot(*a,**k): pass
  def makeAbsolute(*a,**k): pass
  def match(*a,**k): pass
  def mkdir(*a,**k): pass
  def mkpath(*a,**k): pass
  def nameFilters(*a,**k): pass
  def nameFiltersFromString(*a,**k): pass
  def path(*a,**k): pass
  def refresh(*a,**k): pass
  def relativeFilePath(*a,**k): pass
  def remove(*a,**k): pass
  def rename(*a,**k): pass
  def rmdir(*a,**k): pass
  def rmpath(*a,**k): pass
  def root(*a,**k): pass
  def rootPath(*a,**k): pass
  def searchPaths(*a,**k): pass
  def separator(*a,**k): pass
  def setCurrent(*a,**k): pass
  def setFilter(*a,**k): pass
  def setNameFilters(*a,**k): pass
  def setPath(*a,**k): pass
  def setSearchPaths(*a,**k): pass
  def setSorting(*a,**k): pass
  def sorting(*a,**k): pass
  def temp(*a,**k): pass
  def tempPath(*a,**k): pass
  def toNativeSeparators(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QDirIterator(object):
  pass
  FollowSymlinks = 1
  NoIteratorFlags = 0
  Subdirectories = 2
  def fileInfo(*a,**k): pass
  def fileName(*a,**k): pass
  def filePath(*a,**k): pass
  def hasNext(*a,**k): pass
  def next(*a,**k): pass
  def path(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QEasingCurve(object):
  pass
  CosineCurve = 44
  Custom = 45
  InBack = 33
  InBounce = 37
  InCirc = 25
  InCubic = 5
  InCurve = 41
  InElastic = 29
  InExpo = 21
  InOutBack = 35
  InOutBounce = 39
  InOutCirc = 27
  InOutCubic = 7
  InOutElastic = 31
  InOutExpo = 23
  InOutQuad = 3
  InOutQuart = 11
  InOutQuint = 15
  InOutSine = 19
  InQuad = 1
  InQuart = 9
  InQuint = 13
  InSine = 17
  Linear = 0
  OutBack = 34
  OutBounce = 38
  OutCirc = 26
  OutCubic = 6
  OutCurve = 42
  OutElastic = 30
  OutExpo = 22
  OutInBack = 36
  OutInBounce = 40
  OutInCirc = 28
  OutInCubic = 8
  OutInElastic = 32
  OutInExpo = 24
  OutInQuad = 4
  OutInQuart = 12
  OutInQuint = 16
  OutInSine = 20
  OutQuad = 2
  OutQuart = 10
  OutQuint = 14
  OutSine = 18
  SineCurve = 43
  def amplitude(*a,**k): pass
  def customType(*a,**k): pass
  def overshoot(*a,**k): pass
  def period(*a,**k): pass
  def setAmplitude(*a,**k): pass
  def setCustomType(*a,**k): pass
  def setOvershoot(*a,**k): pass
  def setPeriod(*a,**k): pass
  def setType(*a,**k): pass
  def type(*a,**k): pass
  def valueForProgress(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QElapsedTimer(object):
  pass
  MachAbsoluteTime = 3
  MonotonicClock = 1
  PerformanceCounter = 4
  SystemTime = 0
  TickCounter = 2
  def clockType(*a,**k): pass
  def elapsed(*a,**k): pass
  def hasExpired(*a,**k): pass
  def invalidate(*a,**k): pass
  def isMonotonic(*a,**k): pass
  def isValid(*a,**k): pass
  def msecsSinceReference(*a,**k): pass
  def msecsTo(*a,**k): pass
  def nsecsElapsed(*a,**k): pass
  def restart(*a,**k): pass
  def secsTo(*a,**k): pass
  def start(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QFileInfo(object):
  pass

  def absoluteDir(*a,**k): pass
  def absoluteFilePath(*a,**k): pass
  def absolutePath(*a,**k): pass
  def baseName(*a,**k): pass
  def bundleName(*a,**k): pass
  def caching(*a,**k): pass
  def canonicalFilePath(*a,**k): pass
  def canonicalPath(*a,**k): pass
  def completeBaseName(*a,**k): pass
  def completeSuffix(*a,**k): pass
  def created(*a,**k): pass
  def dir(*a,**k): pass
  def exists(*a,**k): pass
  def fileName(*a,**k): pass
  def filePath(*a,**k): pass
  def group(*a,**k): pass
  def groupId(*a,**k): pass
  def isAbsolute(*a,**k): pass
  def isBundle(*a,**k): pass
  def isDir(*a,**k): pass
  def isExecutable(*a,**k): pass
  def isFile(*a,**k): pass
  def isHidden(*a,**k): pass
  def isReadable(*a,**k): pass
  def isRelative(*a,**k): pass
  def isRoot(*a,**k): pass
  def isSymLink(*a,**k): pass
  def isWritable(*a,**k): pass
  def lastModified(*a,**k): pass
  def lastRead(*a,**k): pass
  def makeAbsolute(*a,**k): pass
  def owner(*a,**k): pass
  def ownerId(*a,**k): pass
  def path(*a,**k): pass
  def permission(*a,**k): pass
  def permissions(*a,**k): pass
  def readLink(*a,**k): pass
  def refresh(*a,**k): pass
  def setCaching(*a,**k): pass
  def setFile(*a,**k): pass
  def size(*a,**k): pass
  def suffix(*a,**k): pass
  def symLinkTarget(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QGenericArgument(object):
  pass


  def __init__(self, *args, **kwargs): pass


class QGenericReturnArgument(object):
  pass


  def __init__(self, *args, **kwargs): pass


class QLatin1Char(object):
  pass

  def toLatin1(*a,**k): pass
  def unicode(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QLatin1String(object):
  pass

  def latin1(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QLibraryInfo(object):
  pass
  BinariesPath = 4
  DataPath = 6
  DemosPath = 9
  DocumentationPath = 1
  ExamplesPath = 10
  HeadersPath = 2
  ImportsPath = 11
  LibrariesPath = 3
  PluginsPath = 5
  PrefixPath = 0
  SettingsPath = 8
  TranslationsPath = 7
  def buildDate(*a,**k): pass
  def buildKey(*a,**k): pass
  def licensedProducts(*a,**k): pass
  def licensee(*a,**k): pass
  def location(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QLine(object):
  pass

  def dx(*a,**k): pass
  def dy(*a,**k): pass
  def isNull(*a,**k): pass
  def p1(*a,**k): pass
  def p2(*a,**k): pass
  def setLine(*a,**k): pass
  def setP1(*a,**k): pass
  def setP2(*a,**k): pass
  def setPoints(*a,**k): pass
  def translate(*a,**k): pass
  def translated(*a,**k): pass
  def x1(*a,**k): pass
  def x2(*a,**k): pass
  def y1(*a,**k): pass
  def y2(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QLineF(object):
  pass
  BoundedIntersection = 1
  NoIntersection = 0
  UnboundedIntersection = 2
  def angle(*a,**k): pass
  def angleTo(*a,**k): pass
  def dx(*a,**k): pass
  def dy(*a,**k): pass
  def fromPolar(*a,**k): pass
  def intersect(*a,**k): pass
  def isNull(*a,**k): pass
  def length(*a,**k): pass
  def normalVector(*a,**k): pass
  def p1(*a,**k): pass
  def p2(*a,**k): pass
  def pointAt(*a,**k): pass
  def setAngle(*a,**k): pass
  def setLength(*a,**k): pass
  def setLine(*a,**k): pass
  def setP1(*a,**k): pass
  def setP2(*a,**k): pass
  def setPoints(*a,**k): pass
  def toLine(*a,**k): pass
  def translate(*a,**k): pass
  def translated(*a,**k): pass
  def unitVector(*a,**k): pass
  def x1(*a,**k): pass
  def x2(*a,**k): pass
  def y1(*a,**k): pass
  def y2(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QLocale(object):
  pass
  Abkhazian = 2
  Afan = 3
  Afar = 4
  Afghanistan = 1
  Afrikaans = 5
  Aghem = 216
  Akan = 146
  Albania = 2
  Albanian = 6
  Algeria = 3
  AlternateQuotation = 1
  AmericanSamoa = 4
  Amharic = 7
  Andorra = 5
  Angola = 6
  Anguilla = 7
  Antarctica = 8
  AntiguaAndBarbuda = 9
  AnyCountry = 0
  AnyLanguage = 0
  AnyScript = 0
  Arabic = 8
  ArabicScript = 1
  Argentina = 10
  Armenia = 11
  Armenian = 9
  Aruba = 12
  Assamese = 10
  Asu = 205
  Atsam = 156
  Australia = 13
  Austria = 14
  Aymara = 11
  Azerbaijan = 15
  Azerbaijani = 12
  Bafia = 222
  Bahamas = 16
  Bahrain = 17
  Bambara = 188
  Bangladesh = 18
  Barbados = 19
  Basaa = 217
  Bashkir = 13
  Basque = 14
  Belarus = 20
  Belgium = 21
  Belize = 22
  Bemba = 195
  Bena = 186
  Bengali = 15
  Benin = 23
  Bermuda = 24
  Bhutan = 25
  Bhutani = 16
  Bihari = 17
  Bislama = 18
  Blin = 152
  Bodo = 215
  Bolivia = 26
  BosniaAndHerzegowina = 27
  Bosnian = 142
  Botswana = 28
  BouvetIsland = 29
  Brazil = 30
  Breton = 19
  BritishIndianOceanTerritory = 31
  BritishVirginIslands = 233
  BruneiDarussalam = 32
  Bulgaria = 33
  Bulgarian = 20
  BurkinaFaso = 34
  Burmese = 21
  Burundi = 35
  Byelorussian = 22
  C = 1
  Cambodia = 36
  Cambodian = 23
  Cameroon = 37
  Canada = 38
  CapeVerde = 39
  Catalan = 24
  CaymanIslands = 40
  CentralAfricanRepublic = 41
  CentralMoroccoTamazight = 212
  Chad = 42
  Cherokee = 190
  Chewa = 165
  Chiga = 211
  Chile = 43
  China = 44
  Chinese = 25
  ChristmasIsland = 45
  CocosIslands = 46
  Colognian = 201
  Colombia = 47
  Comoros = 48
  CongoSwahili = 230
  CookIslands = 51
  Cornish = 145
  Corsican = 26
  CostaRica = 52
  Croatia = 54
  Croatian = 27
  Cuba = 55
  CurrencyDisplayName = 2
  CurrencyIsoCode = 0
  CurrencySymbol = 1
  Cyprus = 56
  CyrillicScript = 2
  Czech = 28
  CzechRepublic = 57
  Danish = 29
  DemocraticRepublicOfCongo = 49
  DemocraticRepublicOfKorea = 113
  Denmark = 58
  DeseretScript = 3
  Divehi = 143
  Djibouti = 59
  Dominica = 60
  DominicanRepublic = 61
  Duala = 219
  Dutch = 30
  EastTimor = 62
  Ecuador = 63
  Egypt = 64
  ElSalvador = 65
  Embu = 189
  English = 31
  EquatorialGuinea = 66
  Eritrea = 67
  Esperanto = 32
  Estonia = 68
  Estonian = 33
  Ethiopia = 69
  Ewe = 161
  Ewondo = 221
  FalklandIslands = 70
  FaroeIslands = 71
  Faroese = 34
  FijiCountry = 72
  FijiLanguage = 35
  Filipino = 166
  Finland = 73
  Finnish = 36
  France = 74
  French = 37
  FrenchGuiana = 76
  FrenchPolynesia = 77
  FrenchSouthernTerritories = 78
  Frisian = 38
  Friulian = 159
  Fulah = 177
  Ga = 148
  Gabon = 79
  Gaelic = 39
  Galician = 40
  Gambia = 80
  Ganda = 194
  Geez = 153
  Georgia = 81
  Georgian = 41
  German = 42
  Germany = 82
  Ghana = 83
  Gibraltar = 84
  Greece = 85
  Greek = 43
  Greenland = 86
  Greenlandic = 44
  Grenada = 87
  Guadeloupe = 88
  Guam = 89
  Guarani = 45
  Guatemala = 90
  Guinea = 91
  GuineaBissau = 92
  Gujarati = 46
  GurmukhiScript = 4
  Gusii = 175
  Guyana = 93
  Haiti = 94
  Hausa = 47
  Hawaiian = 163
  HeardAndMcDonaldIslands = 95
  Hebrew = 48
  Hindi = 49
  Honduras = 96
  HongKong = 97
  Hungarian = 50
  Hungary = 98
  Iceland = 99
  Icelandic = 51
  Igbo = 149
  ImperialSystem = 1
  India = 100
  Indonesia = 101
  Indonesian = 52
  Interlingua = 53
  Interlingue = 54
  Inuktitut = 55
  Inupiak = 56
  Iran = 102
  Iraq = 103
  Ireland = 104
  Irish = 57
  Israel = 105
  Italian = 58
  Italy = 106
  IvoryCoast = 53
  Jamaica = 107
  Japan = 108
  Japanese = 59
  Javanese = 60
  Jju = 158
  JolaFonyi = 220
  Jordan = 109
  Kabuverdianu = 196
  Kabyle = 184
  Kalenjin = 198
  Kamba = 150
  Kannada = 61
  Kashmiri = 62
  Kazakh = 63
  Kazakhstan = 110
  Kenya = 111
  Kikuyu = 178
  Kinyarwanda = 64
  Kirghiz = 65
  Kiribati = 112
  Konkani = 147
  Korean = 66
  Koro = 154
  KoyraChiini = 208
  KoyraboroSenni = 213
  Kpelle = 169
  Kurdish = 67
  Kurundi = 68
  Kuwait = 115
  Kwasio = 226
  Kyrgyzstan = 116
  Langi = 193
  Lao = 117
  Laothian = 69
  LastCountry = 246
  LastLanguage = 234
  Latin = 70
  LatinAmericaAndTheCaribbean = 246
  LatinScript = 7
  Latvia = 118
  Latvian = 71
  Lebanon = 119
  Lesotho = 120
  Liberia = 121
  LibyanArabJamahiriya = 122
  Liechtenstein = 123
  Lingala = 72
  Lithuania = 124
  Lithuanian = 73
  LongFormat = 0
  LowGerman = 170
  LubaKatanga = 223
  Luo = 210
  Luxembourg = 125
  Luyia = 204
  Macau = 126
  Macedonia = 127
  Macedonian = 74
  Machame = 200
  Madagascar = 128
  MakhuwaMeetto = 224
  Makonde = 192
  Malagasy = 75
  Malawi = 129
  Malay = 76
  Malayalam = 77
  Malaysia = 130
  Maldives = 131
  Mali = 132
  Malta = 133
  Maltese = 78
  Manx = 144
  Maori = 79
  Marathi = 80
  MarshallIslands = 134
  Martinique = 135
  Masai = 202
  Mauritania = 136
  Mauritius = 137
  Mayotte = 138
  Meru = 197
  MetricSystem = 0
  MetropolitanFrance = 75
  Mexico = 139
  Micronesia = 140
  Moldavian = 81
  Moldova = 141
  Monaco = 142
  Mongolia = 143
  Mongolian = 82
  MongolianScript = 8
  Montenegro = 242
  Montserrat = 144
  Morisyen = 191
  Morocco = 145
  Mozambique = 146
  Mundang = 225
  Myanmar = 147
  Nama = 199
  Namibia = 148
  NarrowFormat = 2
  NauruCountry = 149
  NauruLanguage = 83
  Nepal = 150
  Nepali = 84
  Netherlands = 151
  NetherlandsAntilles = 152
  NewCaledonia = 153
  NewZealand = 154
  Nicaragua = 155
  Niger = 156
  Nigeria = 157
  Niue = 158
  NorfolkIsland = 159
  NorthNdebele = 181
  NorthernMarianaIslands = 160
  NorthernSami = 173
  NorthernSotho = 172
  Norway = 161
  Norwegian = 85
  NorwegianBokmal = 85
  NorwegianNynorsk = 141
  Nuer = 227
  Nyankole = 185
  Nynorsk = 141
  Occitan = 86
  Oman = 162
  OmitGroupSeparator = 1
  Oriya = 87
  Pakistan = 163
  Palau = 164
  PalestinianTerritory = 165
  Panama = 166
  PapuaNewGuinea = 167
  Paraguay = 168
  Pashto = 88
  PeoplesRepublicOfCongo = 50
  Persian = 89
  Peru = 169
  Philippines = 170
  Pitcairn = 171
  Poland = 172
  Polish = 90
  Portugal = 173
  Portuguese = 91
  PuertoRico = 174
  Punjabi = 92
  Qatar = 175
  Quechua = 93
  RejectGroupSeparator = 2
  RepublicOfKorea = 114
  Reunion = 176
  RhaetoRomance = 94
  Romania = 177
  Romanian = 95
  Rombo = 182
  Rundi = 68
  Russian = 96
  RussianFederation = 178
  Rwa = 209
  Rwanda = 179
  Saho = 207
  SaintBarthelemy = 244
  SaintKittsAndNevis = 180
  SaintMartin = 245
  Sakha = 228
  Samburu = 179
  Samoa = 183
  Samoan = 97
  SanMarino = 184
  Sangho = 98
  Sangu = 229
  Sanskrit = 99
  SaoTomeAndPrincipe = 185
  SaudiArabia = 186
  Sena = 180
  Senegal = 187
  Serbia = 243
  SerbiaAndMontenegro = 241
  Serbian = 100
  SerboCroatian = 101
  Sesotho = 102
  Setswana = 103
  Seychelles = 188
  Shambala = 214
  Shona = 104
  ShortFormat = 1
  SichuanYi = 168
  Sidamo = 155
  SierraLeone = 189
  SimplifiedChineseScript = 5
  SimplifiedHanScript = 5
  Sindhi = 105
  Singapore = 190
  Singhalese = 106
  Siswati = 107
  Slovak = 108
  Slovakia = 191
  Slovenia = 192
  Slovenian = 109
  Soga = 203
  SolomonIslands = 193
  Somali = 110
  Somalia = 194
  SouthAfrica = 195
  SouthGeorgiaAndTheSouthSandwichIslands = 196
  SouthNdebele = 171
  Spain = 197
  Spanish = 111
  SriLanka = 198
  StHelena = 199
  StLucia = 181
  StPierreAndMiquelon = 200
  StVincentAndTheGrenadines = 182
  StandardQuotation = 0
  Sudan = 201
  Sundanese = 112
  Suriname = 202
  SvalbardAndJanMayenIslands = 203
  Swahili = 113
  Swaziland = 204
  Sweden = 205
  Swedish = 114
  SwissGerman = 167
  Switzerland = 206
  Syriac = 151
  SyrianArabRepublic = 207
  Tachelhit = 183
  Tagalog = 115
  Taita = 176
  Taiwan = 208
  Tajik = 116
  Tajikistan = 209
  Tamil = 117
  Tanzania = 210
  Taroko = 174
  Tasawaq = 231
  Tatar = 118
  Telugu = 119
  Teso = 206
  Thai = 120
  Thailand = 211
  Tibetan = 121
  TifinaghScript = 9
  Tigre = 157
  Tigrinya = 122
  Togo = 212
  Tokelau = 213
  TongaCountry = 214
  TongaLanguage = 123
  TraditionalChineseScript = 6
  TraditionalHanScript = 6
  TrinidadAndTobago = 215
  Tsonga = 124
  Tunisia = 216
  Turkey = 217
  Turkish = 125
  Turkmen = 126
  Turkmenistan = 218
  TurksAndCaicosIslands = 219
  Tuvalu = 220
  Twi = 127
  Tyap = 164
  USVirginIslands = 234
  Uganda = 221
  Uigur = 128
  Ukraine = 222
  Ukrainian = 129
  UnitedArabEmirates = 223
  UnitedKingdom = 224
  UnitedStates = 225
  UnitedStatesMinorOutlyingIslands = 226
  Urdu = 130
  Uruguay = 227
  Uzbek = 131
  Uzbekistan = 228
  Vai = 232
  Vanuatu = 229
  VaticanCityState = 230
  Venda = 160
  Venezuela = 231
  VietNam = 232
  Vietnamese = 132
  Volapuk = 133
  Vunjo = 187
  Walamo = 162
  WallisAndFutunaIslands = 235
  Walser = 233
  Welsh = 134
  WesternSahara = 236
  Wolof = 135
  Xhosa = 136
  Yangben = 234
  Yemen = 237
  Yiddish = 137
  Yoruba = 138
  Yugoslavia = 238
  Zambia = 239
  Zarma = 218
  Zhuang = 139
  Zimbabwe = 240
  Zulu = 140
  def amText(*a,**k): pass
  def bcp47Name(*a,**k): pass
  def c(*a,**k): pass
  def countriesForLanguage(*a,**k): pass
  def country(*a,**k): pass
  def countryToString(*a,**k): pass
  def createSeparatedList(*a,**k): pass
  def currencySymbol(*a,**k): pass
  def dateFormat(*a,**k): pass
  def dateTimeFormat(*a,**k): pass
  def dayName(*a,**k): pass
  def decimalPoint(*a,**k): pass
  def exponential(*a,**k): pass
  def firstDayOfWeek(*a,**k): pass
  def groupSeparator(*a,**k): pass
  def language(*a,**k): pass
  def languageToString(*a,**k): pass
  def matchingLocales(*a,**k): pass
  def measurementSystem(*a,**k): pass
  def monthName(*a,**k): pass
  def name(*a,**k): pass
  def nativeCountryName(*a,**k): pass
  def nativeLanguageName(*a,**k): pass
  def negativeSign(*a,**k): pass
  def numberOptions(*a,**k): pass
  def percent(*a,**k): pass
  def pmText(*a,**k): pass
  def positiveSign(*a,**k): pass
  def quoteString(*a,**k): pass
  def script(*a,**k): pass
  def scriptToString(*a,**k): pass
  def setDefault(*a,**k): pass
  def setNumberOptions(*a,**k): pass
  def standaloneDayName(*a,**k): pass
  def standaloneMonthName(*a,**k): pass
  def system(*a,**k): pass
  def textDirection(*a,**k): pass
  def timeFormat(*a,**k): pass
  def toCurrencyString(*a,**k): pass
  def toDate(*a,**k): pass
  def toDateTime(*a,**k): pass
  def toDouble(*a,**k): pass
  def toFloat(*a,**k): pass
  def toInt(*a,**k): pass
  def toLongLong(*a,**k): pass
  def toLower(*a,**k): pass
  def toShort(*a,**k): pass
  def toString(*a,**k): pass
  def toTime(*a,**k): pass
  def toUInt(*a,**k): pass
  def toULongLong(*a,**k): pass
  def toUShort(*a,**k): pass
  def toUpper(*a,**k): pass
  def uiLanguages(*a,**k): pass
  def weekdays(*a,**k): pass
  def zeroDigit(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMargins(object):
  pass

  def bottom(*a,**k): pass
  def isNull(*a,**k): pass
  def left(*a,**k): pass
  def right(*a,**k): pass
  def setBottom(*a,**k): pass
  def setLeft(*a,**k): pass
  def setRight(*a,**k): pass
  def setTop(*a,**k): pass
  def top(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMetaClassInfo(object):
  pass

  def name(*a,**k): pass
  def value(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMetaEnum(object):
  pass

  def isFlag(*a,**k): pass
  def isValid(*a,**k): pass
  def key(*a,**k): pass
  def keyCount(*a,**k): pass
  def keyToValue(*a,**k): pass
  def keysToValue(*a,**k): pass
  def name(*a,**k): pass
  def scope(*a,**k): pass
  def value(*a,**k): pass
  def valueToKey(*a,**k): pass
  def valueToKeys(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMetaMethod(object):
  pass
  Constructor = 3
  Method = 0
  Private = 0
  Protected = 1
  Public = 2
  Signal = 1
  Slot = 2
  def access(*a,**k): pass
  def invoke(*a,**k): pass
  def methodIndex(*a,**k): pass
  def methodType(*a,**k): pass
  def parameterNames(*a,**k): pass
  def parameterTypes(*a,**k): pass
  def signature(*a,**k): pass
  def tag(*a,**k): pass
  def typeName(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMetaObject(object):
  pass

  def checkConnectArgs(*a,**k): pass
  def classInfo(*a,**k): pass
  def classInfoCount(*a,**k): pass
  def classInfoOffset(*a,**k): pass
  def className(*a,**k): pass
  def connectSlotsByName(*a,**k): pass
  def constructor(*a,**k): pass
  def constructorCount(*a,**k): pass
  def enumerator(*a,**k): pass
  def enumeratorCount(*a,**k): pass
  def enumeratorOffset(*a,**k): pass
  def indexOfClassInfo(*a,**k): pass
  def indexOfConstructor(*a,**k): pass
  def indexOfEnumerator(*a,**k): pass
  def indexOfMethod(*a,**k): pass
  def indexOfProperty(*a,**k): pass
  def indexOfSignal(*a,**k): pass
  def indexOfSlot(*a,**k): pass
  def invokeMethod(*a,**k): pass
  def method(*a,**k): pass
  def methodCount(*a,**k): pass
  def methodOffset(*a,**k): pass
  def newInstance(*a,**k): pass
  def normalizedSignature(*a,**k): pass
  def normalizedType(*a,**k): pass
  def property(*a,**k): pass
  def propertyCount(*a,**k): pass
  def propertyOffset(*a,**k): pass
  def superClass(*a,**k): pass
  def userProperty(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMetaProperty(object):
  pass

  def enumerator(*a,**k): pass
  def hasNotifySignal(*a,**k): pass
  def hasStdCppSet(*a,**k): pass
  def isConstant(*a,**k): pass
  def isDesignable(*a,**k): pass
  def isEditable(*a,**k): pass
  def isEnumType(*a,**k): pass
  def isFinal(*a,**k): pass
  def isFlagType(*a,**k): pass
  def isReadable(*a,**k): pass
  def isResettable(*a,**k): pass
  def isScriptable(*a,**k): pass
  def isStored(*a,**k): pass
  def isUser(*a,**k): pass
  def isValid(*a,**k): pass
  def isWritable(*a,**k): pass
  def name(*a,**k): pass
  def notifySignal(*a,**k): pass
  def notifySignalIndex(*a,**k): pass
  def propertyIndex(*a,**k): pass
  def read(*a,**k): pass
  def reset(*a,**k): pass
  def type(*a,**k): pass
  def typeName(*a,**k): pass
  def userType(*a,**k): pass
  def write(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMetaType(object):
  pass
  Bool = 1
  Char = 131
  Double = 6
  FirstGuiType = 63
  Float = 135
  Int = 2
  LastCoreType = 29
  Long = 129
  LongLong = 4
  QBitArray = 13
  QBitmap = 73
  QBrush = 66
  QByteArray = 12
  QChar = 7
  QColor = 67
  QCursor = 74
  QDate = 14
  QDateTime = 16
  QEasingCurve = 29
  QFont = 64
  QIcon = 69
  QImage = 70
  QKeySequence = 76
  QLine = 23
  QLineF = 24
  QLocale = 18
  QMatrix = 80
  QMatrix4x4 = 82
  QObjectStar = 136
  QPalette = 68
  QPen = 77
  QPixmap = 65
  QPoint = 25
  QPointF = 26
  QPolygon = 71
  QQuaternion = 86
  QRect = 19
  QRectF = 20
  QRegExp = 27
  QRegion = 72
  QSize = 21
  QSizeF = 22
  QSizePolicy = 75
  QString = 10
  QStringList = 11
  QTextFormat = 79
  QTextLength = 78
  QTime = 15
  QTransform = 81
  QUrl = 17
  QVariant = 138
  QVariantHash = 28
  QVariantList = 9
  QVariantMap = 8
  QVector2D = 83
  QVector3D = 84
  QVector4D = 85
  QWidgetStar = 137
  Short = 130
  UChar = 134
  UInt = 3
  ULong = 132
  ULongLong = 5
  UShort = 133
  User = 256
  Void = 0
  VoidStar = 128
  def isRegistered(*a,**k): pass
  def type(*a,**k): pass
  def typeName(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QModelIndex(object):
  pass

  def child(*a,**k): pass
  def column(*a,**k): pass
  def data(*a,**k): pass
  def flags(*a,**k): pass
  def internalId(*a,**k): pass
  def internalPointer(*a,**k): pass
  def isValid(*a,**k): pass
  def model(*a,**k): pass
  def parent(*a,**k): pass
  def row(*a,**k): pass
  def sibling(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMutex(object):
  pass
  NonRecursive = 0
  Recursive = 1
  def lock(*a,**k): pass
  def tryLock(*a,**k): pass
  def unlock(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QMutexLocker(object):
  pass

  def mutex(*a,**k): pass
  def relock(*a,**k): pass
  def unlock(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPersistentModelIndex(object):
  pass

  def child(*a,**k): pass
  def column(*a,**k): pass
  def data(*a,**k): pass
  def flags(*a,**k): pass
  def isValid(*a,**k): pass
  def model(*a,**k): pass
  def parent(*a,**k): pass
  def row(*a,**k): pass
  def sibling(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPoint(object):
  pass

  def isNull(*a,**k): pass
  def manhattanLength(*a,**k): pass
  def setX(*a,**k): pass
  def setY(*a,**k): pass
  def x(*a,**k): pass
  def y(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QPointF(object):
  pass

  def isNull(*a,**k): pass
  def manhattanLength(*a,**k): pass
  def setX(*a,**k): pass
  def setY(*a,**k): pass
  def toPoint(*a,**k): pass
  def x(*a,**k): pass
  def y(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QProcessEnvironment(object):
  pass

  def clear(*a,**k): pass
  def contains(*a,**k): pass
  def insert(*a,**k): pass
  def isEmpty(*a,**k): pass
  def keys(*a,**k): pass
  def remove(*a,**k): pass
  def systemEnvironment(*a,**k): pass
  def toStringList(*a,**k): pass
  def value(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QReadLocker(object):
  pass

  def readWriteLock(*a,**k): pass
  def relock(*a,**k): pass
  def unlock(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QReadWriteLock(object):
  pass
  NonRecursive = 0
  Recursive = 1
  def lockForRead(*a,**k): pass
  def lockForWrite(*a,**k): pass
  def tryLockForRead(*a,**k): pass
  def tryLockForWrite(*a,**k): pass
  def unlock(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QRect(object):
  pass

  def adjust(*a,**k): pass
  def adjusted(*a,**k): pass
  def bottom(*a,**k): pass
  def bottomLeft(*a,**k): pass
  def bottomRight(*a,**k): pass
  def center(*a,**k): pass
  def contains(*a,**k): pass
  def getCoords(*a,**k): pass
  def getRect(*a,**k): pass
  def height(*a,**k): pass
  def intersect(*a,**k): pass
  def intersected(*a,**k): pass
  def intersects(*a,**k): pass
  def isEmpty(*a,**k): pass
  def isNull(*a,**k): pass
  def isValid(*a,**k): pass
  def left(*a,**k): pass
  def moveBottom(*a,**k): pass
  def moveBottomLeft(*a,**k): pass
  def moveBottomRight(*a,**k): pass
  def moveCenter(*a,**k): pass
  def moveLeft(*a,**k): pass
  def moveRight(*a,**k): pass
  def moveTo(*a,**k): pass
  def moveTop(*a,**k): pass
  def moveTopLeft(*a,**k): pass
  def moveTopRight(*a,**k): pass
  def normalized(*a,**k): pass
  def right(*a,**k): pass
  def setBottom(*a,**k): pass
  def setBottomLeft(*a,**k): pass
  def setBottomRight(*a,**k): pass
  def setCoords(*a,**k): pass
  def setHeight(*a,**k): pass
  def setLeft(*a,**k): pass
  def setRect(*a,**k): pass
  def setRight(*a,**k): pass
  def setSize(*a,**k): pass
  def setTop(*a,**k): pass
  def setTopLeft(*a,**k): pass
  def setTopRight(*a,**k): pass
  def setWidth(*a,**k): pass
  def setX(*a,**k): pass
  def setY(*a,**k): pass
  def size(*a,**k): pass
  def top(*a,**k): pass
  def topLeft(*a,**k): pass
  def topRight(*a,**k): pass
  def translate(*a,**k): pass
  def translated(*a,**k): pass
  def unite(*a,**k): pass
  def united(*a,**k): pass
  def width(*a,**k): pass
  def x(*a,**k): pass
  def y(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QRectF(object):
  pass

  def adjust(*a,**k): pass
  def adjusted(*a,**k): pass
  def bottom(*a,**k): pass
  def bottomLeft(*a,**k): pass
  def bottomRight(*a,**k): pass
  def center(*a,**k): pass
  def contains(*a,**k): pass
  def getCoords(*a,**k): pass
  def getRect(*a,**k): pass
  def height(*a,**k): pass
  def intersect(*a,**k): pass
  def intersected(*a,**k): pass
  def intersects(*a,**k): pass
  def isEmpty(*a,**k): pass
  def isNull(*a,**k): pass
  def isValid(*a,**k): pass
  def left(*a,**k): pass
  def moveBottom(*a,**k): pass
  def moveBottomLeft(*a,**k): pass
  def moveBottomRight(*a,**k): pass
  def moveCenter(*a,**k): pass
  def moveLeft(*a,**k): pass
  def moveRight(*a,**k): pass
  def moveTo(*a,**k): pass
  def moveTop(*a,**k): pass
  def moveTopLeft(*a,**k): pass
  def moveTopRight(*a,**k): pass
  def normalized(*a,**k): pass
  def right(*a,**k): pass
  def setBottom(*a,**k): pass
  def setBottomLeft(*a,**k): pass
  def setBottomRight(*a,**k): pass
  def setCoords(*a,**k): pass
  def setHeight(*a,**k): pass
  def setLeft(*a,**k): pass
  def setRect(*a,**k): pass
  def setRight(*a,**k): pass
  def setSize(*a,**k): pass
  def setTop(*a,**k): pass
  def setTopLeft(*a,**k): pass
  def setTopRight(*a,**k): pass
  def setWidth(*a,**k): pass
  def setX(*a,**k): pass
  def setY(*a,**k): pass
  def size(*a,**k): pass
  def toAlignedRect(*a,**k): pass
  def toRect(*a,**k): pass
  def top(*a,**k): pass
  def topLeft(*a,**k): pass
  def topRight(*a,**k): pass
  def translate(*a,**k): pass
  def translated(*a,**k): pass
  def unite(*a,**k): pass
  def united(*a,**k): pass
  def width(*a,**k): pass
  def x(*a,**k): pass
  def y(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QRegExp(object):
  pass
  CaretAtOffset = 1
  CaretAtZero = 0
  CaretWontMatch = 2
  FixedString = 2
  RegExp = 0
  RegExp2 = 3
  W3CXmlSchema11 = 5
  Wildcard = 1
  WildcardUnix = 4
  def cap(*a,**k): pass
  def captureCount(*a,**k): pass
  def capturedTexts(*a,**k): pass
  def caseSensitivity(*a,**k): pass
  def errorString(*a,**k): pass
  def escape(*a,**k): pass
  def exactMatch(*a,**k): pass
  def indexIn(*a,**k): pass
  def isEmpty(*a,**k): pass
  def isMinimal(*a,**k): pass
  def isValid(*a,**k): pass
  def lastIndexIn(*a,**k): pass
  def matchedLength(*a,**k): pass
  def numCaptures(*a,**k): pass
  def pattern(*a,**k): pass
  def patternSyntax(*a,**k): pass
  def pos(*a,**k): pass
  def setCaseSensitivity(*a,**k): pass
  def setMinimal(*a,**k): pass
  def setPattern(*a,**k): pass
  def setPatternSyntax(*a,**k): pass
  def swap(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QResource(object):
  pass

  def absoluteFilePath(*a,**k): pass
  def addSearchPath(*a,**k): pass
  def children(*a,**k): pass
  def data(*a,**k): pass
  def fileName(*a,**k): pass
  def isCompressed(*a,**k): pass
  def isDir(*a,**k): pass
  def isFile(*a,**k): pass
  def isValid(*a,**k): pass
  def locale(*a,**k): pass
  def registerResource(*a,**k): pass
  def registerResourceData(*a,**k): pass
  def searchPaths(*a,**k): pass
  def setFileName(*a,**k): pass
  def setLocale(*a,**k): pass
  def size(*a,**k): pass
  def unregisterResource(*a,**k): pass
  def unregisterResourceData(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QSemaphore(object):
  pass

  def acquire(*a,**k): pass
  def available(*a,**k): pass
  def release(*a,**k): pass
  def tryAcquire(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QSize(object):
  pass

  def boundedTo(*a,**k): pass
  def expandedTo(*a,**k): pass
  def height(*a,**k): pass
  def isEmpty(*a,**k): pass
  def isNull(*a,**k): pass
  def isValid(*a,**k): pass
  def scale(*a,**k): pass
  def setHeight(*a,**k): pass
  def setWidth(*a,**k): pass
  def transpose(*a,**k): pass
  def width(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QSizeF(object):
  pass

  def boundedTo(*a,**k): pass
  def expandedTo(*a,**k): pass
  def height(*a,**k): pass
  def isEmpty(*a,**k): pass
  def isNull(*a,**k): pass
  def isValid(*a,**k): pass
  def scale(*a,**k): pass
  def setHeight(*a,**k): pass
  def setWidth(*a,**k): pass
  def toSize(*a,**k): pass
  def transpose(*a,**k): pass
  def width(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QString(object):
  pass
  KeepEmptyParts = 0
  NormalizationForm_C = 1
  NormalizationForm_D = 0
  NormalizationForm_KC = 3
  NormalizationForm_KD = 2
  SectionCaseInsensitiveSeps = 8
  SectionDefault = 0
  SectionIncludeLeadingSep = 2
  SectionIncludeTrailingSep = 4
  SectionSkipEmpty = 1
  SkipEmptyParts = 1
  def append(*a,**k): pass
  def arg(*a,**k): pass
  def at(*a,**k): pass
  def capacity(*a,**k): pass
  def chop(*a,**k): pass
  def clear(*a,**k): pass
  def compare(*a,**k): pass
  def contains(*a,**k): pass
  def count(*a,**k): pass
  def endsWith(*a,**k): pass
  def fill(*a,**k): pass
  def fromAscii(*a,**k): pass
  def fromLatin1(*a,**k): pass
  def fromLocal8Bit(*a,**k): pass
  def fromUtf8(*a,**k): pass
  def indexOf(*a,**k): pass
  def insert(*a,**k): pass
  def isEmpty(*a,**k): pass
  def isNull(*a,**k): pass
  def isRightToLeft(*a,**k): pass
  def isSimpleText(*a,**k): pass
  def lastIndexOf(*a,**k): pass
  def left(*a,**k): pass
  def leftJustified(*a,**k): pass
  def length(*a,**k): pass
  def localeAwareCompare(*a,**k): pass
  def mid(*a,**k): pass
  def normalized(*a,**k): pass
  def number(*a,**k): pass
  def prepend(*a,**k): pass
  def push_back(*a,**k): pass
  def push_front(*a,**k): pass
  def remove(*a,**k): pass
  def repeated(*a,**k): pass
  def replace(*a,**k): pass
  def reserve(*a,**k): pass
  def resize(*a,**k): pass
  def right(*a,**k): pass
  def rightJustified(*a,**k): pass
  def section(*a,**k): pass
  def setNum(*a,**k): pass
  def simplified(*a,**k): pass
  def size(*a,**k): pass
  def split(*a,**k): pass
  def squeeze(*a,**k): pass
  def startsWith(*a,**k): pass
  def swap(*a,**k): pass
  def toAscii(*a,**k): pass
  def toCaseFolded(*a,**k): pass
  def toDouble(*a,**k): pass
  def toFloat(*a,**k): pass
  def toInt(*a,**k): pass
  def toLatin1(*a,**k): pass
  def toLocal8Bit(*a,**k): pass
  def toLong(*a,**k): pass
  def toLongLong(*a,**k): pass
  def toLower(*a,**k): pass
  def toShort(*a,**k): pass
  def toUInt(*a,**k): pass
  def toULong(*a,**k): pass
  def toULongLong(*a,**k): pass
  def toUShort(*a,**k): pass
  def toUpper(*a,**k): pass
  def toUtf8(*a,**k): pass
  def trimmed(*a,**k): pass
  def truncate(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QStringList(object):
  pass

  def append(*a,**k): pass
  def clear(*a,**k): pass
  def contains(*a,**k): pass
  def count(*a,**k): pass
  def filter(*a,**k): pass
  def first(*a,**k): pass
  def indexOf(*a,**k): pass
  def insert(*a,**k): pass
  def isEmpty(*a,**k): pass
  def join(*a,**k): pass
  def last(*a,**k): pass
  def lastIndexOf(*a,**k): pass
  def mid(*a,**k): pass
  def move(*a,**k): pass
  def prepend(*a,**k): pass
  def removeAll(*a,**k): pass
  def removeAt(*a,**k): pass
  def removeDuplicates(*a,**k): pass
  def replace(*a,**k): pass
  def replaceInStrings(*a,**k): pass
  def sort(*a,**k): pass
  def swap(*a,**k): pass
  def takeAt(*a,**k): pass
  def takeFirst(*a,**k): pass
  def takeLast(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QStringMatcher(object):
  pass

  def caseSensitivity(*a,**k): pass
  def indexIn(*a,**k): pass
  def pattern(*a,**k): pass
  def setCaseSensitivity(*a,**k): pass
  def setPattern(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QStringRef(object):
  pass

  def appendTo(*a,**k): pass
  def at(*a,**k): pass
  def clear(*a,**k): pass
  def compare(*a,**k): pass
  def constData(*a,**k): pass
  def contains(*a,**k): pass
  def count(*a,**k): pass
  def data(*a,**k): pass
  def endsWith(*a,**k): pass
  def indexOf(*a,**k): pass
  def isEmpty(*a,**k): pass
  def isNull(*a,**k): pass
  def lastIndexOf(*a,**k): pass
  def length(*a,**k): pass
  def localeAwareCompare(*a,**k): pass
  def position(*a,**k): pass
  def size(*a,**k): pass
  def startsWith(*a,**k): pass
  def string(*a,**k): pass
  def toAscii(*a,**k): pass
  def toLatin1(*a,**k): pass
  def toLocal8Bit(*a,**k): pass
  def toString(*a,**k): pass
  def toUcs4(*a,**k): pass
  def toUtf8(*a,**k): pass
  def unicode(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QSysInfo(object):
  pass
  BigEndian = 0
  ByteOrder = 1
  LittleEndian = 1
  WordSize = 64

  def __init__(self, *args, **kwargs): pass


class QSystemLocale(object):
  pass
  AMText = 24
  CountryId = 1
  CurrencySymbol = 28
  CurrencyToString = 29
  DateFormatLong = 6
  DateFormatShort = 7
  DateTimeFormatLong = 18
  DateTimeFormatShort = 19
  DateTimeToStringLong = 20
  DateTimeToStringShort = 21
  DateToStringLong = 14
  DateToStringShort = 15
  DayNameLong = 10
  DayNameShort = 11
  DecimalPoint = 2
  FirstDayOfWeek = 26
  GroupSeparator = 3
  LanguageId = 0
  ListToSeparatedString = 34
  LocaleChanged = 35
  MeasurementSystem = 22
  MonthNameLong = 12
  MonthNameShort = 13
  NativeCountryName = 37
  NativeLanguageName = 36
  NegativeSign = 5
  PMText = 25
  PositiveSign = 23
  ScriptId = 33
  StringToAlternateQuotation = 32
  StringToStandardQuotation = 31
  TimeFormatLong = 8
  TimeFormatShort = 9
  TimeToStringLong = 16
  TimeToStringShort = 17
  UILanguages = 30
  Weekdays = 27
  ZeroDigit = 4
  def fallbackLocale(*a,**k): pass
  def query(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QSystemSemaphore(object):
  pass
  AlreadyExists = 3
  Create = 1
  KeyError = 2
  NoError = 0
  NotFound = 4
  Open = 0
  OutOfResources = 5
  PermissionDenied = 1
  UnknownError = 6
  def acquire(*a,**k): pass
  def error(*a,**k): pass
  def errorString(*a,**k): pass
  def key(*a,**k): pass
  def release(*a,**k): pass
  def setKey(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextBoundaryFinder(object):
  pass
  EndWord = 2
  Grapheme = 0
  Line = 2
  NotAtBoundary = 0
  Sentence = 3
  StartWord = 1
  Word = 1
  def boundaryReasons(*a,**k): pass
  def isAtBoundary(*a,**k): pass
  def isValid(*a,**k): pass
  def position(*a,**k): pass
  def setPosition(*a,**k): pass
  def string(*a,**k): pass
  def toEnd(*a,**k): pass
  def toNextBoundary(*a,**k): pass
  def toPreviousBoundary(*a,**k): pass
  def toStart(*a,**k): pass
  def type(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextStream(object):
  pass
  AlignAccountingStyle = 3
  AlignCenter = 2
  AlignLeft = 0
  AlignRight = 1
  FixedNotation = 1
  ForcePoint = 2
  ForceSign = 4
  Ok = 0
  ReadCorruptData = 2
  ReadPastEnd = 1
  ScientificNotation = 2
  ShowBase = 1
  SmartNotation = 0
  UppercaseBase = 8
  UppercaseDigits = 16
  WriteFailed = 3
  def atEnd(*a,**k): pass
  def autoDetectUnicode(*a,**k): pass
  def codec(*a,**k): pass
  def device(*a,**k): pass
  def fieldAlignment(*a,**k): pass
  def fieldWidth(*a,**k): pass
  def flush(*a,**k): pass
  def generateByteOrderMark(*a,**k): pass
  def integerBase(*a,**k): pass
  def locale(*a,**k): pass
  def numberFlags(*a,**k): pass
  def padChar(*a,**k): pass
  def pos(*a,**k): pass
  def read(*a,**k): pass
  def readAll(*a,**k): pass
  def readLine(*a,**k): pass
  def realNumberNotation(*a,**k): pass
  def realNumberPrecision(*a,**k): pass
  def reset(*a,**k): pass
  def resetStatus(*a,**k): pass
  def seek(*a,**k): pass
  def setAutoDetectUnicode(*a,**k): pass
  def setCodec(*a,**k): pass
  def setDevice(*a,**k): pass
  def setFieldAlignment(*a,**k): pass
  def setFieldWidth(*a,**k): pass
  def setGenerateByteOrderMark(*a,**k): pass
  def setIntegerBase(*a,**k): pass
  def setLocale(*a,**k): pass
  def setNumberFlags(*a,**k): pass
  def setPadChar(*a,**k): pass
  def setRealNumberNotation(*a,**k): pass
  def setRealNumberPrecision(*a,**k): pass
  def setStatus(*a,**k): pass
  def setString(*a,**k): pass
  def skipWhiteSpace(*a,**k): pass
  def status(*a,**k): pass
  def string(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextStreamManipulator(object):
  pass


  def __init__(self, *args, **kwargs): pass


class QTime(object):
  pass

  def addMSecs(*a,**k): pass
  def addSecs(*a,**k): pass
  def currentTime(*a,**k): pass
  def elapsed(*a,**k): pass
  def fromString(*a,**k): pass
  def hour(*a,**k): pass
  def isNull(*a,**k): pass
  def isValid(*a,**k): pass
  def minute(*a,**k): pass
  def msec(*a,**k): pass
  def msecsTo(*a,**k): pass
  def restart(*a,**k): pass
  def second(*a,**k): pass
  def secsTo(*a,**k): pass
  def setHMS(*a,**k): pass
  def start(*a,**k): pass
  def toPyTime(*a,**k): pass
  def toString(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QUrl(object):
  pass
  RemoveAuthority = 30
  RemoveFragment = 128
  RemovePassword = 2
  RemovePath = 32
  RemovePort = 8
  RemoveQuery = 64
  RemoveScheme = 1
  RemoveUserInfo = 6
  StrictMode = 1
  StripTrailingSlash = 65536
  TolerantMode = 0
  def addEncodedQueryItem(*a,**k): pass
  def addQueryItem(*a,**k): pass
  def allEncodedQueryItemValues(*a,**k): pass
  def allQueryItemValues(*a,**k): pass
  def authority(*a,**k): pass
  def clear(*a,**k): pass
  def detach(*a,**k): pass
  def encodedFragment(*a,**k): pass
  def encodedHost(*a,**k): pass
  def encodedPassword(*a,**k): pass
  def encodedPath(*a,**k): pass
  def encodedQuery(*a,**k): pass
  def encodedQueryItemValue(*a,**k): pass
  def encodedQueryItems(*a,**k): pass
  def encodedUserName(*a,**k): pass
  def errorString(*a,**k): pass
  def fragment(*a,**k): pass
  def fromAce(*a,**k): pass
  def fromEncoded(*a,**k): pass
  def fromLocalFile(*a,**k): pass
  def fromPercentEncoding(*a,**k): pass
  def fromPunycode(*a,**k): pass
  def fromUserInput(*a,**k): pass
  def hasEncodedQueryItem(*a,**k): pass
  def hasFragment(*a,**k): pass
  def hasQuery(*a,**k): pass
  def hasQueryItem(*a,**k): pass
  def host(*a,**k): pass
  def idnWhitelist(*a,**k): pass
  def isDetached(*a,**k): pass
  def isEmpty(*a,**k): pass
  def isLocalFile(*a,**k): pass
  def isParentOf(*a,**k): pass
  def isRelative(*a,**k): pass
  def isValid(*a,**k): pass
  def password(*a,**k): pass
  def path(*a,**k): pass
  def port(*a,**k): pass
  def queryItemValue(*a,**k): pass
  def queryItems(*a,**k): pass
  def queryPairDelimiter(*a,**k): pass
  def queryValueDelimiter(*a,**k): pass
  def removeAllEncodedQueryItems(*a,**k): pass
  def removeAllQueryItems(*a,**k): pass
  def removeEncodedQueryItem(*a,**k): pass
  def removeQueryItem(*a,**k): pass
  def resolved(*a,**k): pass
  def scheme(*a,**k): pass
  def setAuthority(*a,**k): pass
  def setEncodedFragment(*a,**k): pass
  def setEncodedHost(*a,**k): pass
  def setEncodedPassword(*a,**k): pass
  def setEncodedPath(*a,**k): pass
  def setEncodedQuery(*a,**k): pass
  def setEncodedQueryItems(*a,**k): pass
  def setEncodedUrl(*a,**k): pass
  def setEncodedUserName(*a,**k): pass
  def setFragment(*a,**k): pass
  def setHost(*a,**k): pass
  def setIdnWhitelist(*a,**k): pass
  def setPassword(*a,**k): pass
  def setPath(*a,**k): pass
  def setPort(*a,**k): pass
  def setQueryDelimiters(*a,**k): pass
  def setQueryItems(*a,**k): pass
  def setScheme(*a,**k): pass
  def setUrl(*a,**k): pass
  def setUserInfo(*a,**k): pass
  def setUserName(*a,**k): pass
  def swap(*a,**k): pass
  def toAce(*a,**k): pass
  def toEncoded(*a,**k): pass
  def toLocalFile(*a,**k): pass
  def toPercentEncoding(*a,**k): pass
  def toPunycode(*a,**k): pass
  def toString(*a,**k): pass
  def topLevelDomain(*a,**k): pass
  def userInfo(*a,**k): pass
  def userName(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QUuid(object):
  pass
  DCE = 2
  EmbeddedPOSIX = 2
  Microsoft = 6
  NCS = 0
  Name = 3
  Random = 4
  Reserved = 7
  Time = 1
  VarUnknown = -1
  VerUnknown = -1
  def createUuid(*a,**k): pass
  def fromRfc4122(*a,**k): pass
  def isNull(*a,**k): pass
  def toByteArray(*a,**k): pass
  def toRfc4122(*a,**k): pass
  def toString(*a,**k): pass
  def variant(*a,**k): pass
  def version(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QVariant(object):
  pass
  BitArray = 13
  Bitmap = 73
  Bool = 1
  Brush = 66
  ByteArray = 12
  Char = 7
  Color = 67
  Cursor = 74
  Date = 14
  DateTime = 16
  Double = 6
  EasingCurve = 29
  Font = 64
  Hash = 28
  Icon = 69
  Image = 70
  Int = 2
  Invalid = 0
  KeySequence = 76
  Line = 23
  LineF = 24
  List = 9
  Locale = 18
  LongLong = 4
  Map = 8
  Matrix = 80
  Matrix4x4 = 82
  Palette = 68
  Pen = 77
  Pixmap = 65
  Point = 25
  PointF = 26
  Polygon = 71
  Quaternion = 86
  Rect = 19
  RectF = 20
  RegExp = 27
  Region = 72
  Size = 21
  SizeF = 22
  SizePolicy = 75
  String = 10
  StringList = 11
  TextFormat = 79
  TextLength = 78
  Time = 15
  Transform = 81
  UInt = 3
  ULongLong = 5
  Url = 17
  UserType = 127
  Vector2D = 83
  Vector3D = 84
  Vector4D = 85
  def canConvert(*a,**k): pass
  def clear(*a,**k): pass
  def convert(*a,**k): pass
  def data(*a,**k): pass
  def detach(*a,**k): pass
  def fromList(*a,**k): pass
  def fromMap(*a,**k): pass
  def isDetached(*a,**k): pass
  def isNull(*a,**k): pass
  def isValid(*a,**k): pass
  def load(*a,**k): pass
  def nameToType(*a,**k): pass
  def save(*a,**k): pass
  def swap(*a,**k): pass
  def toBitArray(*a,**k): pass
  def toBool(*a,**k): pass
  def toByteArray(*a,**k): pass
  def toChar(*a,**k): pass
  def toDate(*a,**k): pass
  def toDateTime(*a,**k): pass
  def toDouble(*a,**k): pass
  def toEasingCurve(*a,**k): pass
  def toFloat(*a,**k): pass
  def toHash(*a,**k): pass
  def toInt(*a,**k): pass
  def toLine(*a,**k): pass
  def toLineF(*a,**k): pass
  def toList(*a,**k): pass
  def toLocale(*a,**k): pass
  def toLongLong(*a,**k): pass
  def toMap(*a,**k): pass
  def toPoint(*a,**k): pass
  def toPointF(*a,**k): pass
  def toPyObject(*a,**k): pass
  def toReal(*a,**k): pass
  def toRect(*a,**k): pass
  def toRectF(*a,**k): pass
  def toRegExp(*a,**k): pass
  def toSize(*a,**k): pass
  def toSizeF(*a,**k): pass
  def toString(*a,**k): pass
  def toStringList(*a,**k): pass
  def toTime(*a,**k): pass
  def toUInt(*a,**k): pass
  def toULongLong(*a,**k): pass
  def toUrl(*a,**k): pass
  def type(*a,**k): pass
  def typeName(*a,**k): pass
  def typeToName(*a,**k): pass
  def userType(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QWaitCondition(object):
  pass

  def wait(*a,**k): pass
  def wakeAll(*a,**k): pass
  def wakeOne(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QWriteLocker(object):
  pass

  def readWriteLock(*a,**k): pass
  def relock(*a,**k): pass
  def unlock(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QXmlStreamAttribute(object):
  pass

  def isDefault(*a,**k): pass
  def name(*a,**k): pass
  def namespaceUri(*a,**k): pass
  def prefix(*a,**k): pass
  def qualifiedName(*a,**k): pass
  def value(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QXmlStreamAttributes(object):
  pass

  def append(*a,**k): pass
  def at(*a,**k): pass
  def clear(*a,**k): pass
  def contains(*a,**k): pass
  def count(*a,**k): pass
  def data(*a,**k): pass
  def fill(*a,**k): pass
  def first(*a,**k): pass
  def hasAttribute(*a,**k): pass
  def indexOf(*a,**k): pass
  def insert(*a,**k): pass
  def isEmpty(*a,**k): pass
  def last(*a,**k): pass
  def lastIndexOf(*a,**k): pass
  def prepend(*a,**k): pass
  def remove(*a,**k): pass
  def replace(*a,**k): pass
  def size(*a,**k): pass
  def value(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QXmlStreamEntityDeclaration(object):
  pass

  def name(*a,**k): pass
  def notationName(*a,**k): pass
  def publicId(*a,**k): pass
  def systemId(*a,**k): pass
  def value(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QXmlStreamEntityResolver(object):
  pass

  def resolveUndeclaredEntity(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QXmlStreamNamespaceDeclaration(object):
  pass

  def namespaceUri(*a,**k): pass
  def prefix(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QXmlStreamNotationDeclaration(object):
  pass

  def name(*a,**k): pass
  def publicId(*a,**k): pass
  def systemId(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QXmlStreamReader(object):
  pass
  Characters = 6
  Comment = 7
  CustomError = 2
  DTD = 8
  EndDocument = 3
  EndElement = 5
  EntityReference = 9
  ErrorOnUnexpectedElement = 0
  IncludeChildElements = 1
  Invalid = 1
  NoError = 0
  NoToken = 0
  NotWellFormedError = 3
  PrematureEndOfDocumentError = 4
  ProcessingInstruction = 10
  SkipChildElements = 2
  StartDocument = 2
  StartElement = 4
  UnexpectedElementError = 1
  def addData(*a,**k): pass
  def addExtraNamespaceDeclaration(*a,**k): pass
  def addExtraNamespaceDeclarations(*a,**k): pass
  def atEnd(*a,**k): pass
  def attributes(*a,**k): pass
  def characterOffset(*a,**k): pass
  def clear(*a,**k): pass
  def columnNumber(*a,**k): pass
  def device(*a,**k): pass
  def documentEncoding(*a,**k): pass
  def documentVersion(*a,**k): pass
  def dtdName(*a,**k): pass
  def dtdPublicId(*a,**k): pass
  def dtdSystemId(*a,**k): pass
  def entityDeclarations(*a,**k): pass
  def entityResolver(*a,**k): pass
  def error(*a,**k): pass
  def errorString(*a,**k): pass
  def hasError(*a,**k): pass
  def isCDATA(*a,**k): pass
  def isCharacters(*a,**k): pass
  def isComment(*a,**k): pass
  def isDTD(*a,**k): pass
  def isEndDocument(*a,**k): pass
  def isEndElement(*a,**k): pass
  def isEntityReference(*a,**k): pass
  def isProcessingInstruction(*a,**k): pass
  def isStandaloneDocument(*a,**k): pass
  def isStartDocument(*a,**k): pass
  def isStartElement(*a,**k): pass
  def isWhitespace(*a,**k): pass
  def lineNumber(*a,**k): pass
  def name(*a,**k): pass
  def namespaceDeclarations(*a,**k): pass
  def namespaceProcessing(*a,**k): pass
  def namespaceUri(*a,**k): pass
  def notationDeclarations(*a,**k): pass
  def prefix(*a,**k): pass
  def processingInstructionData(*a,**k): pass
  def processingInstructionTarget(*a,**k): pass
  def qualifiedName(*a,**k): pass
  def raiseError(*a,**k): pass
  def readElementText(*a,**k): pass
  def readNext(*a,**k): pass
  def readNextStartElement(*a,**k): pass
  def setDevice(*a,**k): pass
  def setEntityResolver(*a,**k): pass
  def setNamespaceProcessing(*a,**k): pass
  def skipCurrentElement(*a,**k): pass
  def text(*a,**k): pass
  def tokenString(*a,**k): pass
  def tokenType(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QXmlStreamWriter(object):
  pass

  def autoFormatting(*a,**k): pass
  def autoFormattingIndent(*a,**k): pass
  def codec(*a,**k): pass
  def device(*a,**k): pass
  def hasError(*a,**k): pass
  def setAutoFormatting(*a,**k): pass
  def setAutoFormattingIndent(*a,**k): pass
  def setCodec(*a,**k): pass
  def setDevice(*a,**k): pass
  def writeAttribute(*a,**k): pass
  def writeAttributes(*a,**k): pass
  def writeCDATA(*a,**k): pass
  def writeCharacters(*a,**k): pass
  def writeComment(*a,**k): pass
  def writeCurrentToken(*a,**k): pass
  def writeDTD(*a,**k): pass
  def writeDefaultNamespace(*a,**k): pass
  def writeEmptyElement(*a,**k): pass
  def writeEndDocument(*a,**k): pass
  def writeEndElement(*a,**k): pass
  def writeEntityReference(*a,**k): pass
  def writeNamespace(*a,**k): pass
  def writeProcessingInstruction(*a,**k): pass
  def writeStartDocument(*a,**k): pass
  def writeStartElement(*a,**k): pass
  def writeTextElement(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QObject(object):
  pass

  def blockSignals(*a,**k): pass
  def childEvent(*a,**k): pass
  def children(*a,**k): pass
  def connect(*a,**k): pass
  def connectNotify(*a,**k): pass
  def customEvent(*a,**k): pass
  def deleteLater(*a,**k): pass
  def destroyed(*a,**k): pass
  def disconnect(*a,**k): pass
  def disconnectNotify(*a,**k): pass
  def dumpObjectInfo(*a,**k): pass
  def dumpObjectTree(*a,**k): pass
  def dynamicPropertyNames(*a,**k): pass
  def emit(*a,**k): pass
  def event(*a,**k): pass
  def eventFilter(*a,**k): pass
  def findChild(*a,**k): pass
  def findChildren(*a,**k): pass
  def inherits(*a,**k): pass
  def installEventFilter(*a,**k): pass
  def isWidgetType(*a,**k): pass
  def killTimer(*a,**k): pass
  def metaObject(*a,**k): pass
  def moveToThread(*a,**k): pass
  def objectName(*a,**k): pass
  def parent(*a,**k): pass
  def property(*a,**k): pass
  def pyqtConfigure(*a,**k): pass
  def receivers(*a,**k): pass
  def removeEventFilter(*a,**k): pass
  def sender(*a,**k): pass
  def senderSignalIndex(*a,**k): pass
  def setObjectName(*a,**k): pass
  def setParent(*a,**k): pass
  def setProperty(*a,**k): pass
  def signalsBlocked(*a,**k): pass
  def startTimer(*a,**k): pass
  def thread(*a,**k): pass
  def timerEvent(*a,**k): pass
  def tr(*a,**k): pass
  def trUtf8(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QAbstractAnimation(QObject):
  pass
  Backward = 1
  DeleteWhenStopped = 1
  Forward = 0
  KeepWhenStopped = 0
  Paused = 1
  Running = 2
  Stopped = 0
  def currentLoop(*a,**k): pass
  def currentLoopChanged(*a,**k): pass
  def currentLoopTime(*a,**k): pass
  def currentTime(*a,**k): pass
  def direction(*a,**k): pass
  def directionChanged(*a,**k): pass
  def duration(*a,**k): pass
  def finished(*a,**k): pass
  def group(*a,**k): pass
  def loopCount(*a,**k): pass
  def pause(*a,**k): pass
  def resume(*a,**k): pass
  def setCurrentTime(*a,**k): pass
  def setDirection(*a,**k): pass
  def setLoopCount(*a,**k): pass
  def setPaused(*a,**k): pass
  def start(*a,**k): pass
  def state(*a,**k): pass
  def stateChanged(*a,**k): pass
  def stop(*a,**k): pass
  def totalDuration(*a,**k): pass
  def updateCurrentTime(*a,**k): pass
  def updateDirection(*a,**k): pass
  def updateState(*a,**k): pass

class QAnimationGroup(QAbstractAnimation):
  pass

  def addAnimation(*a,**k): pass
  def animationAt(*a,**k): pass
  def animationCount(*a,**k): pass
  def clear(*a,**k): pass
  def indexOfAnimation(*a,**k): pass
  def insertAnimation(*a,**k): pass
  def removeAnimation(*a,**k): pass
  def takeAnimation(*a,**k): pass

class QParallelAnimationGroup(QAnimationGroup):
  pass



class QSequentialAnimationGroup(QAnimationGroup):
  pass

  def addPause(*a,**k): pass
  def currentAnimation(*a,**k): pass
  def currentAnimationChanged(*a,**k): pass
  def insertPause(*a,**k): pass

class QPauseAnimation(QAbstractAnimation):
  pass

  def setDuration(*a,**k): pass

class QVariantAnimation(QAbstractAnimation):
  pass

  def currentValue(*a,**k): pass
  def easingCurve(*a,**k): pass
  def endValue(*a,**k): pass
  def interpolated(*a,**k): pass
  def keyValueAt(*a,**k): pass
  def keyValues(*a,**k): pass
  def setDuration(*a,**k): pass
  def setEasingCurve(*a,**k): pass
  def setEndValue(*a,**k): pass
  def setKeyValueAt(*a,**k): pass
  def setKeyValues(*a,**k): pass
  def setStartValue(*a,**k): pass
  def startValue(*a,**k): pass
  def updateCurrentValue(*a,**k): pass
  def valueChanged(*a,**k): pass

class QPropertyAnimation(QVariantAnimation):
  pass

  def propertyName(*a,**k): pass
  def setPropertyName(*a,**k): pass
  def setTargetObject(*a,**k): pass
  def targetObject(*a,**k): pass

class QAbstractEventDispatcher(QObject):
  pass

  def aboutToBlock(*a,**k): pass
  def awake(*a,**k): pass
  def closingDown(*a,**k): pass
  def filterEvent(*a,**k): pass
  def flush(*a,**k): pass
  def hasPendingEvents(*a,**k): pass
  def instance(*a,**k): pass
  def interrupt(*a,**k): pass
  def processEvents(*a,**k): pass
  def registerSocketNotifier(*a,**k): pass
  def registerTimer(*a,**k): pass
  def registeredTimers(*a,**k): pass
  def setEventFilter(*a,**k): pass
  def startingUp(*a,**k): pass
  def unregisterSocketNotifier(*a,**k): pass
  def unregisterTimer(*a,**k): pass
  def unregisterTimers(*a,**k): pass
  def wakeUp(*a,**k): pass

class QAbstractItemModel(QObject):
  pass

  def beginInsertColumns(*a,**k): pass
  def beginInsertRows(*a,**k): pass
  def beginMoveColumns(*a,**k): pass
  def beginMoveRows(*a,**k): pass
  def beginRemoveColumns(*a,**k): pass
  def beginRemoveRows(*a,**k): pass
  def beginResetModel(*a,**k): pass
  def buddy(*a,**k): pass
  def canFetchMore(*a,**k): pass
  def changePersistentIndex(*a,**k): pass
  def changePersistentIndexList(*a,**k): pass
  def columnCount(*a,**k): pass
  def columnsAboutToBeInserted(*a,**k): pass
  def columnsAboutToBeMoved(*a,**k): pass
  def columnsAboutToBeRemoved(*a,**k): pass
  def columnsInserted(*a,**k): pass
  def columnsMoved(*a,**k): pass
  def columnsRemoved(*a,**k): pass
  def createIndex(*a,**k): pass
  def data(*a,**k): pass
  def dataChanged(*a,**k): pass
  def decodeData(*a,**k): pass
  def dropMimeData(*a,**k): pass
  def encodeData(*a,**k): pass
  def endInsertColumns(*a,**k): pass
  def endInsertRows(*a,**k): pass
  def endMoveColumns(*a,**k): pass
  def endMoveRows(*a,**k): pass
  def endRemoveColumns(*a,**k): pass
  def endRemoveRows(*a,**k): pass
  def endResetModel(*a,**k): pass
  def fetchMore(*a,**k): pass
  def flags(*a,**k): pass
  def hasChildren(*a,**k): pass
  def hasIndex(*a,**k): pass
  def headerData(*a,**k): pass
  def headerDataChanged(*a,**k): pass
  def index(*a,**k): pass
  def insertColumn(*a,**k): pass
  def insertColumns(*a,**k): pass
  def insertRow(*a,**k): pass
  def insertRows(*a,**k): pass
  def itemData(*a,**k): pass
  def layoutAboutToBeChanged(*a,**k): pass
  def layoutChanged(*a,**k): pass
  def match(*a,**k): pass
  def mimeData(*a,**k): pass
  def mimeTypes(*a,**k): pass
  def modelAboutToBeReset(*a,**k): pass
  def modelReset(*a,**k): pass
  def persistentIndexList(*a,**k): pass
  def removeColumn(*a,**k): pass
  def removeColumns(*a,**k): pass
  def removeRow(*a,**k): pass
  def removeRows(*a,**k): pass
  def reset(*a,**k): pass
  def resetInternalData(*a,**k): pass
  def revert(*a,**k): pass
  def roleNames(*a,**k): pass
  def rowCount(*a,**k): pass
  def rowsAboutToBeInserted(*a,**k): pass
  def rowsAboutToBeMoved(*a,**k): pass
  def rowsAboutToBeRemoved(*a,**k): pass
  def rowsInserted(*a,**k): pass
  def rowsMoved(*a,**k): pass
  def rowsRemoved(*a,**k): pass
  def setData(*a,**k): pass
  def setHeaderData(*a,**k): pass
  def setItemData(*a,**k): pass
  def setRoleNames(*a,**k): pass
  def setSupportedDragActions(*a,**k): pass
  def sibling(*a,**k): pass
  def sort(*a,**k): pass
  def span(*a,**k): pass
  def submit(*a,**k): pass
  def supportedDragActions(*a,**k): pass
  def supportedDropActions(*a,**k): pass

class QAbstractListModel(QAbstractItemModel):
  pass



class QAbstractTableModel(QAbstractItemModel):
  pass



class QAbstractState(QObject):
  pass

  def entered(*a,**k): pass
  def exited(*a,**k): pass
  def machine(*a,**k): pass
  def onEntry(*a,**k): pass
  def onExit(*a,**k): pass
  def parentState(*a,**k): pass

class QFinalState(QAbstractState):
  pass



class QHistoryState(QAbstractState):
  pass
  DeepHistory = 1
  ShallowHistory = 0
  def defaultState(*a,**k): pass
  def historyType(*a,**k): pass
  def setDefaultState(*a,**k): pass
  def setHistoryType(*a,**k): pass

class QState(QAbstractState):
  pass
  ExclusiveStates = 0
  ParallelStates = 1
  def addTransition(*a,**k): pass
  def assignProperty(*a,**k): pass
  def childMode(*a,**k): pass
  def errorState(*a,**k): pass
  def finished(*a,**k): pass
  def initialState(*a,**k): pass
  def propertiesAssigned(*a,**k): pass
  def removeTransition(*a,**k): pass
  def setChildMode(*a,**k): pass
  def setErrorState(*a,**k): pass
  def setInitialState(*a,**k): pass
  def transitions(*a,**k): pass

class QStateMachine(QState):
  pass
  DontRestoreProperties = 0
  HighPriority = 1
  NoCommonAncestorForTransitionError = 3
  NoDefaultStateInHistoryStateError = 2
  NoError = 0
  NoInitialStateError = 1
  NormalPriority = 0
  RestoreProperties = 1
  def addDefaultAnimation(*a,**k): pass
  def addState(*a,**k): pass
  def cancelDelayedEvent(*a,**k): pass
  def clearError(*a,**k): pass
  def configuration(*a,**k): pass
  def defaultAnimations(*a,**k): pass
  def error(*a,**k): pass
  def errorString(*a,**k): pass
  def globalRestorePolicy(*a,**k): pass
  def isAnimated(*a,**k): pass
  def isRunning(*a,**k): pass
  def postDelayedEvent(*a,**k): pass
  def postEvent(*a,**k): pass
  def removeDefaultAnimation(*a,**k): pass
  def removeState(*a,**k): pass
  def setAnimated(*a,**k): pass
  def setGlobalRestorePolicy(*a,**k): pass
  def start(*a,**k): pass
  def started(*a,**k): pass
  def stop(*a,**k): pass
  def stopped(*a,**k): pass

class QAbstractTransition(QObject):
  pass

  def addAnimation(*a,**k): pass
  def animations(*a,**k): pass
  def eventTest(*a,**k): pass
  def machine(*a,**k): pass
  def onTransition(*a,**k): pass
  def removeAnimation(*a,**k): pass
  def setTargetState(*a,**k): pass
  def setTargetStates(*a,**k): pass
  def sourceState(*a,**k): pass
  def targetState(*a,**k): pass
  def targetStates(*a,**k): pass
  def triggered(*a,**k): pass

class QEventTransition(QAbstractTransition):
  pass

  def eventSource(*a,**k): pass
  def eventType(*a,**k): pass
  def setEventSource(*a,**k): pass
  def setEventType(*a,**k): pass

class QSignalTransition(QAbstractTransition):
  pass

  def senderObject(*a,**k): pass
  def setSenderObject(*a,**k): pass
  def setSignal(*a,**k): pass
  def signal(*a,**k): pass

class QIODevice(QObject):
  pass
  Append = 4
  NotOpen = 0
  ReadOnly = 1
  ReadWrite = 3
  Text = 16
  Truncate = 8
  Unbuffered = 32
  WriteOnly = 2
  def aboutToClose(*a,**k): pass
  def atEnd(*a,**k): pass
  def bytesAvailable(*a,**k): pass
  def bytesToWrite(*a,**k): pass
  def bytesWritten(*a,**k): pass
  def canReadLine(*a,**k): pass
  def close(*a,**k): pass
  def errorString(*a,**k): pass
  def getChar(*a,**k): pass
  def isOpen(*a,**k): pass
  def isReadable(*a,**k): pass
  def isSequential(*a,**k): pass
  def isTextModeEnabled(*a,**k): pass
  def isWritable(*a,**k): pass
  def open(*a,**k): pass
  def openMode(*a,**k): pass
  def peek(*a,**k): pass
  def pos(*a,**k): pass
  def putChar(*a,**k): pass
  def read(*a,**k): pass
  def readAll(*a,**k): pass
  def readChannelFinished(*a,**k): pass
  def readData(*a,**k): pass
  def readLine(*a,**k): pass
  def readLineData(*a,**k): pass
  def readyRead(*a,**k): pass
  def reset(*a,**k): pass
  def seek(*a,**k): pass
  def setErrorString(*a,**k): pass
  def setOpenMode(*a,**k): pass
  def setTextModeEnabled(*a,**k): pass
  def size(*a,**k): pass
  def ungetChar(*a,**k): pass
  def waitForBytesWritten(*a,**k): pass
  def waitForReadyRead(*a,**k): pass
  def write(*a,**k): pass
  def writeData(*a,**k): pass

class QBuffer(QIODevice):
  pass

  def buffer(*a,**k): pass
  def data(*a,**k): pass
  def setBuffer(*a,**k): pass
  def setData(*a,**k): pass

class QFile(QIODevice):
  pass
  AbortError = 6
  AutoCloseHandle = 1
  CopyError = 14
  DontCloseHandle = 0
  ExeGroup = 16
  ExeOther = 1
  ExeOwner = 4096
  ExeUser = 256
  FatalError = 3
  NoError = 0
  NoOptions = 0
  OpenError = 5
  PermissionsError = 13
  PositionError = 11
  ReadError = 1
  ReadGroup = 64
  ReadOther = 4
  ReadOwner = 16384
  ReadUser = 1024
  RemoveError = 9
  RenameError = 10
  ResizeError = 12
  ResourceError = 4
  TimeOutError = 7
  UnspecifiedError = 8
  WriteError = 2
  WriteGroup = 32
  WriteOther = 2
  WriteOwner = 8192
  WriteUser = 512
  def copy(*a,**k): pass
  def decodeName(*a,**k): pass
  def encodeName(*a,**k): pass
  def error(*a,**k): pass
  def exists(*a,**k): pass
  def fileEngine(*a,**k): pass
  def fileName(*a,**k): pass
  def flush(*a,**k): pass
  def handle(*a,**k): pass
  def link(*a,**k): pass
  def map(*a,**k): pass
  def permissions(*a,**k): pass
  def readLink(*a,**k): pass
  def remove(*a,**k): pass
  def rename(*a,**k): pass
  def resize(*a,**k): pass
  def setFileName(*a,**k): pass
  def setPermissions(*a,**k): pass
  def symLinkTarget(*a,**k): pass
  def unmap(*a,**k): pass
  def unsetError(*a,**k): pass

class QTemporaryFile(QFile):
  pass

  def autoRemove(*a,**k): pass
  def createLocalFile(*a,**k): pass
  def fileTemplate(*a,**k): pass
  def setAutoRemove(*a,**k): pass
  def setFileTemplate(*a,**k): pass

class QProcess(QIODevice):
  pass
  CrashExit = 1
  Crashed = 1
  FailedToStart = 0
  ForwardedChannels = 2
  MergedChannels = 1
  NormalExit = 0
  NotRunning = 0
  ReadError = 3
  Running = 2
  SeparateChannels = 0
  StandardError = 1
  StandardOutput = 0
  Starting = 1
  Timedout = 2
  UnknownError = 5
  WriteError = 4
  def closeReadChannel(*a,**k): pass
  def closeWriteChannel(*a,**k): pass
  def environment(*a,**k): pass
  def error(*a,**k): pass
  def execute(*a,**k): pass
  def exitCode(*a,**k): pass
  def exitStatus(*a,**k): pass
  def finished(*a,**k): pass
  def kill(*a,**k): pass
  def pid(*a,**k): pass
  def processChannelMode(*a,**k): pass
  def processEnvironment(*a,**k): pass
  def readAllStandardError(*a,**k): pass
  def readAllStandardOutput(*a,**k): pass
  def readChannel(*a,**k): pass
  def readChannelMode(*a,**k): pass
  def readyReadStandardError(*a,**k): pass
  def readyReadStandardOutput(*a,**k): pass
  def setEnvironment(*a,**k): pass
  def setProcessChannelMode(*a,**k): pass
  def setProcessEnvironment(*a,**k): pass
  def setProcessState(*a,**k): pass
  def setReadChannel(*a,**k): pass
  def setReadChannelMode(*a,**k): pass
  def setStandardErrorFile(*a,**k): pass
  def setStandardInputFile(*a,**k): pass
  def setStandardOutputFile(*a,**k): pass
  def setStandardOutputProcess(*a,**k): pass
  def setWorkingDirectory(*a,**k): pass
  def setupChildProcess(*a,**k): pass
  def start(*a,**k): pass
  def startDetached(*a,**k): pass
  def started(*a,**k): pass
  def state(*a,**k): pass
  def stateChanged(*a,**k): pass
  def systemEnvironment(*a,**k): pass
  def terminate(*a,**k): pass
  def waitForFinished(*a,**k): pass
  def waitForStarted(*a,**k): pass
  def workingDirectory(*a,**k): pass

class QCoreApplication(QObject):
  pass
  CodecForTr = 0
  DefaultCodec = 0
  UnicodeUTF8 = 1
  def aboutToQuit(*a,**k): pass
  def addLibraryPath(*a,**k): pass
  def applicationDirPath(*a,**k): pass
  def applicationFilePath(*a,**k): pass
  def applicationName(*a,**k): pass
  def applicationPid(*a,**k): pass
  def applicationVersion(*a,**k): pass
  def argc(*a,**k): pass
  def arguments(*a,**k): pass
  def argv(*a,**k): pass
  def closingDown(*a,**k): pass
  def exec_(*a,**k): pass
  def exit(*a,**k): pass
  def flush(*a,**k): pass
  def hasPendingEvents(*a,**k): pass
  def installTranslator(*a,**k): pass
  def instance(*a,**k): pass
  def libraryPaths(*a,**k): pass
  def notify(*a,**k): pass
  def organizationDomain(*a,**k): pass
  def organizationName(*a,**k): pass
  def postEvent(*a,**k): pass
  def processEvents(*a,**k): pass
  def quit(*a,**k): pass
  def removeLibraryPath(*a,**k): pass
  def removePostedEvents(*a,**k): pass
  def removeTranslator(*a,**k): pass
  def sendEvent(*a,**k): pass
  def sendPostedEvents(*a,**k): pass
  def setApplicationName(*a,**k): pass
  def setApplicationVersion(*a,**k): pass
  def setAttribute(*a,**k): pass
  def setLibraryPaths(*a,**k): pass
  def setOrganizationDomain(*a,**k): pass
  def setOrganizationName(*a,**k): pass
  def startingUp(*a,**k): pass
  def testAttribute(*a,**k): pass
  def translate(*a,**k): pass

class QEventLoop(QObject):
  pass
  AllEvents = 0
  DeferredDeletion = 16
  ExcludeSocketNotifiers = 2
  ExcludeUserInputEvents = 1
  WaitForMoreEvents = 4
  X11ExcludeTimers = 8
  def exec_(*a,**k): pass
  def exit(*a,**k): pass
  def isRunning(*a,**k): pass
  def processEvents(*a,**k): pass
  def quit(*a,**k): pass
  def wakeUp(*a,**k): pass

class QFileSystemWatcher(QObject):
  pass

  def addPath(*a,**k): pass
  def addPaths(*a,**k): pass
  def directories(*a,**k): pass
  def directoryChanged(*a,**k): pass
  def fileChanged(*a,**k): pass
  def files(*a,**k): pass
  def removePath(*a,**k): pass
  def removePaths(*a,**k): pass

class QLibrary(QObject):
  pass
  ExportExternalSymbolsHint = 2
  LoadArchiveMemberHint = 4
  ResolveAllSymbolsHint = 1
  def errorString(*a,**k): pass
  def fileName(*a,**k): pass
  def isLibrary(*a,**k): pass
  def isLoaded(*a,**k): pass
  def load(*a,**k): pass
  def loadHints(*a,**k): pass
  def resolve(*a,**k): pass
  def setFileName(*a,**k): pass
  def setFileNameAndVersion(*a,**k): pass
  def setLoadHints(*a,**k): pass
  def unload(*a,**k): pass

class QMimeData(QObject):
  pass

  def clear(*a,**k): pass
  def colorData(*a,**k): pass
  def data(*a,**k): pass
  def formats(*a,**k): pass
  def hasColor(*a,**k): pass
  def hasFormat(*a,**k): pass
  def hasHtml(*a,**k): pass
  def hasImage(*a,**k): pass
  def hasText(*a,**k): pass
  def hasUrls(*a,**k): pass
  def html(*a,**k): pass
  def imageData(*a,**k): pass
  def removeFormat(*a,**k): pass
  def retrieveData(*a,**k): pass
  def setColorData(*a,**k): pass
  def setData(*a,**k): pass
  def setHtml(*a,**k): pass
  def setImageData(*a,**k): pass
  def setText(*a,**k): pass
  def setUrls(*a,**k): pass
  def text(*a,**k): pass
  def urls(*a,**k): pass

class QObjectCleanupHandler(QObject):
  pass

  def add(*a,**k): pass
  def clear(*a,**k): pass
  def isEmpty(*a,**k): pass
  def remove(*a,**k): pass

class QPluginLoader(QObject):
  pass

  def errorString(*a,**k): pass
  def fileName(*a,**k): pass
  def instance(*a,**k): pass
  def isLoaded(*a,**k): pass
  def load(*a,**k): pass
  def loadHints(*a,**k): pass
  def setFileName(*a,**k): pass
  def setLoadHints(*a,**k): pass
  def staticInstances(*a,**k): pass
  def unload(*a,**k): pass

class QSettings(QObject):
  pass
  AccessError = 1
  FormatError = 2
  IniFormat = 1
  InvalidFormat = 16
  NativeFormat = 0
  NoError = 0
  SystemScope = 1
  UserScope = 0
  def allKeys(*a,**k): pass
  def applicationName(*a,**k): pass
  def beginGroup(*a,**k): pass
  def beginReadArray(*a,**k): pass
  def beginWriteArray(*a,**k): pass
  def childGroups(*a,**k): pass
  def childKeys(*a,**k): pass
  def clear(*a,**k): pass
  def contains(*a,**k): pass
  def defaultFormat(*a,**k): pass
  def endArray(*a,**k): pass
  def endGroup(*a,**k): pass
  def fallbacksEnabled(*a,**k): pass
  def fileName(*a,**k): pass
  def format(*a,**k): pass
  def group(*a,**k): pass
  def iniCodec(*a,**k): pass
  def isWritable(*a,**k): pass
  def organizationName(*a,**k): pass
  def remove(*a,**k): pass
  def scope(*a,**k): pass
  def setArrayIndex(*a,**k): pass
  def setDefaultFormat(*a,**k): pass
  def setFallbacksEnabled(*a,**k): pass
  def setIniCodec(*a,**k): pass
  def setPath(*a,**k): pass
  def setSystemIniPath(*a,**k): pass
  def setUserIniPath(*a,**k): pass
  def setValue(*a,**k): pass
  def status(*a,**k): pass
  def sync(*a,**k): pass
  def value(*a,**k): pass

class QSharedMemory(QObject):
  pass
  AlreadyExists = 4
  InvalidSize = 2
  KeyError = 3
  LockError = 6
  NoError = 0
  NotFound = 5
  OutOfResources = 7
  PermissionDenied = 1
  ReadOnly = 0
  ReadWrite = 1
  UnknownError = 8
  def attach(*a,**k): pass
  def constData(*a,**k): pass
  def create(*a,**k): pass
  def data(*a,**k): pass
  def detach(*a,**k): pass
  def error(*a,**k): pass
  def errorString(*a,**k): pass
  def isAttached(*a,**k): pass
  def key(*a,**k): pass
  def lock(*a,**k): pass
  def nativeKey(*a,**k): pass
  def setKey(*a,**k): pass
  def setNativeKey(*a,**k): pass
  def size(*a,**k): pass
  def unlock(*a,**k): pass

class QSignalMapper(QObject):
  pass

  def map(*a,**k): pass
  def mapped(*a,**k): pass
  def mapping(*a,**k): pass
  def removeMappings(*a,**k): pass
  def setMapping(*a,**k): pass

class QSocketNotifier(QObject):
  pass
  Exception = 2
  Read = 0
  Write = 1
  def activated(*a,**k): pass
  def isEnabled(*a,**k): pass
  def setEnabled(*a,**k): pass
  def socket(*a,**k): pass
  def type(*a,**k): pass

class QThread(QObject):
  pass
  HighPriority = 4
  HighestPriority = 5
  IdlePriority = 0
  InheritPriority = 7
  LowPriority = 2
  LowestPriority = 1
  NormalPriority = 3
  TimeCriticalPriority = 6
  def currentThread(*a,**k): pass
  def currentThreadId(*a,**k): pass
  def exec_(*a,**k): pass
  def exit(*a,**k): pass
  def finished(*a,**k): pass
  def idealThreadCount(*a,**k): pass
  def isFinished(*a,**k): pass
  def isRunning(*a,**k): pass
  def msleep(*a,**k): pass
  def priority(*a,**k): pass
  def quit(*a,**k): pass
  def run(*a,**k): pass
  def setPriority(*a,**k): pass
  def setStackSize(*a,**k): pass
  def setTerminationEnabled(*a,**k): pass
  def sleep(*a,**k): pass
  def stackSize(*a,**k): pass
  def start(*a,**k): pass
  def started(*a,**k): pass
  def terminate(*a,**k): pass
  def terminated(*a,**k): pass
  def usleep(*a,**k): pass
  def wait(*a,**k): pass
  def yieldCurrentThread(*a,**k): pass

class QThreadPool(QObject):
  pass

  def activeThreadCount(*a,**k): pass
  def expiryTimeout(*a,**k): pass
  def globalInstance(*a,**k): pass
  def maxThreadCount(*a,**k): pass
  def releaseThread(*a,**k): pass
  def reserveThread(*a,**k): pass
  def setExpiryTimeout(*a,**k): pass
  def setMaxThreadCount(*a,**k): pass
  def start(*a,**k): pass
  def tryStart(*a,**k): pass
  def waitForDone(*a,**k): pass

class QTimeLine(QObject):
  pass
  Backward = 1
  CosineCurve = 5
  EaseInCurve = 0
  EaseInOutCurve = 2
  EaseOutCurve = 1
  Forward = 0
  LinearCurve = 3
  NotRunning = 0
  Paused = 1
  Running = 2
  SineCurve = 4
  def currentFrame(*a,**k): pass
  def currentTime(*a,**k): pass
  def currentValue(*a,**k): pass
  def curveShape(*a,**k): pass
  def direction(*a,**k): pass
  def duration(*a,**k): pass
  def easingCurve(*a,**k): pass
  def endFrame(*a,**k): pass
  def finished(*a,**k): pass
  def frameChanged(*a,**k): pass
  def frameForTime(*a,**k): pass
  def loopCount(*a,**k): pass
  def resume(*a,**k): pass
  def setCurrentTime(*a,**k): pass
  def setCurveShape(*a,**k): pass
  def setDirection(*a,**k): pass
  def setDuration(*a,**k): pass
  def setEasingCurve(*a,**k): pass
  def setEndFrame(*a,**k): pass
  def setFrameRange(*a,**k): pass
  def setLoopCount(*a,**k): pass
  def setPaused(*a,**k): pass
  def setStartFrame(*a,**k): pass
  def setUpdateInterval(*a,**k): pass
  def start(*a,**k): pass
  def startFrame(*a,**k): pass
  def state(*a,**k): pass
  def stateChanged(*a,**k): pass
  def stop(*a,**k): pass
  def toggleDirection(*a,**k): pass
  def updateInterval(*a,**k): pass
  def valueChanged(*a,**k): pass
  def valueForTime(*a,**k): pass

class QTimer(QObject):
  pass

  def interval(*a,**k): pass
  def isActive(*a,**k): pass
  def isSingleShot(*a,**k): pass
  def setInterval(*a,**k): pass
  def setSingleShot(*a,**k): pass
  def singleShot(*a,**k): pass
  def start(*a,**k): pass
  def stop(*a,**k): pass
  def timeout(*a,**k): pass
  def timerId(*a,**k): pass

class QTranslator(QObject):
  pass

  def isEmpty(*a,**k): pass
  def load(*a,**k): pass
  def loadFromData(*a,**k): pass
  def translate(*a,**k): pass

class QAbstractFileEngine(object):
  pass
  AbsoluteName = 3
  AbsolutePathName = 4
  AccessTime = 2
  BaseName = 1
  BundleName = 8
  BundleType = 524288
  CanonicalName = 6
  CanonicalPathName = 7
  CreationTime = 0
  DefaultName = 0
  DirectoryType = 262144
  ExeGroupPerm = 16
  ExeOtherPerm = 1
  ExeOwnerPerm = 4096
  ExeUserPerm = 256
  ExistsFlag = 4194304
  FileInfoAll = 268435455
  FileType = 131072
  FlagsMask = 267386880
  HiddenFlag = 1048576
  LinkName = 5
  LinkType = 65536
  LocalDiskFlag = 2097152
  ModificationTime = 1
  OwnerGroup = 1
  OwnerUser = 0
  PathName = 2
  PermsMask = 65535
  ReadGroupPerm = 64
  ReadOtherPerm = 4
  ReadOwnerPerm = 16384
  ReadUserPerm = 1024
  Refresh = 16777216
  RootFlag = 8388608
  TypesMask = 983040
  WriteGroupPerm = 32
  WriteOtherPerm = 2
  WriteOwnerPerm = 8192
  WriteUserPerm = 512
  def atEnd(*a,**k): pass
  def beginEntryList(*a,**k): pass
  def caseSensitive(*a,**k): pass
  def close(*a,**k): pass
  def copy(*a,**k): pass
  def create(*a,**k): pass
  def entryList(*a,**k): pass
  def error(*a,**k): pass
  def errorString(*a,**k): pass
  def fileFlags(*a,**k): pass
  def fileName(*a,**k): pass
  def fileTime(*a,**k): pass
  def flush(*a,**k): pass
  def handle(*a,**k): pass
  def isRelativePath(*a,**k): pass
  def isSequential(*a,**k): pass
  def link(*a,**k): pass
  def map(*a,**k): pass
  def mkdir(*a,**k): pass
  def open(*a,**k): pass
  def owner(*a,**k): pass
  def ownerId(*a,**k): pass
  def pos(*a,**k): pass
  def read(*a,**k): pass
  def readLine(*a,**k): pass
  def remove(*a,**k): pass
  def rename(*a,**k): pass
  def rmdir(*a,**k): pass
  def seek(*a,**k): pass
  def setError(*a,**k): pass
  def setFileName(*a,**k): pass
  def setPermissions(*a,**k): pass
  def setSize(*a,**k): pass
  def size(*a,**k): pass
  def unmap(*a,**k): pass
  def write(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QFSFileEngine(QAbstractFileEngine):
  pass

  def currentPath(*a,**k): pass
  def drives(*a,**k): pass
  def homePath(*a,**k): pass
  def rootPath(*a,**k): pass
  def setCurrentPath(*a,**k): pass
  def tempPath(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QAbstractFileEngineIterator(object):
  pass

  def currentFileInfo(*a,**k): pass
  def currentFileName(*a,**k): pass
  def currentFilePath(*a,**k): pass
  def filters(*a,**k): pass
  def hasNext(*a,**k): pass
  def nameFilters(*a,**k): pass
  def next(*a,**k): pass
  def path(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QEvent(object):
  pass
  AccessibilityDescription = 130
  AccessibilityHelp = 119
  AccessibilityPrepare = 86
  ActionAdded = 114
  ActionChanged = 113
  ActionRemoved = 115
  ActivationChange = 99
  ApplicationActivate = 121
  ApplicationActivated = 121
  ApplicationDeactivate = 122
  ApplicationDeactivated = 122
  ApplicationFontChange = 36
  ApplicationLayoutDirectionChange = 37
  ApplicationPaletteChange = 38
  ApplicationWindowIconChange = 35
  ChildAdded = 68
  ChildPolished = 69
  ChildRemoved = 71
  Clipboard = 40
  Close = 19
  CloseSoftwareInputPanel = 200
  ContextMenu = 82
  CursorChange = 183
  DeferredDelete = 52
  DragEnter = 60
  DragLeave = 62
  DragMove = 61
  Drop = 63
  DynamicPropertyChange = 170
  EnabledChange = 98
  Enter = 10
  EnterWhatsThisMode = 124
  FileOpen = 116
  FocusIn = 8
  FocusOut = 9
  FontChange = 97
  Gesture = 198
  GestureOverride = 202
  GrabKeyboard = 188
  GrabMouse = 186
  GraphicsSceneContextMenu = 159
  GraphicsSceneDragEnter = 164
  GraphicsSceneDragLeave = 166
  GraphicsSceneDragMove = 165
  GraphicsSceneDrop = 167
  GraphicsSceneHelp = 163
  GraphicsSceneHoverEnter = 160
  GraphicsSceneHoverLeave = 162
  GraphicsSceneHoverMove = 161
  GraphicsSceneMouseDoubleClick = 158
  GraphicsSceneMouseMove = 155
  GraphicsSceneMousePress = 156
  GraphicsSceneMouseRelease = 157
  GraphicsSceneMove = 182
  GraphicsSceneResize = 181
  GraphicsSceneWheel = 168
  Hide = 18
  HideToParent = 27
  HoverEnter = 127
  HoverLeave = 128
  HoverMove = 129
  IconDrag = 96
  IconTextChange = 101
  InputMethod = 83
  KeyPress = 6
  KeyRelease = 7
  KeyboardLayoutChange = 169
  LanguageChange = 89
  LayoutDirectionChange = 90
  LayoutRequest = 76
  Leave = 11
  LeaveWhatsThisMode = 125
  LocaleChange = 88
  MaxUser = 65535
  MenubarUpdated = 153
  MetaCall = 43
  ModifiedChange = 102
  MouseButtonDblClick = 4
  MouseButtonPress = 2
  MouseButtonRelease = 3
  MouseMove = 5
  MouseTrackingChange = 109
  Move = 13
  OkRequest = 94
  Paint = 12
  PaletteChange = 39
  ParentAboutToChange = 131
  ParentChange = 21
  PlatformPanel = 212
  Polish = 75
  PolishRequest = 74
  QueryWhatsThis = 123
  RequestSoftwareInputPanel = 199
  Resize = 14
  Shortcut = 117
  ShortcutOverride = 51
  Show = 17
  ShowToParent = 26
  SockAct = 50
  StateMachineSignal = 192
  StateMachineWrapped = 193
  StatusTip = 112
  StyleChange = 100
  TabletEnterProximity = 171
  TabletLeaveProximity = 172
  TabletMove = 87
  TabletPress = 92
  TabletRelease = 93
  Timer = 1
  ToolBarChange = 120
  ToolTip = 110
  ToolTipChange = 184
  TouchBegin = 194
  TouchEnd = 196
  TouchUpdate = 195
  UngrabKeyboard = 189
  UngrabMouse = 187
  UpdateLater = 78
  UpdateRequest = 77
  User = 1000
  WhatsThis = 111
  WhatsThisClicked = 118
  Wheel = 31
  WinEventAct = 132
  WinIdChange = 203
  WindowActivate = 24
  WindowBlocked = 103
  WindowDeactivate = 25
  WindowIconChange = 34
  WindowStateChange = 105
  WindowTitleChange = 33
  WindowUnblocked = 104
  ZOrderChange = 126
  def accept(*a,**k): pass
  def ignore(*a,**k): pass
  def isAccepted(*a,**k): pass
  def registerEventType(*a,**k): pass
  def setAccepted(*a,**k): pass
  def spontaneous(*a,**k): pass
  def type(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QChildEvent(QEvent):
  pass

  def added(*a,**k): pass
  def child(*a,**k): pass
  def polished(*a,**k): pass
  def removed(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QDynamicPropertyChangeEvent(QEvent):
  pass

  def propertyName(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTimerEvent(QEvent):
  pass

  def timerId(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QRunnable(object):
  pass

  def autoDelete(*a,**k): pass
  def run(*a,**k): pass
  def setAutoDelete(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextCodec(object):
  pass
  ConvertInvalidToNull = -2147483648
  DefaultConversion = 0
  IgnoreHeader = 1
  def aliases(*a,**k): pass
  def availableCodecs(*a,**k): pass
  def availableMibs(*a,**k): pass
  def canEncode(*a,**k): pass
  def codecForCStrings(*a,**k): pass
  def codecForHtml(*a,**k): pass
  def codecForLocale(*a,**k): pass
  def codecForMib(*a,**k): pass
  def codecForName(*a,**k): pass
  def codecForTr(*a,**k): pass
  def codecForUtfText(*a,**k): pass
  def convertToUnicode(*a,**k): pass
  def fromUnicode(*a,**k): pass
  def makeDecoder(*a,**k): pass
  def makeEncoder(*a,**k): pass
  def mibEnum(*a,**k): pass
  def name(*a,**k): pass
  def setCodecForCStrings(*a,**k): pass
  def setCodecForLocale(*a,**k): pass
  def setCodecForTr(*a,**k): pass
  def toUnicode(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextDecoder(object):
  pass

  def toUnicode(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class QTextEncoder(object):
  pass

  def fromUnicode(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class Qt(object):
  pass
  AA_CaptureMultimediaKeys = 11
  AA_DontCreateNativeWidgetSiblings = 4
  AA_DontShowIconsInMenus = 2
  AA_DontUseNativeMenuBar = 6
  AA_ImmediateWidgetCreation = 0
  AA_MSWindowsUseDirect3DByDefault = 1
  AA_MacDontSwapCtrlAndMeta = 7
  AA_MacPluginApplication = 5
  AA_NativeWindows = 3
  AA_S60DisablePartialScreenInputMode = 9
  AA_S60DontConstructApplicationPanes = 8
  AA_X11InitThreads = 10
  ALT = 134217728
  AbsoluteSize = 0
  AccessibleDescriptionRole = 12
  AccessibleTextRole = 11
  ActionMask = 255
  ActionsContextMenu = 2
  ActiveWindowFocusReason = 3
  AlignAbsolute = 16
  AlignBottom = 64
  AlignCenter = 132
  AlignHCenter = 4
  AlignHorizontal_Mask = 31
  AlignJustify = 8
  AlignLeading = 1
  AlignLeft = 1
  AlignRight = 2
  AlignTop = 32
  AlignTrailing = 2
  AlignVCenter = 128
  AlignVertical_Mask = 224
  AllDockWidgetAreas = 15
  AllToolBarAreas = 15
  AltModifier = 134217728
  AnchorBottom = 5
  AnchorHorizontalCenter = 1
  AnchorHref = 1
  AnchorLeft = 0
  AnchorName = 0
  AnchorRight = 2
  AnchorTop = 3
  AnchorVerticalCenter = 4
  ApplicationModal = 2
  ApplicationShortcut = 2
  ArrowCursor = 0
  AscendingOrder = 0
  AutoColor = 0
  AutoCompatConnection = 3
  AutoConnection = 0
  AutoDither = 0
  AutoText = 2
  AvoidDither = 128
  BDiagPattern = 12
  BackgroundColorRole = 8
  BackgroundRole = 8
  BacktabFocusReason = 2
  BevelJoin = 64
  BitmapCursor = 24
  BlankCursor = 10
  BlockingQueuedConnection = 4
  BottomDockWidgetArea = 8
  BottomLeftCorner = 2
  BottomLeftSection = 8
  BottomRightCorner = 3
  BottomRightSection = 6
  BottomSection = 7
  BottomToolBarArea = 8
  BusyCursor = 16
  BypassGraphicsProxyWidget = 536870912
  CTRL = 67108864
  CaseInsensitive = 0
  CaseSensitive = 1
  CheckStateRole = 10
  Checked = 2
  ClickFocus = 2
  ClosedHandCursor = 18
  ColorOnly = 3
  ConicalGradientPattern = 17
  ContainsItemBoundingRect = 2
  ContainsItemShape = 0
  ControlModifier = 67108864
  CopyAction = 1
  CrossCursor = 2
  CrossPattern = 11
  CustomContextMenu = 3
  CustomCursor = 25
  CustomDashLine = 6
  CustomGesture = 256
  CustomizeWindowHint = 33554432
  DashDotDotLine = 5
  DashDotLine = 4
  DashLine = 2
  DecorationRole = 1
  DefaultContextMenu = 1
  DefaultLocaleLongDate = 7
  DefaultLocaleShortDate = 6
  Dense1Pattern = 2
  Dense2Pattern = 3
  Dense3Pattern = 4
  Dense4Pattern = 5
  Dense5Pattern = 6
  Dense6Pattern = 7
  Dense7Pattern = 8
  DescendingOrder = 1
  Desktop = 17
  DeviceCoordinates = 0
  DiagCrossPattern = 14
  Dialog = 3
  DiffuseAlphaDither = 8
  DiffuseDither = 0
  DirectConnection = 1
  DisplayRole = 0
  DockWidgetArea_Mask = 15
  DontStartGestureOnChildren = 1
  DotLine = 3
  DownArrow = 2
  DragCopyCursor = 19
  DragLinkCursor = 21
  DragMoveCursor = 20
  Drawer = 7
  EditRole = 2
  ElideLeft = 0
  ElideMiddle = 2
  ElideNone = 3
  ElideRight = 1
  FDiagPattern = 13
  FastTransformation = 0
  FlatCap = 0
  FontRole = 6
  ForbiddenCursor = 14
  ForegroundRole = 9
  FramelessWindowHint = 2048
  Friday = 5
  GestureCanceled = 4
  GestureFinished = 3
  GestureStarted = 1
  GestureUpdated = 2
  GroupSwitchModifier = 1073741824
  HighEventPriority = 1
  HorPattern = 9
  Horizontal = 1
  IBeamCursor = 4
  ISODate = 1
  IgnoreAction = 0
  IgnoreAspectRatio = 0
  IgnoredGesturesPropagateToParent = 4
  ImAnchorPosition = 6
  ImCurrentSelection = 4
  ImCursorPosition = 2
  ImFont = 1
  ImMaximumTextLength = 5
  ImMicroFocus = 0
  ImSurroundingText = 3
  ImhDialableCharactersOnly = 1048576
  ImhDigitsOnly = 65536
  ImhEmailCharactersOnly = 2097152
  ImhExclusiveInputMask = -65536
  ImhFormattedNumbersOnly = 131072
  ImhHiddenText = 1
  ImhLowercaseOnly = 524288
  ImhNoAutoUppercase = 2
  ImhNoPredictiveText = 32
  ImhNone = 0
  ImhPreferLowercase = 16
  ImhPreferNumbers = 4
  ImhPreferUppercase = 8
  ImhUppercaseOnly = 262144
  ImhUrlCharactersOnly = 4194304
  InitialSortOrderRole = 14
  IntersectClip = 2
  IntersectsItemBoundingRect = 3
  IntersectsItemShape = 1
  ItemIsDragEnabled = 4
  ItemIsDropEnabled = 8
  ItemIsEditable = 2
  ItemIsEnabled = 32
  ItemIsSelectable = 1
  ItemIsTristate = 64
  ItemIsUserCheckable = 16
  KeepAspectRatio = 1
  KeepAspectRatioByExpanding = 2
  Key_0 = 48
  Key_1 = 49
  Key_2 = 50
  Key_3 = 51
  Key_4 = 52
  Key_5 = 53
  Key_6 = 54
  Key_7 = 55
  Key_8 = 56
  Key_9 = 57
  Key_A = 65
  Key_AE = 198
  Key_Aacute = 193
  Key_Acircumflex = 194
  Key_AddFavorite = 16777408
  Key_Adiaeresis = 196
  Key_Agrave = 192
  Key_Alt = 16777251
  Key_AltGr = 16781571
  Key_Ampersand = 38
  Key_Any = 32
  Key_Apostrophe = 39
  Key_ApplicationLeft = 16777415
  Key_ApplicationRight = 16777416
  Key_Aring = 197
  Key_AsciiCircum = 94
  Key_AsciiTilde = 126
  Key_Asterisk = 42
  Key_At = 64
  Key_Atilde = 195
  Key_AudioCycleTrack = 16777478
  Key_AudioForward = 16777474
  Key_AudioRandomPlay = 16777476
  Key_AudioRepeat = 16777475
  Key_AudioRewind = 16777413
  Key_Away = 16777464
  Key_B = 66
  Key_Back = 16777313
  Key_BackForward = 16777414
  Key_Backslash = 92
  Key_Backspace = 16777219
  Key_Backtab = 16777218
  Key_Bar = 124
  Key_BassBoost = 16777331
  Key_BassDown = 16777333
  Key_BassUp = 16777332
  Key_Battery = 16777470
  Key_Bluetooth = 16777471
  Key_Book = 16777417
  Key_BraceLeft = 123
  Key_BraceRight = 125
  Key_BracketLeft = 91
  Key_BracketRight = 93
  Key_BrightnessAdjust = 16777410
  Key_C = 67
  Key_CD = 16777418
  Key_Calculator = 16777419
  Key_Calendar = 16777444
  Key_Call = 17825796
  Key_Camera = 17825824
  Key_CameraFocus = 17825825
  Key_Cancel = 16908289
  Key_CapsLock = 16777252
  Key_Ccedilla = 199
  Key_Clear = 16777227
  Key_ClearGrab = 16777421
  Key_Close = 16777422
  Key_Codeinput = 16781623
  Key_Colon = 58
  Key_Comma = 44
  Key_Community = 16777412
  Key_Context1 = 17825792
  Key_Context2 = 17825793
  Key_Context3 = 17825794
  Key_Context4 = 17825795
  Key_ContrastAdjust = 16777485
  Key_Control = 16777249
  Key_Copy = 16777423
  Key_Cut = 16777424
  Key_D = 68
  Key_DOS = 16777426
  Key_Dead_Abovedot = 16781910
  Key_Dead_Abovering = 16781912
  Key_Dead_Acute = 16781905
  Key_Dead_Belowdot = 16781920
  Key_Dead_Breve = 16781909
  Key_Dead_Caron = 16781914
  Key_Dead_Cedilla = 16781915
  Key_Dead_Circumflex = 16781906
  Key_Dead_Diaeresis = 16781911
  Key_Dead_Doubleacute = 16781913
  Key_Dead_Grave = 16781904
  Key_Dead_Hook = 16781921
  Key_Dead_Horn = 16781922
  Key_Dead_Iota = 16781917
  Key_Dead_Macron = 16781908
  Key_Dead_Ogonek = 16781916
  Key_Dead_Semivoiced_Sound = 16781919
  Key_Dead_Tilde = 16781907
  Key_Dead_Voiced_Sound = 16781918
  Key_Delete = 16777223
  Key_Direction_L = 16777305
  Key_Direction_R = 16777312
  Key_Display = 16777425
  Key_Documents = 16777427
  Key_Dollar = 36
  Key_Down = 16777237
  Key_E = 69
  Key_ETH = 208
  Key_Eacute = 201
  Key_Ecircumflex = 202
  Key_Ediaeresis = 203
  Key_Egrave = 200
  Key_Eisu_Shift = 16781615
  Key_Eisu_toggle = 16781616
  Key_Eject = 16777401
  Key_End = 16777233
  Key_Enter = 16777221
  Key_Equal = 61
  Key_Escape = 16777216
  Key_Excel = 16777428
  Key_Exclam = 33
  Key_Execute = 16908291
  Key_Explorer = 16777429
  Key_F = 70
  Key_F1 = 16777264
  Key_F10 = 16777273
  Key_F11 = 16777274
  Key_F12 = 16777275
  Key_F13 = 16777276
  Key_F14 = 16777277
  Key_F15 = 16777278
  Key_F16 = 16777279
  Key_F17 = 16777280
  Key_F18 = 16777281
  Key_F19 = 16777282
  Key_F2 = 16777265
  Key_F20 = 16777283
  Key_F21 = 16777284
  Key_F22 = 16777285
  Key_F23 = 16777286
  Key_F24 = 16777287
  Key_F25 = 16777288
  Key_F26 = 16777289
  Key_F27 = 16777290
  Key_F28 = 16777291
  Key_F29 = 16777292
  Key_F3 = 16777266
  Key_F30 = 16777293
  Key_F31 = 16777294
  Key_F32 = 16777295
  Key_F33 = 16777296
  Key_F34 = 16777297
  Key_F35 = 16777298
  Key_F4 = 16777267
  Key_F5 = 16777268
  Key_F6 = 16777269
  Key_F7 = 16777270
  Key_F8 = 16777271
  Key_F9 = 16777272
  Key_Favorites = 16777361
  Key_Finance = 16777411
  Key_Flip = 17825798
  Key_Forward = 16777314
  Key_G = 71
  Key_Game = 16777430
  Key_Go = 16777431
  Key_Greater = 62
  Key_H = 72
  Key_Hangul = 16781617
  Key_Hangul_Banja = 16781625
  Key_Hangul_End = 16781619
  Key_Hangul_Hanja = 16781620
  Key_Hangul_Jamo = 16781621
  Key_Hangul_Jeonja = 16781624
  Key_Hangul_PostHanja = 16781627
  Key_Hangul_PreHanja = 16781626
  Key_Hangul_Romaja = 16781622
  Key_Hangul_Special = 16781631
  Key_Hangul_Start = 16781618
  Key_Hangup = 17825797
  Key_Hankaku = 16781609
  Key_Help = 16777304
  Key_Henkan = 16781603
  Key_Hibernate = 16777480
  Key_Hiragana = 16781605
  Key_Hiragana_Katakana = 16781607
  Key_History = 16777407
  Key_Home = 16777232
  Key_HomePage = 16777360
  Key_HotLinks = 16777409
  Key_Hyper_L = 16777302
  Key_Hyper_R = 16777303
  Key_I = 73
  Key_Iacute = 205
  Key_Icircumflex = 206
  Key_Idiaeresis = 207
  Key_Igrave = 204
  Key_Insert = 16777222
  Key_J = 74
  Key_K = 75
  Key_Kana_Lock = 16781613
  Key_Kana_Shift = 16781614
  Key_Kanji = 16781601
  Key_Katakana = 16781606
  Key_KeyboardBrightnessDown = 16777398
  Key_KeyboardBrightnessUp = 16777397
  Key_KeyboardLightOnOff = 16777396
  Key_L = 76
  Key_LastNumberRedial = 17825801
  Key_Launch0 = 16777378
  Key_Launch1 = 16777379
  Key_Launch2 = 16777380
  Key_Launch3 = 16777381
  Key_Launch4 = 16777382
  Key_Launch5 = 16777383
  Key_Launch6 = 16777384
  Key_Launch7 = 16777385
  Key_Launch8 = 16777386
  Key_Launch9 = 16777387
  Key_LaunchA = 16777388
  Key_LaunchB = 16777389
  Key_LaunchC = 16777390
  Key_LaunchD = 16777391
  Key_LaunchE = 16777392
  Key_LaunchF = 16777393
  Key_LaunchG = 16777486
  Key_LaunchH = 16777487
  Key_LaunchMail = 16777376
  Key_LaunchMedia = 16777377
  Key_Left = 16777234
  Key_Less = 60
  Key_LightBulb = 16777405
  Key_LogOff = 16777433
  Key_M = 77
  Key_MailForward = 16777467
  Key_Market = 16777434
  Key_Massyo = 16781612
  Key_MediaLast = 16842751
  Key_MediaNext = 16777347
  Key_MediaPause = 16777349
  Key_MediaPlay = 16777344
  Key_MediaPrevious = 16777346
  Key_MediaRecord = 16777348
  Key_MediaStop = 16777345
  Key_MediaTogglePlayPause = 16777350
  Key_Meeting = 16777435
  Key_Memo = 16777404
  Key_Menu = 16777301
  Key_MenuKB = 16777436
  Key_MenuPB = 16777437
  Key_Messenger = 16777465
  Key_Meta = 16777250
  Key_Minus = 45
  Key_Mode_switch = 16781694
  Key_MonBrightnessDown = 16777395
  Key_MonBrightnessUp = 16777394
  Key_Muhenkan = 16781602
  Key_Multi_key = 16781600
  Key_MultipleCandidate = 16781629
  Key_Music = 16777469
  Key_MySites = 16777438
  Key_N = 78
  Key_News = 16777439
  Key_No = 16842754
  Key_Ntilde = 209
  Key_NumLock = 16777253
  Key_NumberSign = 35
  Key_O = 79
  Key_Oacute = 211
  Key_Ocircumflex = 212
  Key_Odiaeresis = 214
  Key_OfficeHome = 16777440
  Key_Ograve = 210
  Key_Ooblique = 216
  Key_OpenUrl = 16777364
  Key_Option = 16777441
  Key_Otilde = 213
  Key_P = 80
  Key_PageDown = 16777239
  Key_PageUp = 16777238
  Key_ParenLeft = 40
  Key_ParenRight = 41
  Key_Paste = 16777442
  Key_Pause = 16777224
  Key_Percent = 37
  Key_Period = 46
  Key_Phone = 16777443
  Key_Pictures = 16777468
  Key_Play = 16908293
  Key_Plus = 43
  Key_PowerDown = 16777483
  Key_PowerOff = 16777399
  Key_PreviousCandidate = 16781630
  Key_Print = 16777225
  Key_Printer = 16908290
  Key_Q = 81
  Key_Question = 63
  Key_QuoteDbl = 34
  Key_QuoteLeft = 96
  Key_R = 82
  Key_Refresh = 16777316
  Key_Reload = 16777446
  Key_Reply = 16777445
  Key_Return = 16777220
  Key_Right = 16777236
  Key_Romaji = 16781604
  Key_RotateWindows = 16777447
  Key_RotationKB = 16777449
  Key_RotationPB = 16777448
  Key_S = 83
  Key_Save = 16777450
  Key_ScreenSaver = 16777402
  Key_ScrollLock = 16777254
  Key_Search = 16777362
  Key_Select = 16842752
  Key_Semicolon = 59
  Key_Send = 16777451
  Key_Shift = 16777248
  Key_Shop = 16777406
  Key_SingleCandidate = 16781628
  Key_Slash = 47
  Key_Sleep = 16908292
  Key_Space = 32
  Key_Spell = 16777452
  Key_SplitScreen = 16777453
  Key_Standby = 16777363
  Key_Stop = 16777315
  Key_Subtitle = 16777477
  Key_Super_L = 16777299
  Key_Super_R = 16777300
  Key_Support = 16777454
  Key_Suspend = 16777484
  Key_SysReq = 16777226
  Key_T = 84
  Key_THORN = 222
  Key_Tab = 16777217
  Key_TaskPane = 16777455
  Key_Terminal = 16777456
  Key_Time = 16777479
  Key_ToDoList = 16777420
  Key_ToggleCallHangup = 17825799
  Key_Tools = 16777457
  Key_TopMenu = 16777482
  Key_Touroku = 16781611
  Key_Travel = 16777458
  Key_TrebleDown = 16777335
  Key_TrebleUp = 16777334
  Key_U = 85
  Key_UWB = 16777473
  Key_Uacute = 218
  Key_Ucircumflex = 219
  Key_Udiaeresis = 220
  Key_Ugrave = 217
  Key_Underscore = 95
  Key_Up = 16777235
  Key_V = 86
  Key_Video = 16777459
  Key_View = 16777481
  Key_VoiceDial = 17825800
  Key_VolumeDown = 16777328
  Key_VolumeMute = 16777329
  Key_VolumeUp = 16777330
  Key_W = 87
  Key_WLAN = 16777472
  Key_WWW = 16777403
  Key_WakeUp = 16777400
  Key_WebCam = 16777466
  Key_Word = 16777460
  Key_X = 88
  Key_Xfer = 16777461
  Key_Y = 89
  Key_Yacute = 221
  Key_Yes = 16842753
  Key_Z = 90
  Key_Zenkaku = 16781608
  Key_Zenkaku_Hankaku = 16781610
  Key_Zoom = 16908294
  Key_ZoomIn = 16777462
  Key_ZoomOut = 16777463
  Key_acute = 180
  Key_brokenbar = 166
  Key_cedilla = 184
  Key_cent = 162
  Key_copyright = 169
  Key_currency = 164
  Key_degree = 176
  Key_diaeresis = 168
  Key_division = 247
  Key_exclamdown = 161
  Key_guillemotleft = 171
  Key_guillemotright = 187
  Key_hyphen = 173
  Key_iTouch = 16777432
  Key_macron = 175
  Key_masculine = 186
  Key_mu = 181
  Key_multiply = 215
  Key_nobreakspace = 160
  Key_notsign = 172
  Key_onehalf = 189
  Key_onequarter = 188
  Key_onesuperior = 185
  Key_ordfeminine = 170
  Key_paragraph = 182
  Key_periodcentered = 183
  Key_plusminus = 177
  Key_questiondown = 191
  Key_registered = 174
  Key_section = 167
  Key_ssharp = 223
  Key_sterling = 163
  Key_threequarters = 190
  Key_threesuperior = 179
  Key_twosuperior = 178
  Key_unknown = 33554431
  Key_ydiaeresis = 255
  Key_yen = 165
  KeyboardModifierMask = -33554432
  KeypadModifier = 536870912
  LastCursor = 21
  LayoutDirectionAuto = 2
  LeftArrow = 3
  LeftButton = 1
  LeftDockWidgetArea = 1
  LeftSection = 1
  LeftToRight = 0
  LeftToolBarArea = 1
  LinearGradientPattern = 15
  LinkAction = 4
  LinksAccessibleByKeyboard = 8
  LinksAccessibleByMouse = 4
  LocalDate = 2
  LocalTime = 0
  LocaleDate = 3
  LogText = 3
  LogicalCoordinates = 1
  LogicalMoveStyle = 0
  LowEventPriority = -1
  META = 268435456
  MODIFIER_MASK = -33554432
  MPenCapStyle = 48
  MPenJoinStyle = 448
  MPenStyle = 15
  MSWindowsFixedSizeDialogHint = 256
  MSWindowsOwnDC = 512
  MacWindowToolBarButtonHint = 268435456
  MaskInColor = 0
  MaskOutColor = 1
  MatchCaseSensitive = 16
  MatchContains = 1
  MatchEndsWith = 3
  MatchExactly = 0
  MatchFixedString = 8
  MatchRecursive = 64
  MatchRegExp = 4
  MatchStartsWith = 2
  MatchWildcard = 5
  MatchWrap = 32
  MaximumSize = 2
  MenuBarFocusReason = 6
  MetaModifier = 268435456
  MidButton = 4
  MiddleButton = 4
  MinimumDescent = 3
  MinimumSize = 0
  MiterJoin = 0
  Monday = 1
  MonoOnly = 2
  MouseFocusReason = 0
  MoveAction = 2
  NavigationModeCursorAuto = 3
  NavigationModeCursorForceVisible = 4
  NavigationModeKeypadDirectional = 2
  NavigationModeKeypadTabOrder = 1
  NavigationModeNone = 0
  NoArrow = 0
  NoBrush = 0
  NoButton = 0
  NoClip = 0
  NoContextMenu = 0
  NoDockWidgetArea = 0
  NoFocus = 0
  NoFocusReason = 8
  NoItemFlags = 0
  NoModifier = 0
  NoPen = 0
  NoSection = 0
  NoTextInteraction = 0
  NoToolBarArea = 0
  NonModal = 0
  NormalEventPriority = 0
  OddEvenFill = 0
  OffsetFromUTC = 2
  OpaqueMode = 1
  OpenHandCursor = 17
  OrderedAlphaDither = 4
  OrderedDither = 16
  OtherFocusReason = 7
  PanGesture = 3
  PartiallyChecked = 1
  PinchGesture = 4
  PlainText = 0
  PointingHandCursor = 13
  Popup = 9
  PopupFocusReason = 4
  PreferDither = 64
  PreferredSize = 1
  PreventContextMenu = 4
  QueuedConnection = 2
  RadialGradientPattern = 16
  ReceivePartialGestures = 2
  RelativeSize = 1
  RepeatTile = 1
  ReplaceClip = 1
  RichText = 1
  RightArrow = 4
  RightButton = 2
  RightDockWidgetArea = 2
  RightSection = 5
  RightToLeft = 1
  RightToolBarArea = 2
  RoundCap = 32
  RoundJoin = 128
  RoundTile = 2
  SHIFT = 33554432
  Saturday = 6
  ScrollBarAlwaysOff = 1
  ScrollBarAlwaysOn = 2
  ScrollBarAsNeeded = 0
  Sheet = 5
  ShiftModifier = 33554432
  ShortcutFocusReason = 5
  SizeAllCursor = 9
  SizeBDiagCursor = 7
  SizeFDiagCursor = 8
  SizeHintRole = 13
  SizeHorCursor = 6
  SizeVerCursor = 5
  SmoothTransformation = 1
  SolidLine = 1
  SolidPattern = 1
  SplashScreen = 15
  SplitHCursor = 12
  SplitVCursor = 11
  SquareCap = 16
  StatusTipRole = 4
  StretchTile = 0
  StrongFocus = 11
  SubWindow = 18
  Sunday = 7
  SvgMiterJoin = 256
  SwipeGesture = 5
  SystemLocaleDate = 2
  SystemLocaleLongDate = 5
  SystemLocaleShortDate = 4
  TabFocus = 1
  TabFocusReason = 1
  TapAndHoldGesture = 2
  TapGesture = 1
  TargetMoveAction = 32770
  TextAlignmentRole = 7
  TextBrowserInteraction = 13
  TextColorRole = 9
  TextDate = 0
  TextDontClip = 512
  TextDontPrint = 16384
  TextEditable = 16
  TextEditorInteraction = 19
  TextExpandTabs = 1024
  TextHideMnemonic = 32768
  TextIncludeTrailingSpaces = 134217728
  TextJustificationForced = 65536
  TextSelectableByKeyboard = 2
  TextSelectableByMouse = 1
  TextShowMnemonic = 2048
  TextSingleLine = 256
  TextWordWrap = 4096
  TextWrapAnywhere = 8192
  TexturePattern = 24
  ThresholdAlphaDither = 0
  ThresholdDither = 32
  Thursday = 4
  TitleBarArea = 9
  Tool = 11
  ToolBarArea_Mask = 15
  ToolButtonFollowStyle = 4
  ToolButtonIconOnly = 0
  ToolButtonTextBesideIcon = 2
  ToolButtonTextOnly = 1
  ToolButtonTextUnderIcon = 3
  ToolTip = 13
  ToolTipRole = 3
  TopDockWidgetArea = 4
  TopLeftCorner = 0
  TopLeftSection = 2
  TopRightCorner = 1
  TopRightSection = 4
  TopSection = 3
  TopToolBarArea = 4
  TouchPointMoved = 2
  TouchPointPressed = 1
  TouchPointReleased = 8
  TouchPointStationary = 4
  TransparentMode = 0
  Tuesday = 2
  UI_AnimateCombo = 3
  UI_AnimateMenu = 1
  UI_AnimateToolBox = 6
  UI_AnimateTooltip = 4
  UI_FadeMenu = 2
  UI_FadeTooltip = 5
  UI_General = 0
  UNICODE_ACCEL = 0
  UTC = 1
  Unchecked = 0
  UniqueConnection = 128
  UniteClip = 3
  UpArrow = 1
  UpArrowCursor = 1
  UserRole = 32
  VerPattern = 10
  Vertical = 2
  VisualMoveStyle = 1
  WA_AcceptDrops = 78
  WA_AcceptTouchEvents = 121
  WA_AlwaysShowToolTips = 84
  WA_AttributeCount = 135
  WA_AutoOrientation = 130
  WA_CustomWhatsThis = 47
  WA_DeleteOnClose = 55
  WA_Disabled = 0
  WA_DontCreateNativeAncestors = 101
  WA_ForceDisabled = 32
  WA_ForceUpdatesDisabled = 59
  WA_GrabbedShortcut = 50
  WA_GroupLeader = 72
  WA_Hover = 74
  WA_InputMethodEnabled = 14
  WA_InputMethodTransparent = 75
  WA_InvalidSize = 45
  WA_KeyCompression = 33
  WA_KeyboardFocusChange = 77
  WA_LaidOut = 7
  WA_LayoutOnEntireRect = 48
  WA_LayoutUsesWidgetRect = 92
  WA_LockLandscapeOrientation = 129
  WA_LockPortraitOrientation = 128
  WA_MSWindowsUseDirect3D = 94
  WA_MacAlwaysShowToolWindow = 96
  WA_MacBrushedMetal = 46
  WA_MacFrameworkScaled = 117
  WA_MacMetalStyle = 46
  WA_MacMiniSize = 91
  WA_MacNoClickThrough = 12
  WA_MacNoShadow = 134
  WA_MacNormalSize = 89
  WA_MacOpaqueSizeGrip = 85
  WA_MacShowFocusRect = 88
  WA_MacSmallSize = 90
  WA_MacVariableSize = 102
  WA_Mapped = 11
  WA_MergeSoftkeys = 124
  WA_MergeSoftkeysRecursively = 125
  WA_MouseNoMask = 71
  WA_MouseTracking = 2
  WA_Moved = 43
  WA_NativeWindow = 100
  WA_NoChildEventsForParent = 58
  WA_NoChildEventsFromChildren = 39
  WA_NoMousePropagation = 73
  WA_NoMouseReplay = 54
  WA_NoSystemBackground = 9
  WA_NoX11EventCompression = 81
  WA_OpaquePaintEvent = 4
  WA_OutsideWSRange = 49
  WA_PaintOnScreen = 8
  WA_PaintOutsidePaintEvent = 13
  WA_PaintUnclipped = 52
  WA_PendingMoveEvent = 34
  WA_PendingResizeEvent = 35
  WA_PendingUpdate = 44
  WA_QuitOnClose = 76
  WA_Resized = 42
  WA_RightToLeft = 56
  WA_SetCursor = 38
  WA_SetFont = 37
  WA_SetLayoutDirection = 57
  WA_SetLocale = 87
  WA_SetPalette = 36
  WA_SetStyle = 86
  WA_SetWindowIcon = 53
  WA_ShowWithoutActivating = 98
  WA_StaticContents = 5
  WA_StyleSheet = 97
  WA_StyledBackground = 93
  WA_TintedBackground = 82
  WA_TouchPadAcceptSingleTouchEvents = 123
  WA_TranslucentBackground = 120
  WA_TransparentForMouseEvents = 51
  WA_UnderMouse = 1
  WA_UpdatesDisabled = 10
  WA_WState_CompressKeys = 61
  WA_WState_ConfigPending = 64
  WA_WState_Created = 60
  WA_WState_ExplicitShowHide = 69
  WA_WState_Hidden = 16
  WA_WState_InPaintEvent = 62
  WA_WState_OwnSizePolicy = 68
  WA_WState_Polished = 66
  WA_WState_Reparented = 63
  WA_WState_Visible = 15
  WA_WindowModified = 41
  WA_WindowPropagation = 80
  WA_X11DoNotAcceptFocus = 132
  WA_X11NetWmWindowTypeCombo = 115
  WA_X11NetWmWindowTypeDND = 116
  WA_X11NetWmWindowTypeDesktop = 104
  WA_X11NetWmWindowTypeDialog = 110
  WA_X11NetWmWindowTypeDock = 105
  WA_X11NetWmWindowTypeDropDownMenu = 111
  WA_X11NetWmWindowTypeMenu = 107
  WA_X11NetWmWindowTypeNotification = 114
  WA_X11NetWmWindowTypePopupMenu = 112
  WA_X11NetWmWindowTypeSplash = 109
  WA_X11NetWmWindowTypeToolBar = 106
  WA_X11NetWmWindowTypeToolTip = 113
  WA_X11NetWmWindowTypeUtility = 108
  WA_X11OpenGLOverlay = 83
  WaitCursor = 3
  Wednesday = 3
  WhatsThisCursor = 15
  WhatsThisRole = 5
  WheelFocus = 15
  Widget = 0
  WidgetShortcut = 0
  WidgetWithChildrenShortcut = 3
  WindingFill = 1
  Window = 1
  WindowActive = 8
  WindowCancelButtonHint = 1048576
  WindowCloseButtonHint = 134217728
  WindowContextHelpButtonHint = 65536
  WindowFullScreen = 4
  WindowMaximizeButtonHint = 32768
  WindowMaximized = 2
  WindowMinMaxButtonsHint = 49152
  WindowMinimizeButtonHint = 16384
  WindowMinimized = 1
  WindowModal = 1
  WindowNoState = 0
  WindowOkButtonHint = 524288
  WindowShadeButtonHint = 131072
  WindowShortcut = 1
  WindowSoftkeysRespondHint = -2147483648
  WindowSoftkeysVisibleHint = 1073741824
  WindowStaysOnBottomHint = 67108864
  WindowStaysOnTopHint = 262144
  WindowSystemMenuHint = 8192
  WindowTitleHint = 4096
  WindowType_Mask = 255
  X11BypassWindowManagerHint = 1024
  XAxis = 0
  XButton1 = 8
  XButton2 = 16
  YAxis = 1
  ZAxis = 2
  black = 2
  blue = 9
  color0 = 0
  color1 = 1
  cyan = 10
  darkBlue = 15
  darkCyan = 16
  darkGray = 4
  darkGreen = 14
  darkMagenta = 17
  darkRed = 13
  darkYellow = 18
  gray = 5
  green = 8
  lightGray = 6
  magenta = 11
  red = 7
  transparent = 19
  white = 3
  yellow = 12

  def __init__(self, *args, **kwargs): pass


class pyqtBoundSignal(object):
  pass

  def connect(*a,**k): pass
  def disconnect(*a,**k): pass
  def emit(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class pyqtProperty(object):
  pass

  def deleter(*a,**k): pass
  def getter(*a,**k): pass
  def read(*a,**k): pass
  def reset(*a,**k): pass
  def setter(*a,**k): pass
  def write(*a,**k): pass
  def __init__(self, *args, **kwargs): pass


class pyqtSignal(object):
  pass


  def __init__(self, *args, **kwargs): pass


