from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1s3_clusters_update_active_error_component import ApiV1S3ClustersUpdateActiveErrorComponent
    from ..models.api_v1s3_clusters_update_actual_availability_error_component import (
        ApiV1S3ClustersUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_admin_endpoint_error_component import (
        ApiV1S3ClustersUpdateAdminEndpointErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_admin_endpoint_secure_error_component import (
        ApiV1S3ClustersUpdateAdminEndpointSecureErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_alias_error_component import ApiV1S3ClustersUpdateAliasErrorComponent
    from ..models.api_v1s3_clusters_update_allow_new_buckets_error_component import (
        ApiV1S3ClustersUpdateAllowNewBucketsErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_annotations_error_component import (
        ApiV1S3ClustersUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_archived_at_error_component import (
        ApiV1S3ClustersUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_archived_by_error_component import (
        ApiV1S3ClustersUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_archived_error_component import ApiV1S3ClustersUpdateArchivedErrorComponent
    from ..models.api_v1s3_clusters_update_archived_reason_error_component import (
        ApiV1S3ClustersUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_ceph_osd_cluster_total_bytes_error_component import (
        ApiV1S3ClustersUpdateCephOsdClusterTotalBytesErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_cluster_config_error_component import (
        ApiV1S3ClustersUpdateClusterConfigErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_cluster_info_error_component import (
        ApiV1S3ClustersUpdateClusterInfoErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_created_by_component_error_component import (
        ApiV1S3ClustersUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_created_by_user_error_component import (
        ApiV1S3ClustersUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_credential_error_component import (
        ApiV1S3ClustersUpdateCredentialErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_criticality_error_component import (
        ApiV1S3ClustersUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_debug_mode_error_component import (
        ApiV1S3ClustersUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_default_product_error_component import (
        ApiV1S3ClustersUpdateDefaultProductErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_description_error_component import (
        ApiV1S3ClustersUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_discovery_enabled_error_component import (
        ApiV1S3ClustersUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_display_name_error_component import (
        ApiV1S3ClustersUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_endpoint_error_component import ApiV1S3ClustersUpdateEndpointErrorComponent
    from ..models.api_v1s3_clusters_update_endpoint_secure_error_component import (
        ApiV1S3ClustersUpdateEndpointSecureErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_include_in_cost_statement_error_component import (
        ApiV1S3ClustersUpdateIncludeInCostStatementErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_k8s_cluster_error_component import (
        ApiV1S3ClustersUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_kind_error_component import ApiV1S3ClustersUpdateKindErrorComponent
    from ..models.api_v1s3_clusters_update_labels_error_component import ApiV1S3ClustersUpdateLabelsErrorComponent
    from ..models.api_v1s3_clusters_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1S3ClustersUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_managed_buckets_object_count_error_component import (
        ApiV1S3ClustersUpdateManagedBucketsObjectCountErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_managed_buckets_usage_kb_error_component import (
        ApiV1S3ClustersUpdateManagedBucketsUsageKbErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_managed_by_content_type_error_component import (
        ApiV1S3ClustersUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_managed_by_object_id_error_component import (
        ApiV1S3ClustersUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_minio_cluster_capacity_usable_bytes_error_component import (
        ApiV1S3ClustersUpdateMinioClusterCapacityUsableBytesErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_minio_cluster_usage_bytes_error_component import (
        ApiV1S3ClustersUpdateMinioClusterUsageBytesErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_modified_by_user_error_component import (
        ApiV1S3ClustersUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_name_error_component import ApiV1S3ClustersUpdateNameErrorComponent
    from ..models.api_v1s3_clusters_update_namespace_error_component import ApiV1S3ClustersUpdateNamespaceErrorComponent
    from ..models.api_v1s3_clusters_update_non_field_errors_error_component import (
        ApiV1S3ClustersUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_platform_dns_record_created_error_component import (
        ApiV1S3ClustersUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_platform_service_error_component import (
        ApiV1S3ClustersUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_provider_error_component import ApiV1S3ClustersUpdateProviderErrorComponent
    from ..models.api_v1s3_clusters_update_provider_id_error_component import (
        ApiV1S3ClustersUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_provider_reference_error_component import (
        ApiV1S3ClustersUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_radosgw_buckets_logical_used_bytes_error_component import (
        ApiV1S3ClustersUpdateRadosgwBucketsLogicalUsedBytesErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_reconciliation_enabled_error_component import (
        ApiV1S3ClustersUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_region_error_component import ApiV1S3ClustersUpdateRegionErrorComponent
    from ..models.api_v1s3_clusters_update_scope_error_component import ApiV1S3ClustersUpdateScopeErrorComponent
    from ..models.api_v1s3_clusters_update_sla_availability_error_component import (
        ApiV1S3ClustersUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_sla_target_error_component import (
        ApiV1S3ClustersUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_sla_window_days_error_component import (
        ApiV1S3ClustersUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_slo_availability_error_component import (
        ApiV1S3ClustersUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_slo_target_error_component import (
        ApiV1S3ClustersUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_slo_window_days_error_component import (
        ApiV1S3ClustersUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1s3_clusters_update_slug_error_component import ApiV1S3ClustersUpdateSlugErrorComponent
    from ..models.api_v1s3_clusters_update_target_availability_error_component import (
        ApiV1S3ClustersUpdateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1S3ClustersUpdateValidationError")


@_attrs_define
class ApiV1S3ClustersUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1S3ClustersUpdateActiveErrorComponent | ApiV1S3ClustersUpdateActualAvailabilityErrorComponent |
            ApiV1S3ClustersUpdateAdminEndpointErrorComponent | ApiV1S3ClustersUpdateAdminEndpointSecureErrorComponent |
            ApiV1S3ClustersUpdateAliasErrorComponent | ApiV1S3ClustersUpdateAllowNewBucketsErrorComponent |
            ApiV1S3ClustersUpdateAnnotationsErrorComponent | ApiV1S3ClustersUpdateArchivedAtErrorComponent |
            ApiV1S3ClustersUpdateArchivedByErrorComponent | ApiV1S3ClustersUpdateArchivedErrorComponent |
            ApiV1S3ClustersUpdateArchivedReasonErrorComponent | ApiV1S3ClustersUpdateCephOsdClusterTotalBytesErrorComponent
            | ApiV1S3ClustersUpdateClusterConfigErrorComponent | ApiV1S3ClustersUpdateClusterInfoErrorComponent |
            ApiV1S3ClustersUpdateCreatedByComponentErrorComponent | ApiV1S3ClustersUpdateCreatedByUserErrorComponent |
            ApiV1S3ClustersUpdateCredentialErrorComponent | ApiV1S3ClustersUpdateCriticalityErrorComponent |
            ApiV1S3ClustersUpdateDebugModeErrorComponent | ApiV1S3ClustersUpdateDefaultProductErrorComponent |
            ApiV1S3ClustersUpdateDescriptionErrorComponent | ApiV1S3ClustersUpdateDiscoveryEnabledErrorComponent |
            ApiV1S3ClustersUpdateDisplayNameErrorComponent | ApiV1S3ClustersUpdateEndpointErrorComponent |
            ApiV1S3ClustersUpdateEndpointSecureErrorComponent | ApiV1S3ClustersUpdateIncludeInCostStatementErrorComponent |
            ApiV1S3ClustersUpdateK8SClusterErrorComponent | ApiV1S3ClustersUpdateKindErrorComponent |
            ApiV1S3ClustersUpdateLabelsErrorComponent | ApiV1S3ClustersUpdateLastReconciliationDurationSecondsErrorComponent
            | ApiV1S3ClustersUpdateManagedBucketsObjectCountErrorComponent |
            ApiV1S3ClustersUpdateManagedBucketsUsageKbErrorComponent |
            ApiV1S3ClustersUpdateManagedByContentTypeErrorComponent | ApiV1S3ClustersUpdateManagedByObjectIdErrorComponent |
            ApiV1S3ClustersUpdateMinioClusterCapacityUsableBytesErrorComponent |
            ApiV1S3ClustersUpdateMinioClusterUsageBytesErrorComponent | ApiV1S3ClustersUpdateModifiedByUserErrorComponent |
            ApiV1S3ClustersUpdateNameErrorComponent | ApiV1S3ClustersUpdateNamespaceErrorComponent |
            ApiV1S3ClustersUpdateNonFieldErrorsErrorComponent | ApiV1S3ClustersUpdatePlatformDnsRecordCreatedErrorComponent
            | ApiV1S3ClustersUpdatePlatformServiceErrorComponent | ApiV1S3ClustersUpdateProviderErrorComponent |
            ApiV1S3ClustersUpdateProviderIdErrorComponent | ApiV1S3ClustersUpdateProviderReferenceErrorComponent |
            ApiV1S3ClustersUpdateRadosgwBucketsLogicalUsedBytesErrorComponent |
            ApiV1S3ClustersUpdateReconciliationEnabledErrorComponent | ApiV1S3ClustersUpdateRegionErrorComponent |
            ApiV1S3ClustersUpdateScopeErrorComponent | ApiV1S3ClustersUpdateSlaAvailabilityErrorComponent |
            ApiV1S3ClustersUpdateSlaTargetErrorComponent | ApiV1S3ClustersUpdateSlaWindowDaysErrorComponent |
            ApiV1S3ClustersUpdateSloAvailabilityErrorComponent | ApiV1S3ClustersUpdateSloTargetErrorComponent |
            ApiV1S3ClustersUpdateSloWindowDaysErrorComponent | ApiV1S3ClustersUpdateSlugErrorComponent |
            ApiV1S3ClustersUpdateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1S3ClustersUpdateActiveErrorComponent
        | ApiV1S3ClustersUpdateActualAvailabilityErrorComponent
        | ApiV1S3ClustersUpdateAdminEndpointErrorComponent
        | ApiV1S3ClustersUpdateAdminEndpointSecureErrorComponent
        | ApiV1S3ClustersUpdateAliasErrorComponent
        | ApiV1S3ClustersUpdateAllowNewBucketsErrorComponent
        | ApiV1S3ClustersUpdateAnnotationsErrorComponent
        | ApiV1S3ClustersUpdateArchivedAtErrorComponent
        | ApiV1S3ClustersUpdateArchivedByErrorComponent
        | ApiV1S3ClustersUpdateArchivedErrorComponent
        | ApiV1S3ClustersUpdateArchivedReasonErrorComponent
        | ApiV1S3ClustersUpdateCephOsdClusterTotalBytesErrorComponent
        | ApiV1S3ClustersUpdateClusterConfigErrorComponent
        | ApiV1S3ClustersUpdateClusterInfoErrorComponent
        | ApiV1S3ClustersUpdateCreatedByComponentErrorComponent
        | ApiV1S3ClustersUpdateCreatedByUserErrorComponent
        | ApiV1S3ClustersUpdateCredentialErrorComponent
        | ApiV1S3ClustersUpdateCriticalityErrorComponent
        | ApiV1S3ClustersUpdateDebugModeErrorComponent
        | ApiV1S3ClustersUpdateDefaultProductErrorComponent
        | ApiV1S3ClustersUpdateDescriptionErrorComponent
        | ApiV1S3ClustersUpdateDiscoveryEnabledErrorComponent
        | ApiV1S3ClustersUpdateDisplayNameErrorComponent
        | ApiV1S3ClustersUpdateEndpointErrorComponent
        | ApiV1S3ClustersUpdateEndpointSecureErrorComponent
        | ApiV1S3ClustersUpdateIncludeInCostStatementErrorComponent
        | ApiV1S3ClustersUpdateK8SClusterErrorComponent
        | ApiV1S3ClustersUpdateKindErrorComponent
        | ApiV1S3ClustersUpdateLabelsErrorComponent
        | ApiV1S3ClustersUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1S3ClustersUpdateManagedBucketsObjectCountErrorComponent
        | ApiV1S3ClustersUpdateManagedBucketsUsageKbErrorComponent
        | ApiV1S3ClustersUpdateManagedByContentTypeErrorComponent
        | ApiV1S3ClustersUpdateManagedByObjectIdErrorComponent
        | ApiV1S3ClustersUpdateMinioClusterCapacityUsableBytesErrorComponent
        | ApiV1S3ClustersUpdateMinioClusterUsageBytesErrorComponent
        | ApiV1S3ClustersUpdateModifiedByUserErrorComponent
        | ApiV1S3ClustersUpdateNameErrorComponent
        | ApiV1S3ClustersUpdateNamespaceErrorComponent
        | ApiV1S3ClustersUpdateNonFieldErrorsErrorComponent
        | ApiV1S3ClustersUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1S3ClustersUpdatePlatformServiceErrorComponent
        | ApiV1S3ClustersUpdateProviderErrorComponent
        | ApiV1S3ClustersUpdateProviderIdErrorComponent
        | ApiV1S3ClustersUpdateProviderReferenceErrorComponent
        | ApiV1S3ClustersUpdateRadosgwBucketsLogicalUsedBytesErrorComponent
        | ApiV1S3ClustersUpdateReconciliationEnabledErrorComponent
        | ApiV1S3ClustersUpdateRegionErrorComponent
        | ApiV1S3ClustersUpdateScopeErrorComponent
        | ApiV1S3ClustersUpdateSlaAvailabilityErrorComponent
        | ApiV1S3ClustersUpdateSlaTargetErrorComponent
        | ApiV1S3ClustersUpdateSlaWindowDaysErrorComponent
        | ApiV1S3ClustersUpdateSloAvailabilityErrorComponent
        | ApiV1S3ClustersUpdateSloTargetErrorComponent
        | ApiV1S3ClustersUpdateSloWindowDaysErrorComponent
        | ApiV1S3ClustersUpdateSlugErrorComponent
        | ApiV1S3ClustersUpdateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1s3_clusters_update_active_error_component import ApiV1S3ClustersUpdateActiveErrorComponent
        from ..models.api_v1s3_clusters_update_actual_availability_error_component import (
            ApiV1S3ClustersUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_admin_endpoint_error_component import (
            ApiV1S3ClustersUpdateAdminEndpointErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_admin_endpoint_secure_error_component import (
            ApiV1S3ClustersUpdateAdminEndpointSecureErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_alias_error_component import ApiV1S3ClustersUpdateAliasErrorComponent
        from ..models.api_v1s3_clusters_update_allow_new_buckets_error_component import (
            ApiV1S3ClustersUpdateAllowNewBucketsErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_annotations_error_component import (
            ApiV1S3ClustersUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_archived_at_error_component import (
            ApiV1S3ClustersUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_archived_by_error_component import (
            ApiV1S3ClustersUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_archived_error_component import (
            ApiV1S3ClustersUpdateArchivedErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_archived_reason_error_component import (
            ApiV1S3ClustersUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_ceph_osd_cluster_total_bytes_error_component import (
            ApiV1S3ClustersUpdateCephOsdClusterTotalBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_cluster_config_error_component import (
            ApiV1S3ClustersUpdateClusterConfigErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_cluster_info_error_component import (
            ApiV1S3ClustersUpdateClusterInfoErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_created_by_component_error_component import (
            ApiV1S3ClustersUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_created_by_user_error_component import (
            ApiV1S3ClustersUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_credential_error_component import (
            ApiV1S3ClustersUpdateCredentialErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_criticality_error_component import (
            ApiV1S3ClustersUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_debug_mode_error_component import (
            ApiV1S3ClustersUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_description_error_component import (
            ApiV1S3ClustersUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_discovery_enabled_error_component import (
            ApiV1S3ClustersUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_display_name_error_component import (
            ApiV1S3ClustersUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_endpoint_error_component import (
            ApiV1S3ClustersUpdateEndpointErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_endpoint_secure_error_component import (
            ApiV1S3ClustersUpdateEndpointSecureErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_include_in_cost_statement_error_component import (
            ApiV1S3ClustersUpdateIncludeInCostStatementErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_k8s_cluster_error_component import (
            ApiV1S3ClustersUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_kind_error_component import ApiV1S3ClustersUpdateKindErrorComponent
        from ..models.api_v1s3_clusters_update_labels_error_component import ApiV1S3ClustersUpdateLabelsErrorComponent
        from ..models.api_v1s3_clusters_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1S3ClustersUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_managed_buckets_object_count_error_component import (
            ApiV1S3ClustersUpdateManagedBucketsObjectCountErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_managed_buckets_usage_kb_error_component import (
            ApiV1S3ClustersUpdateManagedBucketsUsageKbErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_managed_by_content_type_error_component import (
            ApiV1S3ClustersUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_managed_by_object_id_error_component import (
            ApiV1S3ClustersUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_minio_cluster_capacity_usable_bytes_error_component import (
            ApiV1S3ClustersUpdateMinioClusterCapacityUsableBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_minio_cluster_usage_bytes_error_component import (
            ApiV1S3ClustersUpdateMinioClusterUsageBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_modified_by_user_error_component import (
            ApiV1S3ClustersUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_name_error_component import ApiV1S3ClustersUpdateNameErrorComponent
        from ..models.api_v1s3_clusters_update_namespace_error_component import (
            ApiV1S3ClustersUpdateNamespaceErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_non_field_errors_error_component import (
            ApiV1S3ClustersUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_platform_dns_record_created_error_component import (
            ApiV1S3ClustersUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_platform_service_error_component import (
            ApiV1S3ClustersUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_provider_error_component import (
            ApiV1S3ClustersUpdateProviderErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_provider_id_error_component import (
            ApiV1S3ClustersUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_provider_reference_error_component import (
            ApiV1S3ClustersUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_radosgw_buckets_logical_used_bytes_error_component import (
            ApiV1S3ClustersUpdateRadosgwBucketsLogicalUsedBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_reconciliation_enabled_error_component import (
            ApiV1S3ClustersUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_region_error_component import ApiV1S3ClustersUpdateRegionErrorComponent
        from ..models.api_v1s3_clusters_update_scope_error_component import ApiV1S3ClustersUpdateScopeErrorComponent
        from ..models.api_v1s3_clusters_update_sla_availability_error_component import (
            ApiV1S3ClustersUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_sla_target_error_component import (
            ApiV1S3ClustersUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_sla_window_days_error_component import (
            ApiV1S3ClustersUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_slo_availability_error_component import (
            ApiV1S3ClustersUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_slo_target_error_component import (
            ApiV1S3ClustersUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_slo_window_days_error_component import (
            ApiV1S3ClustersUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_slug_error_component import ApiV1S3ClustersUpdateSlugErrorComponent
        from ..models.api_v1s3_clusters_update_target_availability_error_component import (
            ApiV1S3ClustersUpdateTargetAvailabilityErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1S3ClustersUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateEndpointSecureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateAdminEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateAdminEndpointSecureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateClusterConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateClusterInfoErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateAllowNewBucketsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateIncludeInCostStatementErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateCephOsdClusterTotalBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateRadosgwBucketsLogicalUsedBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateMinioClusterCapacityUsableBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateMinioClusterUsageBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateManagedBucketsUsageKbErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateManagedBucketsObjectCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersUpdateK8SClusterErrorComponent):
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
        from ..models.api_v1s3_clusters_update_active_error_component import ApiV1S3ClustersUpdateActiveErrorComponent
        from ..models.api_v1s3_clusters_update_actual_availability_error_component import (
            ApiV1S3ClustersUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_admin_endpoint_error_component import (
            ApiV1S3ClustersUpdateAdminEndpointErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_admin_endpoint_secure_error_component import (
            ApiV1S3ClustersUpdateAdminEndpointSecureErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_alias_error_component import ApiV1S3ClustersUpdateAliasErrorComponent
        from ..models.api_v1s3_clusters_update_allow_new_buckets_error_component import (
            ApiV1S3ClustersUpdateAllowNewBucketsErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_annotations_error_component import (
            ApiV1S3ClustersUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_archived_at_error_component import (
            ApiV1S3ClustersUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_archived_by_error_component import (
            ApiV1S3ClustersUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_archived_error_component import (
            ApiV1S3ClustersUpdateArchivedErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_archived_reason_error_component import (
            ApiV1S3ClustersUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_ceph_osd_cluster_total_bytes_error_component import (
            ApiV1S3ClustersUpdateCephOsdClusterTotalBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_cluster_config_error_component import (
            ApiV1S3ClustersUpdateClusterConfigErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_cluster_info_error_component import (
            ApiV1S3ClustersUpdateClusterInfoErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_created_by_component_error_component import (
            ApiV1S3ClustersUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_created_by_user_error_component import (
            ApiV1S3ClustersUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_credential_error_component import (
            ApiV1S3ClustersUpdateCredentialErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_criticality_error_component import (
            ApiV1S3ClustersUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_debug_mode_error_component import (
            ApiV1S3ClustersUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_default_product_error_component import (
            ApiV1S3ClustersUpdateDefaultProductErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_description_error_component import (
            ApiV1S3ClustersUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_discovery_enabled_error_component import (
            ApiV1S3ClustersUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_display_name_error_component import (
            ApiV1S3ClustersUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_endpoint_error_component import (
            ApiV1S3ClustersUpdateEndpointErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_endpoint_secure_error_component import (
            ApiV1S3ClustersUpdateEndpointSecureErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_include_in_cost_statement_error_component import (
            ApiV1S3ClustersUpdateIncludeInCostStatementErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_k8s_cluster_error_component import (
            ApiV1S3ClustersUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_kind_error_component import ApiV1S3ClustersUpdateKindErrorComponent
        from ..models.api_v1s3_clusters_update_labels_error_component import ApiV1S3ClustersUpdateLabelsErrorComponent
        from ..models.api_v1s3_clusters_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1S3ClustersUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_managed_buckets_object_count_error_component import (
            ApiV1S3ClustersUpdateManagedBucketsObjectCountErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_managed_buckets_usage_kb_error_component import (
            ApiV1S3ClustersUpdateManagedBucketsUsageKbErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_managed_by_content_type_error_component import (
            ApiV1S3ClustersUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_managed_by_object_id_error_component import (
            ApiV1S3ClustersUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_minio_cluster_capacity_usable_bytes_error_component import (
            ApiV1S3ClustersUpdateMinioClusterCapacityUsableBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_minio_cluster_usage_bytes_error_component import (
            ApiV1S3ClustersUpdateMinioClusterUsageBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_modified_by_user_error_component import (
            ApiV1S3ClustersUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_name_error_component import ApiV1S3ClustersUpdateNameErrorComponent
        from ..models.api_v1s3_clusters_update_namespace_error_component import (
            ApiV1S3ClustersUpdateNamespaceErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_non_field_errors_error_component import (
            ApiV1S3ClustersUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_platform_dns_record_created_error_component import (
            ApiV1S3ClustersUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_platform_service_error_component import (
            ApiV1S3ClustersUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_provider_error_component import (
            ApiV1S3ClustersUpdateProviderErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_provider_id_error_component import (
            ApiV1S3ClustersUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_provider_reference_error_component import (
            ApiV1S3ClustersUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_radosgw_buckets_logical_used_bytes_error_component import (
            ApiV1S3ClustersUpdateRadosgwBucketsLogicalUsedBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_reconciliation_enabled_error_component import (
            ApiV1S3ClustersUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_region_error_component import ApiV1S3ClustersUpdateRegionErrorComponent
        from ..models.api_v1s3_clusters_update_scope_error_component import ApiV1S3ClustersUpdateScopeErrorComponent
        from ..models.api_v1s3_clusters_update_sla_availability_error_component import (
            ApiV1S3ClustersUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_sla_target_error_component import (
            ApiV1S3ClustersUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_sla_window_days_error_component import (
            ApiV1S3ClustersUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_slo_availability_error_component import (
            ApiV1S3ClustersUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_slo_target_error_component import (
            ApiV1S3ClustersUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_slo_window_days_error_component import (
            ApiV1S3ClustersUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1s3_clusters_update_slug_error_component import ApiV1S3ClustersUpdateSlugErrorComponent
        from ..models.api_v1s3_clusters_update_target_availability_error_component import (
            ApiV1S3ClustersUpdateTargetAvailabilityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1S3ClustersUpdateActiveErrorComponent
                | ApiV1S3ClustersUpdateActualAvailabilityErrorComponent
                | ApiV1S3ClustersUpdateAdminEndpointErrorComponent
                | ApiV1S3ClustersUpdateAdminEndpointSecureErrorComponent
                | ApiV1S3ClustersUpdateAliasErrorComponent
                | ApiV1S3ClustersUpdateAllowNewBucketsErrorComponent
                | ApiV1S3ClustersUpdateAnnotationsErrorComponent
                | ApiV1S3ClustersUpdateArchivedAtErrorComponent
                | ApiV1S3ClustersUpdateArchivedByErrorComponent
                | ApiV1S3ClustersUpdateArchivedErrorComponent
                | ApiV1S3ClustersUpdateArchivedReasonErrorComponent
                | ApiV1S3ClustersUpdateCephOsdClusterTotalBytesErrorComponent
                | ApiV1S3ClustersUpdateClusterConfigErrorComponent
                | ApiV1S3ClustersUpdateClusterInfoErrorComponent
                | ApiV1S3ClustersUpdateCreatedByComponentErrorComponent
                | ApiV1S3ClustersUpdateCreatedByUserErrorComponent
                | ApiV1S3ClustersUpdateCredentialErrorComponent
                | ApiV1S3ClustersUpdateCriticalityErrorComponent
                | ApiV1S3ClustersUpdateDebugModeErrorComponent
                | ApiV1S3ClustersUpdateDefaultProductErrorComponent
                | ApiV1S3ClustersUpdateDescriptionErrorComponent
                | ApiV1S3ClustersUpdateDiscoveryEnabledErrorComponent
                | ApiV1S3ClustersUpdateDisplayNameErrorComponent
                | ApiV1S3ClustersUpdateEndpointErrorComponent
                | ApiV1S3ClustersUpdateEndpointSecureErrorComponent
                | ApiV1S3ClustersUpdateIncludeInCostStatementErrorComponent
                | ApiV1S3ClustersUpdateK8SClusterErrorComponent
                | ApiV1S3ClustersUpdateKindErrorComponent
                | ApiV1S3ClustersUpdateLabelsErrorComponent
                | ApiV1S3ClustersUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1S3ClustersUpdateManagedBucketsObjectCountErrorComponent
                | ApiV1S3ClustersUpdateManagedBucketsUsageKbErrorComponent
                | ApiV1S3ClustersUpdateManagedByContentTypeErrorComponent
                | ApiV1S3ClustersUpdateManagedByObjectIdErrorComponent
                | ApiV1S3ClustersUpdateMinioClusterCapacityUsableBytesErrorComponent
                | ApiV1S3ClustersUpdateMinioClusterUsageBytesErrorComponent
                | ApiV1S3ClustersUpdateModifiedByUserErrorComponent
                | ApiV1S3ClustersUpdateNameErrorComponent
                | ApiV1S3ClustersUpdateNamespaceErrorComponent
                | ApiV1S3ClustersUpdateNonFieldErrorsErrorComponent
                | ApiV1S3ClustersUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1S3ClustersUpdatePlatformServiceErrorComponent
                | ApiV1S3ClustersUpdateProviderErrorComponent
                | ApiV1S3ClustersUpdateProviderIdErrorComponent
                | ApiV1S3ClustersUpdateProviderReferenceErrorComponent
                | ApiV1S3ClustersUpdateRadosgwBucketsLogicalUsedBytesErrorComponent
                | ApiV1S3ClustersUpdateReconciliationEnabledErrorComponent
                | ApiV1S3ClustersUpdateRegionErrorComponent
                | ApiV1S3ClustersUpdateScopeErrorComponent
                | ApiV1S3ClustersUpdateSlaAvailabilityErrorComponent
                | ApiV1S3ClustersUpdateSlaTargetErrorComponent
                | ApiV1S3ClustersUpdateSlaWindowDaysErrorComponent
                | ApiV1S3ClustersUpdateSloAvailabilityErrorComponent
                | ApiV1S3ClustersUpdateSloTargetErrorComponent
                | ApiV1S3ClustersUpdateSloWindowDaysErrorComponent
                | ApiV1S3ClustersUpdateSlugErrorComponent
                | ApiV1S3ClustersUpdateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_0 = (
                        ApiV1S3ClustersUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_1 = (
                        ApiV1S3ClustersUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_2 = (
                        ApiV1S3ClustersUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_3 = (
                        ApiV1S3ClustersUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_4 = (
                        ApiV1S3ClustersUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_5 = (
                        ApiV1S3ClustersUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_6 = (
                        ApiV1S3ClustersUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_7 = (
                        ApiV1S3ClustersUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_8 = (
                        ApiV1S3ClustersUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_9 = (
                        ApiV1S3ClustersUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_10 = (
                        ApiV1S3ClustersUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_11 = (
                        ApiV1S3ClustersUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_12 = (
                        ApiV1S3ClustersUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_13 = (
                        ApiV1S3ClustersUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_14 = (
                        ApiV1S3ClustersUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_15 = (
                        ApiV1S3ClustersUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_16 = (
                        ApiV1S3ClustersUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_17 = (
                        ApiV1S3ClustersUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_18 = (
                        ApiV1S3ClustersUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_19 = (
                        ApiV1S3ClustersUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_20 = (
                        ApiV1S3ClustersUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_21 = (
                        ApiV1S3ClustersUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_22 = (
                        ApiV1S3ClustersUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_23 = (
                        ApiV1S3ClustersUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_24 = (
                        ApiV1S3ClustersUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_25 = (
                        ApiV1S3ClustersUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_26 = (
                        ApiV1S3ClustersUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_27 = (
                        ApiV1S3ClustersUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_28 = (
                        ApiV1S3ClustersUpdateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_29 = (
                        ApiV1S3ClustersUpdateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_30 = (
                        ApiV1S3ClustersUpdateEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_31 = (
                        ApiV1S3ClustersUpdateEndpointSecureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_32 = (
                        ApiV1S3ClustersUpdateAdminEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_33 = (
                        ApiV1S3ClustersUpdateAdminEndpointSecureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_34 = (
                        ApiV1S3ClustersUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_35 = (
                        ApiV1S3ClustersUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_36 = (
                        ApiV1S3ClustersUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_37 = (
                        ApiV1S3ClustersUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_38 = (
                        ApiV1S3ClustersUpdateClusterConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_39 = (
                        ApiV1S3ClustersUpdateClusterInfoErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_40 = (
                        ApiV1S3ClustersUpdateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_41 = (
                        ApiV1S3ClustersUpdateRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_42 = (
                        ApiV1S3ClustersUpdateAllowNewBucketsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_43 = (
                        ApiV1S3ClustersUpdateIncludeInCostStatementErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_44 = (
                        ApiV1S3ClustersUpdateCephOsdClusterTotalBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_45 = (
                        ApiV1S3ClustersUpdateRadosgwBucketsLogicalUsedBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_46 = (
                        ApiV1S3ClustersUpdateMinioClusterCapacityUsableBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_47 = (
                        ApiV1S3ClustersUpdateMinioClusterUsageBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_48 = (
                        ApiV1S3ClustersUpdateManagedBucketsUsageKbErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_49 = (
                        ApiV1S3ClustersUpdateManagedBucketsObjectCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_50 = (
                        ApiV1S3ClustersUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_51 = (
                        ApiV1S3ClustersUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_52 = (
                        ApiV1S3ClustersUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_53 = (
                        ApiV1S3ClustersUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_54 = (
                        ApiV1S3ClustersUpdateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_update_error_type_55 = (
                        ApiV1S3ClustersUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_update_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1s3_clusters_update_error_type_56 = (
                    ApiV1S3ClustersUpdateDefaultProductErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1s3_clusters_update_error_type_56

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1s3_clusters_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1s3_clusters_update_validation_error.additional_properties = d
        return api_v1s3_clusters_update_validation_error

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
