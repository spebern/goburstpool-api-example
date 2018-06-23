import grpc
import api_pb2
import api_pb2_grpc

channel = grpc.insecure_channel('0-100-pool.burst.cryptoguru.org:8008')
stub = api_pb2_grpc.ApiStub(channel)

pool_stats = stub.GetPoolStatsInfo(api_pb2.Void())
print(pool_stats)

block_info = stub.GetBlockInfo(api_pb2.Void())
print(block_info)

channel = grpc.insecure_channel('100-0-pool.burst.cryptoguru.org:8008')
stub = api_pb2_grpc.ApiStub(channel)

pool_stats = stub.GetPoolStatsInfo(api_pb2.Void())
print(pool_stats)

block_info = stub.GetBlockInfo(api_pb2.Void())
print(block_info)

channel = grpc.insecure_channel('50-50-pool.burst.cryptoguru.org:8008')
stub = api_pb2_grpc.ApiStub(channel)

pool_stats = stub.GetPoolStatsInfo(api_pb2.Void())
print(pool_stats)

block_info = stub.GetBlockInfo(api_pb2.Void())
print(block_info)

# miner = stub.GetMinerInfo(api_pb2.MinerRequest(ID=10282355196851764065))
# print(miner)

# pool_cfg_info = stub.GetPoolConfigInfo(api_pb2.Void())
# print(pool_cfg_info )
