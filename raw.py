from typing import TypedDict, Callable, Union, Dict, List, Any, Iterable, Literal

#Note: no docs for Memory or RawMemory

#will create a copy with all typings unneccesary for casting removed once finished

from enums import *

#MapVisual.import -> from_string
#MapVisual.export -> to_string

#GameObject is a Union of all possible game objects

NumberType = int

StrOrRoom = Union[str, Room]

class HeapStatType(TypedDict):
	total_heap_size: NumberType
	total_heap_size_executable: NumberType
	total_physical_size: NumberType
	total_available_size: NumberType
	used_heap_size: NumberType
	heap_size_limit: NumberType
	malloced_memory: NumberType
	peak_malloced_memory: NumberType
	does_zap_garbage: NumberType
	externally_allocated_size: NumberType

class CPUType(TypedDict):
	limit: NumberType
	tickLimit: NumberType
	bucket: NumberType
	shardLimits: Dict[str, NumberType]
	unlocked: bool
	unlockedTime: NumberType
	getHeapStatistics: Optional[Callable[[], HeapStatType]]
	getUsed: Callable[[], NumberType]
	halt: Optional[Callable[[], None]]
	setShardLimits: Callable[[Dict[str, NumberType]], NumberType]
	unlock: Callable[[], NumberType]
	generatePixel: Callable[[], NumberType]

class GLType(TypedDict):
	level: NumberType
	progress: NumberType
	progressTotal: NumberType

class ShardType(TypedDict):
	name: str
	type: str
	ptr: bool

class MultiRoomRouteOpts(TypedDict):
	routeCallback: Callable[[str, str], NumberType]

class MultiRoomRouteOutput(TypedDict):
	exit: NumberType
	room: str

class RoomStatus(TypedDict):
	status: str
	timestamp: NumberType

class LineStyle(TypedDict):
	width: Optional[NumberType]
	color: Optional[str]
	opacity: Optional[NumberType]
	lineStyle: Optional[str]

class ShapeStyle(TypedDict):
	fill: Optional[str]
	opacity: Optional[NumberType]
	stroke: Optional[str]
	strokeWidth: Optional[NumberType]
	lineStyle: Optional[str]

class CircleStyle(ShapeStyle):
	radius: Optional[NumberType]

class TextStyle(TypedDict):
	color: Optional[str]
	fontFamily: Optional[str]
	fontSize: Optional[NumberType]
	fontStyle: Optional[str]
	fontVariant: Optional[str]
	stroke: Optional[str]
	strokeWidth: Optional[NumberType]
	backgroundColor: Optional[str]
	backgroundPadding: Optional[NumberType]
	align: Optional[str]
	opacity: Optional[NumberType]

class MapVisual():
	line: Callable[[RoomPos, RoomPos, Optional[LineStyle]], MapVisual]
	circle: Callable[[RoomPos, Optional[CircleStyle]], MapVisual]
	rect: Callable[[RoomPos, NumberType, NumberType, Optional[ShapeStyle]], MapVisual]
	poly: Callable[[List[RoomPos], Optional[ShapeStyle]], MapVisual]
	text: Callable[[str, RoomPos, Optional[TextStyle]], MapVisual]
	clear: Callable[[], MapVisual]
	getSize: Callable[[], NumberType]
	toString: Callable[[], str]
	fromString: Callable[[str], MapVisual]

class Map():
	describeExits: Callable[[str], Dict[str, str]]
	findExit: Callable[[*[StrOrRoom] * 2, Optional[RouteOpts]], Union[NumberType, NumberType]]
	findRoute: Callable[[*[StrOrRoom] * 2, Optional[MultiRoomRouteOpts]], Union[List[MultiRoomRouteOutput], NumberType]]
	getRoomLinearDistance: Callable[[str, str, Optional[bool]], NumberType]
	getRoomTerrain: Callable[[str], RoomTerrain]
	getWorldSize: Callable[[], NumberType]
	getRoomStatus: Callable[[str], RoomStatus]
	visual: MapVisual

class TransactionPlayer(TypedDict):
	username: str

class TransactionOrder(TypedDict):
	id: str
	type: str
	price: NumberType

class Transaction(TypedDict):
	transactionId: str
	time: NumberType
	sender: TransactionPlayer
	recipient: TransactionPlayer
	resourceType: str
	amount: NumberType
	to: str
	description: str
	order: TransactionOrder

