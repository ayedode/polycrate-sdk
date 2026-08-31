from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1s3_clusters_partial_update_active_error_component import (
        ApiV1S3ClustersPartialUpdateActiveErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_actual_availability_error_component import (
        ApiV1S3ClustersPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_admin_endpoint_error_component import (
        ApiV1S3ClustersPartialUpdateAdminEndpointErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_admin_endpoint_secure_error_component import (
        ApiV1S3ClustersPartialUpdateAdminEndpointSecureErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_alias_error_component import (
        ApiV1S3ClustersPartialUpdateAliasErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_allow_new_buckets_error_component import (
        ApiV1S3ClustersPartialUpdateAllowNewBucketsErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_annotations_error_component import (
        ApiV1S3ClustersPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_archived_at_error_component import (
        ApiV1S3ClustersPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_archived_by_error_component import (
        ApiV1S3ClustersPartialUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_archived_error_component import (
        ApiV1S3ClustersPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_archived_reason_error_component import (
        ApiV1S3ClustersPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_ceph_osd_cluster_total_bytes_error_component import (
        ApiV1S3ClustersPartialUpdateCephOsdClusterTotalBytesErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_cluster_config_error_component import (
        ApiV1S3ClustersPartialUpdateClusterConfigErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_cluster_info_error_component import (
        ApiV1S3ClustersPartialUpdateClusterInfoErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_created_by_component_error_component import (
        ApiV1S3ClustersPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_created_by_user_error_component import (
        ApiV1S3ClustersPartialUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_credential_error_component import (
        ApiV1S3ClustersPartialUpdateCredentialErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_criticality_error_component import (
        ApiV1S3ClustersPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_debug_mode_error_component import (
        ApiV1S3ClustersPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_default_product_error_component import (
        ApiV1S3ClustersPartialUpdateDefaultProductErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_description_error_component import (
        ApiV1S3ClustersPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_discovery_enabled_error_component import (
        ApiV1S3ClustersPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_display_name_error_component import (
        ApiV1S3ClustersPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_endpoint_error_component import (
        ApiV1S3ClustersPartialUpdateEndpointErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_endpoint_secure_error_component import (
        ApiV1S3ClustersPartialUpdateEndpointSecureErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_include_in_cost_statement_error_component import (
        ApiV1S3ClustersPartialUpdateIncludeInCostStatementErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_k8s_cluster_error_component import (
        ApiV1S3ClustersPartialUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_kind_error_component import (
        ApiV1S3ClustersPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_labels_error_component import (
        ApiV1S3ClustersPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1S3ClustersPartialUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_managed_buckets_object_count_error_component import (
        ApiV1S3ClustersPartialUpdateManagedBucketsObjectCountErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_managed_buckets_usage_kb_error_component import (
        ApiV1S3ClustersPartialUpdateManagedBucketsUsageKbErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_managed_by_content_type_error_component import (
        ApiV1S3ClustersPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_managed_by_object_id_error_component import (
        ApiV1S3ClustersPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_minio_cluster_capacity_usable_bytes_error_component import (
        ApiV1S3ClustersPartialUpdateMinioClusterCapacityUsableBytesErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_minio_cluster_usage_bytes_error_component import (
        ApiV1S3ClustersPartialUpdateMinioClusterUsageBytesErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_modified_by_user_error_component import (
        ApiV1S3ClustersPartialUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_name_error_component import (
        ApiV1S3ClustersPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_namespace_error_component import (
        ApiV1S3ClustersPartialUpdateNamespaceErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_non_field_errors_error_component import (
        ApiV1S3ClustersPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_platform_dns_record_created_error_component import (
        ApiV1S3ClustersPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_platform_service_error_component import (
        ApiV1S3ClustersPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_provider_error_component import (
        ApiV1S3ClustersPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_provider_id_error_component import (
        ApiV1S3ClustersPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_provider_reference_error_component import (
        ApiV1S3ClustersPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_radosgw_buckets_logical_used_bytes_error_component import (
        ApiV1S3ClustersPartialUpdateRadosgwBucketsLogicalUsedBytesErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_reconciliation_enabled_error_component import (
        ApiV1S3ClustersPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_region_error_component import (
        ApiV1S3ClustersPartialUpdateRegionErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_scope_error_component import (
        ApiV1S3ClustersPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_sla_availability_error_component import (
        ApiV1S3ClustersPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_sla_target_error_component import (
        ApiV1S3ClustersPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_sla_window_days_error_component import (
        ApiV1S3ClustersPartialUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_slo_availability_error_component import (
        ApiV1S3ClustersPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_slo_target_error_component import (
        ApiV1S3ClustersPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_slo_window_days_error_component import (
        ApiV1S3ClustersPartialUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_slug_error_component import (
        ApiV1S3ClustersPartialUpdateSlugErrorComponent,
    )
    from ..models.api_v1s3_clusters_partial_update_target_availability_error_component import (
        ApiV1S3ClustersPartialUpdateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1S3ClustersPartialUpdateValidationError")


@_attrs_define
class ApiV1S3ClustersPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1S3ClustersPartialUpdateActiveErrorComponent |
            ApiV1S3ClustersPartialUpdateActualAvailabilityErrorComponent |
            ApiV1S3ClustersPartialUpdateAdminEndpointErrorComponent |
            ApiV1S3ClustersPartialUpdateAdminEndpointSecureErrorComponent | ApiV1S3ClustersPartialUpdateAliasErrorComponent
            | ApiV1S3ClustersPartialUpdateAllowNewBucketsErrorComponent |
            ApiV1S3ClustersPartialUpdateAnnotationsErrorComponent | ApiV1S3ClustersPartialUpdateArchivedAtErrorComponent |
            ApiV1S3ClustersPartialUpdateArchivedByErrorComponent | ApiV1S3ClustersPartialUpdateArchivedErrorComponent |
            ApiV1S3ClustersPartialUpdateArchivedReasonErrorComponent |
            ApiV1S3ClustersPartialUpdateCephOsdClusterTotalBytesErrorComponent |
            ApiV1S3ClustersPartialUpdateClusterConfigErrorComponent | ApiV1S3ClustersPartialUpdateClusterInfoErrorComponent
            | ApiV1S3ClustersPartialUpdateCreatedByComponentErrorComponent |
            ApiV1S3ClustersPartialUpdateCreatedByUserErrorComponent | ApiV1S3ClustersPartialUpdateCredentialErrorComponent |
            ApiV1S3ClustersPartialUpdateCriticalityErrorComponent | ApiV1S3ClustersPartialUpdateDebugModeErrorComponent |
            ApiV1S3ClustersPartialUpdateDefaultProductErrorComponent | ApiV1S3ClustersPartialUpdateDescriptionErrorComponent
            | ApiV1S3ClustersPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1S3ClustersPartialUpdateDisplayNameErrorComponent | ApiV1S3ClustersPartialUpdateEndpointErrorComponent |
            ApiV1S3ClustersPartialUpdateEndpointSecureErrorComponent |
            ApiV1S3ClustersPartialUpdateIncludeInCostStatementErrorComponent |
            ApiV1S3ClustersPartialUpdateK8SClusterErrorComponent | ApiV1S3ClustersPartialUpdateKindErrorComponent |
            ApiV1S3ClustersPartialUpdateLabelsErrorComponent |
            ApiV1S3ClustersPartialUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1S3ClustersPartialUpdateManagedBucketsObjectCountErrorComponent |
            ApiV1S3ClustersPartialUpdateManagedBucketsUsageKbErrorComponent |
            ApiV1S3ClustersPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1S3ClustersPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1S3ClustersPartialUpdateMinioClusterCapacityUsableBytesErrorComponent |
            ApiV1S3ClustersPartialUpdateMinioClusterUsageBytesErrorComponent |
            ApiV1S3ClustersPartialUpdateModifiedByUserErrorComponent | ApiV1S3ClustersPartialUpdateNameErrorComponent |
            ApiV1S3ClustersPartialUpdateNamespaceErrorComponent | ApiV1S3ClustersPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1S3ClustersPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1S3ClustersPartialUpdatePlatformServiceErrorComponent | ApiV1S3ClustersPartialUpdateProviderErrorComponent |
            ApiV1S3ClustersPartialUpdateProviderIdErrorComponent |
            ApiV1S3ClustersPartialUpdateProviderReferenceErrorComponent |
            ApiV1S3ClustersPartialUpdateRadosgwBucketsLogicalUsedBytesErrorComponent |
            ApiV1S3ClustersPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1S3ClustersPartialUpdateRegionErrorComponent | ApiV1S3ClustersPartialUpdateScopeErrorComponent |
            ApiV1S3ClustersPartialUpdateSlaAvailabilityErrorComponent | ApiV1S3ClustersPartialUpdateSlaTargetErrorComponent
            | ApiV1S3ClustersPartialUpdateSlaWindowDaysErrorComponent |
            ApiV1S3ClustersPartialUpdateSloAvailabilityErrorComponent | ApiV1S3ClustersPartialUpdateSloTargetErrorComponent
            | ApiV1S3ClustersPartialUpdateSloWindowDaysErrorComponent | ApiV1S3ClustersPartialUpdateSlugErrorComponent |
            ApiV1S3ClustersPartialUpdateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1S3ClustersPartialUpdateActiveErrorComponent
        | ApiV1S3ClustersPartialUpdateActualAvailabilityErrorComponent
        | ApiV1S3ClustersPartialUpdateAdminEndpointErrorComponent
        | ApiV1S3ClustersPartialUpdateAdminEndpointSecureErrorComponent
        | ApiV1S3ClustersPartialUpdateAliasErrorComponent
        | ApiV1S3ClustersPartialUpdateAllowNewBucketsErrorComponent
        | ApiV1S3ClustersPartialUpdateAnnotationsErrorComponent
        | ApiV1S3ClustersPartialUpdateArchivedAtErrorComponent
        | ApiV1S3ClustersPartialUpdateArchivedByErrorComponent
        | ApiV1S3ClustersPartialUpdateArchivedErrorComponent
        | ApiV1S3ClustersPartialUpdateArchivedReasonErrorComponent
        | ApiV1S3ClustersPartialUpdateCephOsdClusterTotalBytesErrorComponent
        | ApiV1S3ClustersPartialUpdateClusterConfigErrorComponent
        | ApiV1S3ClustersPartialUpdateClusterInfoErrorComponent
        | ApiV1S3ClustersPartialUpdateCreatedByComponentErrorComponent
        | ApiV1S3ClustersPartialUpdateCreatedByUserErrorComponent
        | ApiV1S3ClustersPartialUpdateCredentialErrorComponent
        | ApiV1S3ClustersPartialUpdateCriticalityErrorComponent
        | ApiV1S3ClustersPartialUpdateDebugModeErrorComponent
        | ApiV1S3ClustersPartialUpdateDefaultProductErrorComponent
        | ApiV1S3ClustersPartialUpdateDescriptionErrorComponent
        | ApiV1S3ClustersPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1S3ClustersPartialUpdateDisplayNameErrorComponent
        | ApiV1S3ClustersPartialUpdateEndpointErrorComponent
        | ApiV1S3ClustersPartialUpdateEndpointSecureErrorComponent
        | ApiV1S3ClustersPartialUpdateIncludeInCostStatementErrorComponent
        | ApiV1S3ClustersPartialUpdateK8SClusterErrorComponent
        | ApiV1S3ClustersPartialUpdateKindErrorComponent
        | ApiV1S3ClustersPartialUpdateLabelsErrorComponent
        | ApiV1S3ClustersPartialUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1S3ClustersPartialUpdateManagedBucketsObjectCountErrorComponent
        | ApiV1S3ClustersPartialUpdateManagedBucketsUsageKbErrorComponent
        | ApiV1S3ClustersPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1S3ClustersPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1S3ClustersPartialUpdateMinioClusterCapacityUsableBytesErrorComponent
        | ApiV1S3ClustersPartialUpdateMinioClusterUsageBytesErrorComponent
        | ApiV1S3ClustersPartialUpdateModifiedByUserErrorComponent
        | ApiV1S3ClustersPartialUpdateNameErrorComponent
        | ApiV1S3ClustersPartialUpdateNamespaceErrorComponent
        | ApiV1S3ClustersPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1S3ClustersPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1S3ClustersPartialUpdatePlatformServiceErrorComponent
        | ApiV1S3ClustersPartialUpdateProviderErrorComponent
        | ApiV1S3ClustersPartialUpdateProviderIdErrorComponent
        | ApiV1S3ClustersPartialUpdateProviderReferenceErrorComponent
        | ApiV1S3ClustersPartialUpdateRadosgwBucketsLogicalUsedBytesErrorComponent
        | ApiV1S3ClustersPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1S3ClustersPartialUpdateRegionErrorComponent
        | ApiV1S3ClustersPartialUpdateScopeErrorComponent
        | ApiV1S3ClustersPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1S3ClustersPartialUpdateSlaTargetErrorComponent
        | ApiV1S3ClustersPartialUpdateSlaWindowDaysErrorComponent
        | ApiV1S3ClustersPartialUpdateSloAvailabilityErrorComponent
        | ApiV1S3ClustersPartialUpdateSloTargetErrorComponent
        | ApiV1S3ClustersPartialUpdateSloWindowDaysErrorComponent
        | ApiV1S3ClustersPartialUpdateSlugErrorComponent
        | ApiV1S3ClustersPartialUpdateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1s3_clusters_partial_update_active_error_component import (
            ApiV1S3ClustersPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_actual_availability_error_component import (
            ApiV1S3ClustersPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_admin_endpoint_error_component import (
            ApiV1S3ClustersPartialUpdateAdminEndpointErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_admin_endpoint_secure_error_component import (
            ApiV1S3ClustersPartialUpdateAdminEndpointSecureErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_alias_error_component import (
            ApiV1S3ClustersPartialUpdateAliasErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_allow_new_buckets_error_component import (
            ApiV1S3ClustersPartialUpdateAllowNewBucketsErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_annotations_error_component import (
            ApiV1S3ClustersPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_archived_at_error_component import (
            ApiV1S3ClustersPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_archived_by_error_component import (
            ApiV1S3ClustersPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_archived_error_component import (
            ApiV1S3ClustersPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_archived_reason_error_component import (
            ApiV1S3ClustersPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_ceph_osd_cluster_total_bytes_error_component import (
            ApiV1S3ClustersPartialUpdateCephOsdClusterTotalBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_cluster_config_error_component import (
            ApiV1S3ClustersPartialUpdateClusterConfigErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_cluster_info_error_component import (
            ApiV1S3ClustersPartialUpdateClusterInfoErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_created_by_component_error_component import (
            ApiV1S3ClustersPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_created_by_user_error_component import (
            ApiV1S3ClustersPartialUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_credential_error_component import (
            ApiV1S3ClustersPartialUpdateCredentialErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_criticality_error_component import (
            ApiV1S3ClustersPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_debug_mode_error_component import (
            ApiV1S3ClustersPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_description_error_component import (
            ApiV1S3ClustersPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_discovery_enabled_error_component import (
            ApiV1S3ClustersPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_display_name_error_component import (
            ApiV1S3ClustersPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_endpoint_error_component import (
            ApiV1S3ClustersPartialUpdateEndpointErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_endpoint_secure_error_component import (
            ApiV1S3ClustersPartialUpdateEndpointSecureErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_include_in_cost_statement_error_component import (
            ApiV1S3ClustersPartialUpdateIncludeInCostStatementErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_k8s_cluster_error_component import (
            ApiV1S3ClustersPartialUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_kind_error_component import (
            ApiV1S3ClustersPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_labels_error_component import (
            ApiV1S3ClustersPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1S3ClustersPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_managed_buckets_object_count_error_component import (
            ApiV1S3ClustersPartialUpdateManagedBucketsObjectCountErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_managed_buckets_usage_kb_error_component import (
            ApiV1S3ClustersPartialUpdateManagedBucketsUsageKbErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_managed_by_content_type_error_component import (
            ApiV1S3ClustersPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_managed_by_object_id_error_component import (
            ApiV1S3ClustersPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_minio_cluster_capacity_usable_bytes_error_component import (
            ApiV1S3ClustersPartialUpdateMinioClusterCapacityUsableBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_minio_cluster_usage_bytes_error_component import (
            ApiV1S3ClustersPartialUpdateMinioClusterUsageBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_modified_by_user_error_component import (
            ApiV1S3ClustersPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_name_error_component import (
            ApiV1S3ClustersPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_namespace_error_component import (
            ApiV1S3ClustersPartialUpdateNamespaceErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_non_field_errors_error_component import (
            ApiV1S3ClustersPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_platform_dns_record_created_error_component import (
            ApiV1S3ClustersPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_platform_service_error_component import (
            ApiV1S3ClustersPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_provider_error_component import (
            ApiV1S3ClustersPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_provider_id_error_component import (
            ApiV1S3ClustersPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_provider_reference_error_component import (
            ApiV1S3ClustersPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_radosgw_buckets_logical_used_bytes_error_component import (
            ApiV1S3ClustersPartialUpdateRadosgwBucketsLogicalUsedBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_reconciliation_enabled_error_component import (
            ApiV1S3ClustersPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_region_error_component import (
            ApiV1S3ClustersPartialUpdateRegionErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_scope_error_component import (
            ApiV1S3ClustersPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_sla_availability_error_component import (
            ApiV1S3ClustersPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_sla_target_error_component import (
            ApiV1S3ClustersPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_sla_window_days_error_component import (
            ApiV1S3ClustersPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_slo_availability_error_component import (
            ApiV1S3ClustersPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_slo_target_error_component import (
            ApiV1S3ClustersPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_slo_window_days_error_component import (
            ApiV1S3ClustersPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_slug_error_component import (
            ApiV1S3ClustersPartialUpdateSlugErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_target_availability_error_component import (
            ApiV1S3ClustersPartialUpdateTargetAvailabilityErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1S3ClustersPartialUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateEndpointSecureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateAdminEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateAdminEndpointSecureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateClusterConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateClusterInfoErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateAllowNewBucketsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateIncludeInCostStatementErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateCephOsdClusterTotalBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateRadosgwBucketsLogicalUsedBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1S3ClustersPartialUpdateMinioClusterCapacityUsableBytesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateMinioClusterUsageBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateManagedBucketsUsageKbErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateManagedBucketsObjectCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersPartialUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1s3_clusters_partial_update_active_error_component import (
            ApiV1S3ClustersPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_actual_availability_error_component import (
            ApiV1S3ClustersPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_admin_endpoint_error_component import (
            ApiV1S3ClustersPartialUpdateAdminEndpointErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_admin_endpoint_secure_error_component import (
            ApiV1S3ClustersPartialUpdateAdminEndpointSecureErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_alias_error_component import (
            ApiV1S3ClustersPartialUpdateAliasErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_allow_new_buckets_error_component import (
            ApiV1S3ClustersPartialUpdateAllowNewBucketsErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_annotations_error_component import (
            ApiV1S3ClustersPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_archived_at_error_component import (
            ApiV1S3ClustersPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_archived_by_error_component import (
            ApiV1S3ClustersPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_archived_error_component import (
            ApiV1S3ClustersPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_archived_reason_error_component import (
            ApiV1S3ClustersPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_ceph_osd_cluster_total_bytes_error_component import (
            ApiV1S3ClustersPartialUpdateCephOsdClusterTotalBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_cluster_config_error_component import (
            ApiV1S3ClustersPartialUpdateClusterConfigErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_cluster_info_error_component import (
            ApiV1S3ClustersPartialUpdateClusterInfoErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_created_by_component_error_component import (
            ApiV1S3ClustersPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_created_by_user_error_component import (
            ApiV1S3ClustersPartialUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_credential_error_component import (
            ApiV1S3ClustersPartialUpdateCredentialErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_criticality_error_component import (
            ApiV1S3ClustersPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_debug_mode_error_component import (
            ApiV1S3ClustersPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_default_product_error_component import (
            ApiV1S3ClustersPartialUpdateDefaultProductErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_description_error_component import (
            ApiV1S3ClustersPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_discovery_enabled_error_component import (
            ApiV1S3ClustersPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_display_name_error_component import (
            ApiV1S3ClustersPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_endpoint_error_component import (
            ApiV1S3ClustersPartialUpdateEndpointErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_endpoint_secure_error_component import (
            ApiV1S3ClustersPartialUpdateEndpointSecureErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_include_in_cost_statement_error_component import (
            ApiV1S3ClustersPartialUpdateIncludeInCostStatementErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_k8s_cluster_error_component import (
            ApiV1S3ClustersPartialUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_kind_error_component import (
            ApiV1S3ClustersPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_labels_error_component import (
            ApiV1S3ClustersPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1S3ClustersPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_managed_buckets_object_count_error_component import (
            ApiV1S3ClustersPartialUpdateManagedBucketsObjectCountErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_managed_buckets_usage_kb_error_component import (
            ApiV1S3ClustersPartialUpdateManagedBucketsUsageKbErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_managed_by_content_type_error_component import (
            ApiV1S3ClustersPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_managed_by_object_id_error_component import (
            ApiV1S3ClustersPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_minio_cluster_capacity_usable_bytes_error_component import (
            ApiV1S3ClustersPartialUpdateMinioClusterCapacityUsableBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_minio_cluster_usage_bytes_error_component import (
            ApiV1S3ClustersPartialUpdateMinioClusterUsageBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_modified_by_user_error_component import (
            ApiV1S3ClustersPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_name_error_component import (
            ApiV1S3ClustersPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_namespace_error_component import (
            ApiV1S3ClustersPartialUpdateNamespaceErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_non_field_errors_error_component import (
            ApiV1S3ClustersPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_platform_dns_record_created_error_component import (
            ApiV1S3ClustersPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_platform_service_error_component import (
            ApiV1S3ClustersPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_provider_error_component import (
            ApiV1S3ClustersPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_provider_id_error_component import (
            ApiV1S3ClustersPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_provider_reference_error_component import (
            ApiV1S3ClustersPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_radosgw_buckets_logical_used_bytes_error_component import (
            ApiV1S3ClustersPartialUpdateRadosgwBucketsLogicalUsedBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_reconciliation_enabled_error_component import (
            ApiV1S3ClustersPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_region_error_component import (
            ApiV1S3ClustersPartialUpdateRegionErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_scope_error_component import (
            ApiV1S3ClustersPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_sla_availability_error_component import (
            ApiV1S3ClustersPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_sla_target_error_component import (
            ApiV1S3ClustersPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_sla_window_days_error_component import (
            ApiV1S3ClustersPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_slo_availability_error_component import (
            ApiV1S3ClustersPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_slo_target_error_component import (
            ApiV1S3ClustersPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_slo_window_days_error_component import (
            ApiV1S3ClustersPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_slug_error_component import (
            ApiV1S3ClustersPartialUpdateSlugErrorComponent,
        )
        from ..models.api_v1s3_clusters_partial_update_target_availability_error_component import (
            ApiV1S3ClustersPartialUpdateTargetAvailabilityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1S3ClustersPartialUpdateActiveErrorComponent
                | ApiV1S3ClustersPartialUpdateActualAvailabilityErrorComponent
                | ApiV1S3ClustersPartialUpdateAdminEndpointErrorComponent
                | ApiV1S3ClustersPartialUpdateAdminEndpointSecureErrorComponent
                | ApiV1S3ClustersPartialUpdateAliasErrorComponent
                | ApiV1S3ClustersPartialUpdateAllowNewBucketsErrorComponent
                | ApiV1S3ClustersPartialUpdateAnnotationsErrorComponent
                | ApiV1S3ClustersPartialUpdateArchivedAtErrorComponent
                | ApiV1S3ClustersPartialUpdateArchivedByErrorComponent
                | ApiV1S3ClustersPartialUpdateArchivedErrorComponent
                | ApiV1S3ClustersPartialUpdateArchivedReasonErrorComponent
                | ApiV1S3ClustersPartialUpdateCephOsdClusterTotalBytesErrorComponent
                | ApiV1S3ClustersPartialUpdateClusterConfigErrorComponent
                | ApiV1S3ClustersPartialUpdateClusterInfoErrorComponent
                | ApiV1S3ClustersPartialUpdateCreatedByComponentErrorComponent
                | ApiV1S3ClustersPartialUpdateCreatedByUserErrorComponent
                | ApiV1S3ClustersPartialUpdateCredentialErrorComponent
                | ApiV1S3ClustersPartialUpdateCriticalityErrorComponent
                | ApiV1S3ClustersPartialUpdateDebugModeErrorComponent
                | ApiV1S3ClustersPartialUpdateDefaultProductErrorComponent
                | ApiV1S3ClustersPartialUpdateDescriptionErrorComponent
                | ApiV1S3ClustersPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1S3ClustersPartialUpdateDisplayNameErrorComponent
                | ApiV1S3ClustersPartialUpdateEndpointErrorComponent
                | ApiV1S3ClustersPartialUpdateEndpointSecureErrorComponent
                | ApiV1S3ClustersPartialUpdateIncludeInCostStatementErrorComponent
                | ApiV1S3ClustersPartialUpdateK8SClusterErrorComponent
                | ApiV1S3ClustersPartialUpdateKindErrorComponent
                | ApiV1S3ClustersPartialUpdateLabelsErrorComponent
                | ApiV1S3ClustersPartialUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1S3ClustersPartialUpdateManagedBucketsObjectCountErrorComponent
                | ApiV1S3ClustersPartialUpdateManagedBucketsUsageKbErrorComponent
                | ApiV1S3ClustersPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1S3ClustersPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1S3ClustersPartialUpdateMinioClusterCapacityUsableBytesErrorComponent
                | ApiV1S3ClustersPartialUpdateMinioClusterUsageBytesErrorComponent
                | ApiV1S3ClustersPartialUpdateModifiedByUserErrorComponent
                | ApiV1S3ClustersPartialUpdateNameErrorComponent
                | ApiV1S3ClustersPartialUpdateNamespaceErrorComponent
                | ApiV1S3ClustersPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1S3ClustersPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1S3ClustersPartialUpdatePlatformServiceErrorComponent
                | ApiV1S3ClustersPartialUpdateProviderErrorComponent
                | ApiV1S3ClustersPartialUpdateProviderIdErrorComponent
                | ApiV1S3ClustersPartialUpdateProviderReferenceErrorComponent
                | ApiV1S3ClustersPartialUpdateRadosgwBucketsLogicalUsedBytesErrorComponent
                | ApiV1S3ClustersPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1S3ClustersPartialUpdateRegionErrorComponent
                | ApiV1S3ClustersPartialUpdateScopeErrorComponent
                | ApiV1S3ClustersPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1S3ClustersPartialUpdateSlaTargetErrorComponent
                | ApiV1S3ClustersPartialUpdateSlaWindowDaysErrorComponent
                | ApiV1S3ClustersPartialUpdateSloAvailabilityErrorComponent
                | ApiV1S3ClustersPartialUpdateSloTargetErrorComponent
                | ApiV1S3ClustersPartialUpdateSloWindowDaysErrorComponent
                | ApiV1S3ClustersPartialUpdateSlugErrorComponent
                | ApiV1S3ClustersPartialUpdateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_0 = (
                        ApiV1S3ClustersPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_1 = (
                        ApiV1S3ClustersPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_2 = (
                        ApiV1S3ClustersPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_3 = (
                        ApiV1S3ClustersPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_4 = (
                        ApiV1S3ClustersPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_5 = (
                        ApiV1S3ClustersPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_6 = (
                        ApiV1S3ClustersPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_7 = (
                        ApiV1S3ClustersPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_8 = (
                        ApiV1S3ClustersPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_9 = (
                        ApiV1S3ClustersPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_10 = (
                        ApiV1S3ClustersPartialUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_11 = (
                        ApiV1S3ClustersPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_12 = (
                        ApiV1S3ClustersPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_13 = (
                        ApiV1S3ClustersPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_14 = (
                        ApiV1S3ClustersPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_15 = (
                        ApiV1S3ClustersPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_16 = (
                        ApiV1S3ClustersPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_17 = (
                        ApiV1S3ClustersPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_18 = (
                        ApiV1S3ClustersPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_19 = (
                        ApiV1S3ClustersPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_20 = (
                        ApiV1S3ClustersPartialUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_21 = (
                        ApiV1S3ClustersPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_22 = (
                        ApiV1S3ClustersPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_23 = (
                        ApiV1S3ClustersPartialUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_24 = (
                        ApiV1S3ClustersPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_25 = (
                        ApiV1S3ClustersPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_26 = (
                        ApiV1S3ClustersPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_27 = (
                        ApiV1S3ClustersPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_28 = (
                        ApiV1S3ClustersPartialUpdateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_29 = (
                        ApiV1S3ClustersPartialUpdateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_30 = (
                        ApiV1S3ClustersPartialUpdateEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_31 = (
                        ApiV1S3ClustersPartialUpdateEndpointSecureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_32 = (
                        ApiV1S3ClustersPartialUpdateAdminEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_33 = (
                        ApiV1S3ClustersPartialUpdateAdminEndpointSecureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_34 = (
                        ApiV1S3ClustersPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_35 = (
                        ApiV1S3ClustersPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_36 = (
                        ApiV1S3ClustersPartialUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_37 = (
                        ApiV1S3ClustersPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_38 = (
                        ApiV1S3ClustersPartialUpdateClusterConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_39 = (
                        ApiV1S3ClustersPartialUpdateClusterInfoErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_40 = (
                        ApiV1S3ClustersPartialUpdateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_41 = (
                        ApiV1S3ClustersPartialUpdateRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_42 = (
                        ApiV1S3ClustersPartialUpdateAllowNewBucketsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_43 = (
                        ApiV1S3ClustersPartialUpdateIncludeInCostStatementErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_44 = (
                        ApiV1S3ClustersPartialUpdateCephOsdClusterTotalBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_45 = (
                        ApiV1S3ClustersPartialUpdateRadosgwBucketsLogicalUsedBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_46 = (
                        ApiV1S3ClustersPartialUpdateMinioClusterCapacityUsableBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_47 = (
                        ApiV1S3ClustersPartialUpdateMinioClusterUsageBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_48 = (
                        ApiV1S3ClustersPartialUpdateManagedBucketsUsageKbErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_49 = (
                        ApiV1S3ClustersPartialUpdateManagedBucketsObjectCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_50 = (
                        ApiV1S3ClustersPartialUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_51 = (
                        ApiV1S3ClustersPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_52 = (
                        ApiV1S3ClustersPartialUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_53 = (
                        ApiV1S3ClustersPartialUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_54 = (
                        ApiV1S3ClustersPartialUpdateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_partial_update_error_type_55 = (
                        ApiV1S3ClustersPartialUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_partial_update_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1s3_clusters_partial_update_error_type_56 = (
                    ApiV1S3ClustersPartialUpdateDefaultProductErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1s3_clusters_partial_update_error_type_56

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1s3_clusters_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1s3_clusters_partial_update_validation_error.additional_properties = d
        return api_v1s3_clusters_partial_update_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
