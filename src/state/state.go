package state

import (
	"sync"
	//"fmt"
	//"code.google.com/p/leveldb-go/leveldb"
	//"encoding/binary"
)

type Operation uint8

const (
	NONE Operation = iota
	PUT
	GET
	DELETE
	RLOCK
	WLOCK
)

type Value int64

const NIL Value = 0

type Key int64

type Command struct {
	Op  Operation
	K   Key
	V   Value
	K1  Key
	V1  Value
	K2  Key
	V2  Value
	K3  Key
	V3  Value
	K4  Key
	V4  Value
	K5  Key
	V5  Value
	K6  Key
	V6  Value
	K7  Key
	V7  Value
	K8  Key
	V8  Value
	K9  Key
	V9  Value
	K10 Key
	V10 Value
	K11 Key
	V11 Value
	K12 Key
	V12 Value
	K13 Key
	V13 Value
	K14 Key
	V14 Value
	K15 Key
	V15 Value
}

type State struct {
	mutex *sync.Mutex
	Store map[Key]Value
	//DB *leveldb.DB
}

func InitState() *State {
	/*
	   d, err := leveldb.Open("/Users/iulian/git/epaxos-batching/dpaxos/bin/db", nil)

	   if err != nil {
	       fmt.Printf("Leveldb open failed: %v\n", err)
	   }

	   return &State{d}
	*/

	return &State{new(sync.Mutex), make(map[Key]Value)}
}

func Conflict(gamma *Command, delta *Command) bool {
	if gamma.K == delta.K {
		if gamma.Op == PUT || delta.Op == PUT {
			return true
		}
	}
	return false
}

func ConflictBatch(batch1 []Command, batch2 []Command) bool {
	for i := 0; i < len(batch1); i++ {
		for j := 0; j < len(batch2); j++ {
			if Conflict(&batch1[i], &batch2[j]) {
				return true
			}
		}
	}
	return false
}

func IsRead(command *Command) bool {
	return command.Op == GET
}

func (c *Command) Execute(st *State) Value {
	//fmt.Printf("Executing (%d, %d)\n", c.K, c.V)

	//var key, value [8]byte

	//    st.mutex.Lock()
	//    defer st.mutex.Unlock()

	switch c.Op {
	case PUT:
		/*
		   binary.LittleEndian.PutUint64(key[:], uint64(c.K))
		   binary.LittleEndian.PutUint64(value[:], uint64(c.V))
		   st.DB.Set(key[:], value[:], nil)
		*/

		st.Store[c.K] = c.V
		st.Store[c.K1] = c.V1
		st.Store[c.K2] = c.V2
		st.Store[c.K3] = c.V3
		st.Store[c.K4] = c.V4
		st.Store[c.K5] = c.V5
		st.Store[c.K6] = c.V6
		st.Store[c.K7] = c.V7
		st.Store[c.K8] = c.V8
		st.Store[c.K9] = c.V9
		st.Store[c.K10] = c.V10
		st.Store[c.K11] = c.V11
		st.Store[c.K12] = c.V12
		st.Store[c.K13] = c.V13
		st.Store[c.K14] = c.V14
		st.Store[c.K15] = c.V15
		return c.V

	case GET:
		if val, present := st.Store[c.K]; present {
			return val
		}
	}

	return NIL
}