Transaction.__annotations__.setdefault("from", str)

class Order(TypedDict):
	id: str
	created: NumberType
	active: bool
	type: str
	resourceType: str
	roomName: str
	amount: NumberType
	remainingAmount: NumberType
	totalAmount: NumberType
	price: NumberType

class OrderParams(TypedDict):
	type: str
	resourceType: str
	price: NumberType
	totalAmount: NumberType
	roomName: Optional[str]

LodashFilter = Callable[[Any, Union[str, NumberType], Iterable], bool]

class OrderData(TypedDict):
	id: str
	created: NumberType
	createdTimestamp: Optional[NumberType]
	type: str
	resourceType: str
	roomName: str
	amount: NumberType
	remainingAmount: NumberType
	price: NumberType

class ResourcePriceHistory(TypedDict):
	resourceType: str
	date: str
	transactions: NumberType
	volume: NumberType
	avgPrice: NumberType
	stddevPrice: NumberType

class Market():
	credits: NumberType
	incomingTransactions: List[Transaction]
	outgoingTransactions: List[Transaction]
	orders: Dict[str, Order]
	calcTransactionCost: Callable[[NumberType, str, str], NumberType]
	cancelOrder: Callable[[str], NumberType]
	changeOrderPrice: Callable[[str, NumberType], NumberType]
	createOrder: Callable[[OrderParams], NumberType]
	deal: Callable[[str, NumberType, Optional[str]], NumberType]
	extendOrder: Callable[[str, NumberType], NumberType]
	getAllOrders: Callable[[Optional[LodashFilter]], List[OrderData]]
	getHistory: Callable[[str], List[ResourcePriceHistory]]
	getOrderById: Callable[[str], OrderData]

class Game():
	constructionSites: Dict[str, ConstructionSite]
	cpu: CPUType
	creeps: Dict[str, Creep]
	flags: Dict[str, Flag]
	gcl: GLType
	gpl: GLType
	map: Map
	market: Market
	powerCreeps: Dict[str, PowerCreep]
	resources: ResourcesType
	rooms: Dict[str, Room]
	shard: ShardType
	spawns: Dict[str, StructureSpawn]
	structures: Dict[str, Structure]
	time: NumberType
	getObjectById: Callable([str], Union[GameObject, None])
	notify: Callable[[str, Optional[NumberType]], None]

class InterShardMemory():
	getLocal: Callable[[], str]
	setLocal: Callable[[str], None]
	getRemote: Callable[[str], str]

class PathFinderOpts(TypedDict):
	roomCallback: Optional[Callable[[str], Union[CostMatrix, bool]]]
	plainCost: Optional[NumberType]
	swampCost: Optional[NumberType]
	flee: Optional[bool]
	maxOps: Optional[NumberType]
	maxRooms: Optional[NumberType]
	maxCost: Optional[NumberType]
	heuristicWeight: Optional[NumberType]

class Path(TypedDict):
	path: List[RoomPos]
	ops: NumberType
	cost: NumberType
	incomplete: bool

class PathFinder():
	search: Callable[[RoomPos, Union[Goal, List[Goal]], Optional[PathFinderOpts]], Path]

class Effect(TypedDict):
	effect: NumberType
	level: Optional[NumberType]
	ticksRemaining: NumberType

class RoomObject():
	effects: List[Effect]
	pos: RoomPos
	room: Union[Room, None]

class OwnerDict(TypedDict):
	username: str

class ConstructionSite(RoomObject):
	id: str
	my: bool
	owner: OwnerDict
	progress: NumberType
	progressTotal: NumberType
	structureType: str
	remove: Callable[[], NumberType]

class CreepBodyPart(TypedDict):
	boost: Union[str, None]
	type: str
	hits: NumberType

class DropResourceData(TypedDict):
	resourceType: str
	amount: NumberType

class CreepMoveToOpts(RoomFindPathOpts):
	reusePath: Optional[NumberType]
	serializeMemory: Optional[bool]
	noPathFinding: Optional[bool]
	visualizePathStyle: Optional[RoomVisualPolyStyle]

Pos = Union[RoomObject, RoomPos]

