# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.bigtable.admin.v2 import bigtable_table_admin_pb2 as google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2
from google.bigtable.admin.v2 import table_pb2 as google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class BigtableTableAdminStub(object):
  """Service for creating, configuring, and deleting Cloud Bigtable tables.


  Provides access to the table schemas only, not the data stored within
  the tables.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateTable = channel.unary_unary(
        '/google.bigtable.admin.v2.BigtableTableAdmin/CreateTable',
        request_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.CreateTableRequest.SerializeToString,
        response_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2.Table.FromString,
        )
    self.CreateTableFromSnapshot = channel.unary_unary(
        '/google.bigtable.admin.v2.BigtableTableAdmin/CreateTableFromSnapshot',
        request_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.CreateTableFromSnapshotRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.ListTables = channel.unary_unary(
        '/google.bigtable.admin.v2.BigtableTableAdmin/ListTables',
        request_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.ListTablesRequest.SerializeToString,
        response_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.ListTablesResponse.FromString,
        )
    self.GetTable = channel.unary_unary(
        '/google.bigtable.admin.v2.BigtableTableAdmin/GetTable',
        request_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.GetTableRequest.SerializeToString,
        response_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2.Table.FromString,
        )
    self.DeleteTable = channel.unary_unary(
        '/google.bigtable.admin.v2.BigtableTableAdmin/DeleteTable',
        request_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.DeleteTableRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ModifyColumnFamilies = channel.unary_unary(
        '/google.bigtable.admin.v2.BigtableTableAdmin/ModifyColumnFamilies',
        request_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.ModifyColumnFamiliesRequest.SerializeToString,
        response_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2.Table.FromString,
        )
    self.DropRowRange = channel.unary_unary(
        '/google.bigtable.admin.v2.BigtableTableAdmin/DropRowRange',
        request_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.DropRowRangeRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GenerateConsistencyToken = channel.unary_unary(
        '/google.bigtable.admin.v2.BigtableTableAdmin/GenerateConsistencyToken',
        request_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.GenerateConsistencyTokenRequest.SerializeToString,
        response_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.GenerateConsistencyTokenResponse.FromString,
        )
    self.CheckConsistency = channel.unary_unary(
        '/google.bigtable.admin.v2.BigtableTableAdmin/CheckConsistency',
        request_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.CheckConsistencyRequest.SerializeToString,
        response_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.CheckConsistencyResponse.FromString,
        )
    self.SnapshotTable = channel.unary_unary(
        '/google.bigtable.admin.v2.BigtableTableAdmin/SnapshotTable',
        request_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.SnapshotTableRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.GetSnapshot = channel.unary_unary(
        '/google.bigtable.admin.v2.BigtableTableAdmin/GetSnapshot',
        request_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.GetSnapshotRequest.SerializeToString,
        response_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2.Snapshot.FromString,
        )
    self.ListSnapshots = channel.unary_unary(
        '/google.bigtable.admin.v2.BigtableTableAdmin/ListSnapshots',
        request_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.ListSnapshotsRequest.SerializeToString,
        response_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.ListSnapshotsResponse.FromString,
        )
    self.DeleteSnapshot = channel.unary_unary(
        '/google.bigtable.admin.v2.BigtableTableAdmin/DeleteSnapshot',
        request_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.DeleteSnapshotRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class BigtableTableAdminServicer(object):
  """Service for creating, configuring, and deleting Cloud Bigtable tables.


  Provides access to the table schemas only, not the data stored within
  the tables.
  """

  def CreateTable(self, request, context):
    """Creates a new table in the specified instance.
    The table can be created with a full set of initial column families,
    specified in the request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateTableFromSnapshot(self, request, context):
    """Creates a new table from the specified snapshot. The target table must
    not exist. The snapshot and the table must be in the same instance.

    Note: This is a private alpha release of Cloud Bigtable snapshots. This
    feature is not currently available to most Cloud Bigtable customers. This
    feature might be changed in backward-incompatible ways and is not
    recommended for production use. It is not subject to any SLA or deprecation
    policy.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListTables(self, request, context):
    """Lists all tables served from a specified instance.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTable(self, request, context):
    """Gets metadata information about the specified table.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteTable(self, request, context):
    """Permanently deletes a specified table and all of its data.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModifyColumnFamilies(self, request, context):
    """Performs a series of column family modifications on the specified table.
    Either all or none of the modifications will occur before this method
    returns, but data requests received prior to that point may see a table
    where only some modifications have taken effect.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DropRowRange(self, request, context):
    """Permanently drop/delete a row range from a specified table. The request can
    specify whether to delete all rows in a table, or only those that match a
    particular prefix.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GenerateConsistencyToken(self, request, context):
    """Generates a consistency token for a Table, which can be used in
    CheckConsistency to check whether mutations to the table that finished
    before this call started have been replicated. The tokens will be available
    for 90 days.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckConsistency(self, request, context):
    """Checks replication consistency based on a consistency token, that is, if
    replication has caught up based on the conditions specified in the token
    and the check request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotTable(self, request, context):
    """Creates a new snapshot in the specified cluster from the specified
    source table. The cluster and the table must be in the same instance.

    Note: This is a private alpha release of Cloud Bigtable snapshots. This
    feature is not currently available to most Cloud Bigtable customers. This
    feature might be changed in backward-incompatible ways and is not
    recommended for production use. It is not subject to any SLA or deprecation
    policy.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSnapshot(self, request, context):
    """Gets metadata information about the specified snapshot.

    Note: This is a private alpha release of Cloud Bigtable snapshots. This
    feature is not currently available to most Cloud Bigtable customers. This
    feature might be changed in backward-incompatible ways and is not
    recommended for production use. It is not subject to any SLA or deprecation
    policy.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListSnapshots(self, request, context):
    """Lists all snapshots associated with the specified cluster.

    Note: This is a private alpha release of Cloud Bigtable snapshots. This
    feature is not currently available to most Cloud Bigtable customers. This
    feature might be changed in backward-incompatible ways and is not
    recommended for production use. It is not subject to any SLA or deprecation
    policy.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteSnapshot(self, request, context):
    """Permanently deletes the specified snapshot.

    Note: This is a private alpha release of Cloud Bigtable snapshots. This
    feature is not currently available to most Cloud Bigtable customers. This
    feature might be changed in backward-incompatible ways and is not
    recommended for production use. It is not subject to any SLA or deprecation
    policy.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BigtableTableAdminServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateTable': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTable,
          request_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.CreateTableRequest.FromString,
          response_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2.Table.SerializeToString,
      ),
      'CreateTableFromSnapshot': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTableFromSnapshot,
          request_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.CreateTableFromSnapshotRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'ListTables': grpc.unary_unary_rpc_method_handler(
          servicer.ListTables,
          request_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.ListTablesRequest.FromString,
          response_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.ListTablesResponse.SerializeToString,
      ),
      'GetTable': grpc.unary_unary_rpc_method_handler(
          servicer.GetTable,
          request_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.GetTableRequest.FromString,
          response_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2.Table.SerializeToString,
      ),
      'DeleteTable': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteTable,
          request_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.DeleteTableRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ModifyColumnFamilies': grpc.unary_unary_rpc_method_handler(
          servicer.ModifyColumnFamilies,
          request_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.ModifyColumnFamiliesRequest.FromString,
          response_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2.Table.SerializeToString,
      ),
      'DropRowRange': grpc.unary_unary_rpc_method_handler(
          servicer.DropRowRange,
          request_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.DropRowRangeRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GenerateConsistencyToken': grpc.unary_unary_rpc_method_handler(
          servicer.GenerateConsistencyToken,
          request_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.GenerateConsistencyTokenRequest.FromString,
          response_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.GenerateConsistencyTokenResponse.SerializeToString,
      ),
      'CheckConsistency': grpc.unary_unary_rpc_method_handler(
          servicer.CheckConsistency,
          request_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.CheckConsistencyRequest.FromString,
          response_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.CheckConsistencyResponse.SerializeToString,
      ),
      'SnapshotTable': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotTable,
          request_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.SnapshotTableRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'GetSnapshot': grpc.unary_unary_rpc_method_handler(
          servicer.GetSnapshot,
          request_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.GetSnapshotRequest.FromString,
          response_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_table__pb2.Snapshot.SerializeToString,
      ),
      'ListSnapshots': grpc.unary_unary_rpc_method_handler(
          servicer.ListSnapshots,
          request_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.ListSnapshotsRequest.FromString,
          response_serializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.ListSnapshotsResponse.SerializeToString,
      ),
      'DeleteSnapshot': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteSnapshot,
          request_deserializer=google_dot_bigtable_dot_admin_dot_v2_dot_bigtable__table__admin__pb2.DeleteSnapshotRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.bigtable.admin.v2.BigtableTableAdmin', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))