class BaseCreep(RoomObject):
	hits: NumberType
	hitsMax: NumberType
	id: str
	memory: Any
	my: bool
	name: str
	owner: OwnerDict
	saying: str
	store: Store
	ticksToLive: NumberType
	cancelOrder: Callable[[str], NumberType]
	drop: Callable[[DropResourceData], NumberType]
	move: Callable[[Union[Creep, NumberType]], NumberType]
	moveByPath: Callable[[Union[list, str]], NumberType]
	moveTo: Union[
		Callable[[NumberType, NumberType, Optional[CreepMoveToOpts]], NumberType],
		Callable[[Pos, Optional[CreepMoveToOpts]], NumberType]]
	notifyWhenAttacked: Callable[[bool], NumberType]
	pickup: Callable[[Resource], NumberType]
	say: Callable[[str, Optional[bool]], NumberType]
	suicide: Callable[[], NumberType]
	transfer: Callable[[Union[Creep, PowerCreep, Structure], str, Optional[NumberType]], NumberType]
	withdraw: Callable[[Union[Structure, Tombstone, Ruin], str, Optional[NumberType]], NumberType]

class Creep(BaseCreep):
	body: List[CreepBodyPart]
	fatigue: NumberType
	spawning: bool
	attack: Callable[[Union[Creep, PowerCreep, Structure]], NumberType]
	attackController: Callable[[StructureController], NumberType]
	build: Callable[[ConstructionSite], NumberType]
	claimController: Callable[[StructureController], NumberType]
	dismantle: Callable[[Structure], NumberType]
	generateSafeMode: Callable[[StructureController], NumberType]
	getActiveBodyparts: Callable[[str], NumberType]
	harvest: Callable[[Union[Source, Mineral, Deposit]], NumberType]
	heal: Callable[[Union[Creep, PowerCreep]], NumberType]
	pull: Callable[[Creep], NumberType]
	rangedAttack: Callable[[Union[Creep, PowerCreep, Structure]], NumberType]
	rangedHeal: Callable[[Union[Creep, PowerCreep]], NumberType]
	rangedMassAttack: Callable[[], NumberType]
	repair: Callable[[Structure], NumberType]
	reserveController: Callable[[StructureController], NumberType]
	signController: Callable[[StructureController, str], NumberType]
	upgradeController: Callable[[StructureController], NumberType]

class Deposit(RoomObject):
	cooldown: NumberType
	depositType: str
	id: str
	lastCooldown: NumberType
	ticksToDecay: NumberType

class Flag(RoomObject):
	color: NumberType
	memory: Any
	name: str
	secondaryColor: NumberType
	remove: Callable[[], Literal[0]]
	setColor: Callable[[int, Optional[int]], NumberType]
	setPosition: Union[
		Callable[[NumberType, NumberType], NumberType]
		Callable[[Pos], NumberType]]

class Mineral(RoomObject):
	density: NumberType
	mineralAmount: NumberType
	mineralType: str
	id: str
	ticksToRegeneration: NumberType

class Nuke(RoomObject):
	id: str
	launchRoomName: str
	timeToLand: NumberType

class OwnedStructure(Structure):
	my: bool
	owner: OwnerDict

class CostMatrix():
	set: Callable[[NumberType, NumberType, NumberType], None]
	get: Callable[[NumberType, NumberType], NumberType]
	clone: Callable[[], CostMatrix]
	serialize: Callable[[], List[NumberType]]
	deserialize: Callable[[List[NumberType]], CostMatrix]

class PowerDict(TypedDict):
	level: NumberType
	cooldown: NumberType

class PowerCreep(BaseCreep):
	create: Callable[[str, str], NumberType]
	className: str
	deleteTime: NumberType
	level: NumberType
	powers: Dict[str, PowerDict]
	shard: str
	spawnCooldownTime: NumberType
	delete: Callable[[Optional[bool]], NumberType]
	enableRoom: Callable[[StructureController], NumberType]
	rename: Callable[[str], NumberType]
	renew: Callable[[Union[StructurePowerBank, StructurePowerSpawn]], NumberType]
	spawn: Callable[[StructurePowerSpawn], NumberType]
	upgrade: Callable[[NumberType], NumberType]
	usePower: Callable[[NumberType, Optional[RoomObject]], NumberType]

#resume at
#https://docs.screeps.com/api/#Resource

__all__ = ["Game", "InterShardMemory", "Memory", "PathFinder"]
