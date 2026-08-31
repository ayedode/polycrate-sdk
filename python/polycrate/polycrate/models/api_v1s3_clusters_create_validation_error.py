from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1s3_clusters_create_active_error_component import ApiV1S3ClustersCreateActiveErrorComponent
    from ..models.api_v1s3_clusters_create_actual_availability_error_component import (
        ApiV1S3ClustersCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_admin_endpoint_error_component import (
        ApiV1S3ClustersCreateAdminEndpointErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_admin_endpoint_secure_error_component import (
        ApiV1S3ClustersCreateAdminEndpointSecureErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_alias_error_component import ApiV1S3ClustersCreateAliasErrorComponent
    from ..models.api_v1s3_clusters_create_allow_new_buckets_error_component import (
        ApiV1S3ClustersCreateAllowNewBucketsErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_annotations_error_component import (
        ApiV1S3ClustersCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_archived_at_error_component import (
        ApiV1S3ClustersCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_archived_by_error_component import (
        ApiV1S3ClustersCreateArchivedByErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_archived_error_component import ApiV1S3ClustersCreateArchivedErrorComponent
    from ..models.api_v1s3_clusters_create_archived_reason_error_component import (
        ApiV1S3ClustersCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_ceph_osd_cluster_total_bytes_error_component import (
        ApiV1S3ClustersCreateCephOsdClusterTotalBytesErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_cluster_config_error_component import (
        ApiV1S3ClustersCreateClusterConfigErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_cluster_info_error_component import (
        ApiV1S3ClustersCreateClusterInfoErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_created_by_component_error_component import (
        ApiV1S3ClustersCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_created_by_user_error_component import (
        ApiV1S3ClustersCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_credential_error_component import (
        ApiV1S3ClustersCreateCredentialErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_criticality_error_component import (
        ApiV1S3ClustersCreateCriticalityErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_debug_mode_error_component import (
        ApiV1S3ClustersCreateDebugModeErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_default_product_error_component import (
        ApiV1S3ClustersCreateDefaultProductErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_description_error_component import (
        ApiV1S3ClustersCreateDescriptionErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_discovery_enabled_error_component import (
        ApiV1S3ClustersCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_display_name_error_component import (
        ApiV1S3ClustersCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_endpoint_error_component import ApiV1S3ClustersCreateEndpointErrorComponent
    from ..models.api_v1s3_clusters_create_endpoint_secure_error_component import (
        ApiV1S3ClustersCreateEndpointSecureErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_include_in_cost_statement_error_component import (
        ApiV1S3ClustersCreateIncludeInCostStatementErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_k8s_cluster_error_component import (
        ApiV1S3ClustersCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_kind_error_component import ApiV1S3ClustersCreateKindErrorComponent
    from ..models.api_v1s3_clusters_create_labels_error_component import ApiV1S3ClustersCreateLabelsErrorComponent
    from ..models.api_v1s3_clusters_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1S3ClustersCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_managed_buckets_object_count_error_component import (
        ApiV1S3ClustersCreateManagedBucketsObjectCountErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_managed_buckets_usage_kb_error_component import (
        ApiV1S3ClustersCreateManagedBucketsUsageKbErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_managed_by_content_type_error_component import (
        ApiV1S3ClustersCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_managed_by_object_id_error_component import (
        ApiV1S3ClustersCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_minio_cluster_capacity_usable_bytes_error_component import (
        ApiV1S3ClustersCreateMinioClusterCapacityUsableBytesErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_minio_cluster_usage_bytes_error_component import (
        ApiV1S3ClustersCreateMinioClusterUsageBytesErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_modified_by_user_error_component import (
        ApiV1S3ClustersCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_name_error_component import ApiV1S3ClustersCreateNameErrorComponent
    from ..models.api_v1s3_clusters_create_namespace_error_component import ApiV1S3ClustersCreateNamespaceErrorComponent
    from ..models.api_v1s3_clusters_create_non_field_errors_error_component import (
        ApiV1S3ClustersCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_platform_dns_record_created_error_component import (
        ApiV1S3ClustersCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_platform_service_error_component import (
        ApiV1S3ClustersCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_provider_error_component import ApiV1S3ClustersCreateProviderErrorComponent
    from ..models.api_v1s3_clusters_create_provider_id_error_component import (
        ApiV1S3ClustersCreateProviderIdErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_provider_reference_error_component import (
        ApiV1S3ClustersCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_radosgw_buckets_logical_used_bytes_error_component import (
        ApiV1S3ClustersCreateRadosgwBucketsLogicalUsedBytesErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_reconciliation_enabled_error_component import (
        ApiV1S3ClustersCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_region_error_component import ApiV1S3ClustersCreateRegionErrorComponent
    from ..models.api_v1s3_clusters_create_scope_error_component import ApiV1S3ClustersCreateScopeErrorComponent
    from ..models.api_v1s3_clusters_create_sla_availability_error_component import (
        ApiV1S3ClustersCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_sla_target_error_component import (
        ApiV1S3ClustersCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_sla_window_days_error_component import (
        ApiV1S3ClustersCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_slo_availability_error_component import (
        ApiV1S3ClustersCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_slo_target_error_component import (
        ApiV1S3ClustersCreateSloTargetErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_slo_window_days_error_component import (
        ApiV1S3ClustersCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1s3_clusters_create_slug_error_component import ApiV1S3ClustersCreateSlugErrorComponent
    from ..models.api_v1s3_clusters_create_target_availability_error_component import (
        ApiV1S3ClustersCreateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1S3ClustersCreateValidationError")


@_attrs_define
class ApiV1S3ClustersCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1S3ClustersCreateActiveErrorComponent | ApiV1S3ClustersCreateActualAvailabilityErrorComponent |
            ApiV1S3ClustersCreateAdminEndpointErrorComponent | ApiV1S3ClustersCreateAdminEndpointSecureErrorComponent |
            ApiV1S3ClustersCreateAliasErrorComponent | ApiV1S3ClustersCreateAllowNewBucketsErrorComponent |
            ApiV1S3ClustersCreateAnnotationsErrorComponent | ApiV1S3ClustersCreateArchivedAtErrorComponent |
            ApiV1S3ClustersCreateArchivedByErrorComponent | ApiV1S3ClustersCreateArchivedErrorComponent |
            ApiV1S3ClustersCreateArchivedReasonErrorComponent | ApiV1S3ClustersCreateCephOsdClusterTotalBytesErrorComponent
            | ApiV1S3ClustersCreateClusterConfigErrorComponent | ApiV1S3ClustersCreateClusterInfoErrorComponent |
            ApiV1S3ClustersCreateCreatedByComponentErrorComponent | ApiV1S3ClustersCreateCreatedByUserErrorComponent |
            ApiV1S3ClustersCreateCredentialErrorComponent | ApiV1S3ClustersCreateCriticalityErrorComponent |
            ApiV1S3ClustersCreateDebugModeErrorComponent | ApiV1S3ClustersCreateDefaultProductErrorComponent |
            ApiV1S3ClustersCreateDescriptionErrorComponent | ApiV1S3ClustersCreateDiscoveryEnabledErrorComponent |
            ApiV1S3ClustersCreateDisplayNameErrorComponent | ApiV1S3ClustersCreateEndpointErrorComponent |
            ApiV1S3ClustersCreateEndpointSecureErrorComponent | ApiV1S3ClustersCreateIncludeInCostStatementErrorComponent |
            ApiV1S3ClustersCreateK8SClusterErrorComponent | ApiV1S3ClustersCreateKindErrorComponent |
            ApiV1S3ClustersCreateLabelsErrorComponent | ApiV1S3ClustersCreateLastReconciliationDurationSecondsErrorComponent
            | ApiV1S3ClustersCreateManagedBucketsObjectCountErrorComponent |
            ApiV1S3ClustersCreateManagedBucketsUsageKbErrorComponent |
            ApiV1S3ClustersCreateManagedByContentTypeErrorComponent | ApiV1S3ClustersCreateManagedByObjectIdErrorComponent |
            ApiV1S3ClustersCreateMinioClusterCapacityUsableBytesErrorComponent |
            ApiV1S3ClustersCreateMinioClusterUsageBytesErrorComponent | ApiV1S3ClustersCreateModifiedByUserErrorComponent |
            ApiV1S3ClustersCreateNameErrorComponent | ApiV1S3ClustersCreateNamespaceErrorComponent |
            ApiV1S3ClustersCreateNonFieldErrorsErrorComponent | ApiV1S3ClustersCreatePlatformDnsRecordCreatedErrorComponent
            | ApiV1S3ClustersCreatePlatformServiceErrorComponent | ApiV1S3ClustersCreateProviderErrorComponent |
            ApiV1S3ClustersCreateProviderIdErrorComponent | ApiV1S3ClustersCreateProviderReferenceErrorComponent |
            ApiV1S3ClustersCreateRadosgwBucketsLogicalUsedBytesErrorComponent |
            ApiV1S3ClustersCreateReconciliationEnabledErrorComponent | ApiV1S3ClustersCreateRegionErrorComponent |
            ApiV1S3ClustersCreateScopeErrorComponent | ApiV1S3ClustersCreateSlaAvailabilityErrorComponent |
            ApiV1S3ClustersCreateSlaTargetErrorComponent | ApiV1S3ClustersCreateSlaWindowDaysErrorComponent |
            ApiV1S3ClustersCreateSloAvailabilityErrorComponent | ApiV1S3ClustersCreateSloTargetErrorComponent |
            ApiV1S3ClustersCreateSloWindowDaysErrorComponent | ApiV1S3ClustersCreateSlugErrorComponent |
            ApiV1S3ClustersCreateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1S3ClustersCreateActiveErrorComponent
        | ApiV1S3ClustersCreateActualAvailabilityErrorComponent
        | ApiV1S3ClustersCreateAdminEndpointErrorComponent
        | ApiV1S3ClustersCreateAdminEndpointSecureErrorComponent
        | ApiV1S3ClustersCreateAliasErrorComponent
        | ApiV1S3ClustersCreateAllowNewBucketsErrorComponent
        | ApiV1S3ClustersCreateAnnotationsErrorComponent
        | ApiV1S3ClustersCreateArchivedAtErrorComponent
        | ApiV1S3ClustersCreateArchivedByErrorComponent
        | ApiV1S3ClustersCreateArchivedErrorComponent
        | ApiV1S3ClustersCreateArchivedReasonErrorComponent
        | ApiV1S3ClustersCreateCephOsdClusterTotalBytesErrorComponent
        | ApiV1S3ClustersCreateClusterConfigErrorComponent
        | ApiV1S3ClustersCreateClusterInfoErrorComponent
        | ApiV1S3ClustersCreateCreatedByComponentErrorComponent
        | ApiV1S3ClustersCreateCreatedByUserErrorComponent
        | ApiV1S3ClustersCreateCredentialErrorComponent
        | ApiV1S3ClustersCreateCriticalityErrorComponent
        | ApiV1S3ClustersCreateDebugModeErrorComponent
        | ApiV1S3ClustersCreateDefaultProductErrorComponent
        | ApiV1S3ClustersCreateDescriptionErrorComponent
        | ApiV1S3ClustersCreateDiscoveryEnabledErrorComponent
        | ApiV1S3ClustersCreateDisplayNameErrorComponent
        | ApiV1S3ClustersCreateEndpointErrorComponent
        | ApiV1S3ClustersCreateEndpointSecureErrorComponent
        | ApiV1S3ClustersCreateIncludeInCostStatementErrorComponent
        | ApiV1S3ClustersCreateK8SClusterErrorComponent
        | ApiV1S3ClustersCreateKindErrorComponent
        | ApiV1S3ClustersCreateLabelsErrorComponent
        | ApiV1S3ClustersCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1S3ClustersCreateManagedBucketsObjectCountErrorComponent
        | ApiV1S3ClustersCreateManagedBucketsUsageKbErrorComponent
        | ApiV1S3ClustersCreateManagedByContentTypeErrorComponent
        | ApiV1S3ClustersCreateManagedByObjectIdErrorComponent
        | ApiV1S3ClustersCreateMinioClusterCapacityUsableBytesErrorComponent
        | ApiV1S3ClustersCreateMinioClusterUsageBytesErrorComponent
        | ApiV1S3ClustersCreateModifiedByUserErrorComponent
        | ApiV1S3ClustersCreateNameErrorComponent
        | ApiV1S3ClustersCreateNamespaceErrorComponent
        | ApiV1S3ClustersCreateNonFieldErrorsErrorComponent
        | ApiV1S3ClustersCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1S3ClustersCreatePlatformServiceErrorComponent
        | ApiV1S3ClustersCreateProviderErrorComponent
        | ApiV1S3ClustersCreateProviderIdErrorComponent
        | ApiV1S3ClustersCreateProviderReferenceErrorComponent
        | ApiV1S3ClustersCreateRadosgwBucketsLogicalUsedBytesErrorComponent
        | ApiV1S3ClustersCreateReconciliationEnabledErrorComponent
        | ApiV1S3ClustersCreateRegionErrorComponent
        | ApiV1S3ClustersCreateScopeErrorComponent
        | ApiV1S3ClustersCreateSlaAvailabilityErrorComponent
        | ApiV1S3ClustersCreateSlaTargetErrorComponent
        | ApiV1S3ClustersCreateSlaWindowDaysErrorComponent
        | ApiV1S3ClustersCreateSloAvailabilityErrorComponent
        | ApiV1S3ClustersCreateSloTargetErrorComponent
        | ApiV1S3ClustersCreateSloWindowDaysErrorComponent
        | ApiV1S3ClustersCreateSlugErrorComponent
        | ApiV1S3ClustersCreateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1s3_clusters_create_active_error_component import ApiV1S3ClustersCreateActiveErrorComponent
        from ..models.api_v1s3_clusters_create_actual_availability_error_component import (
            ApiV1S3ClustersCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_admin_endpoint_error_component import (
            ApiV1S3ClustersCreateAdminEndpointErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_admin_endpoint_secure_error_component import (
            ApiV1S3ClustersCreateAdminEndpointSecureErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_alias_error_component import ApiV1S3ClustersCreateAliasErrorComponent
        from ..models.api_v1s3_clusters_create_allow_new_buckets_error_component import (
            ApiV1S3ClustersCreateAllowNewBucketsErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_annotations_error_component import (
            ApiV1S3ClustersCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_archived_at_error_component import (
            ApiV1S3ClustersCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_archived_by_error_component import (
            ApiV1S3ClustersCreateArchivedByErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_archived_error_component import (
            ApiV1S3ClustersCreateArchivedErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_archived_reason_error_component import (
            ApiV1S3ClustersCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_ceph_osd_cluster_total_bytes_error_component import (
            ApiV1S3ClustersCreateCephOsdClusterTotalBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_cluster_config_error_component import (
            ApiV1S3ClustersCreateClusterConfigErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_cluster_info_error_component import (
            ApiV1S3ClustersCreateClusterInfoErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_created_by_component_error_component import (
            ApiV1S3ClustersCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_created_by_user_error_component import (
            ApiV1S3ClustersCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_credential_error_component import (
            ApiV1S3ClustersCreateCredentialErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_criticality_error_component import (
            ApiV1S3ClustersCreateCriticalityErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_debug_mode_error_component import (
            ApiV1S3ClustersCreateDebugModeErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_description_error_component import (
            ApiV1S3ClustersCreateDescriptionErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_discovery_enabled_error_component import (
            ApiV1S3ClustersCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_display_name_error_component import (
            ApiV1S3ClustersCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_endpoint_error_component import (
            ApiV1S3ClustersCreateEndpointErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_endpoint_secure_error_component import (
            ApiV1S3ClustersCreateEndpointSecureErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_include_in_cost_statement_error_component import (
            ApiV1S3ClustersCreateIncludeInCostStatementErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_k8s_cluster_error_component import (
            ApiV1S3ClustersCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_kind_error_component import ApiV1S3ClustersCreateKindErrorComponent
        from ..models.api_v1s3_clusters_create_labels_error_component import ApiV1S3ClustersCreateLabelsErrorComponent
        from ..models.api_v1s3_clusters_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1S3ClustersCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_managed_buckets_object_count_error_component import (
            ApiV1S3ClustersCreateManagedBucketsObjectCountErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_managed_buckets_usage_kb_error_component import (
            ApiV1S3ClustersCreateManagedBucketsUsageKbErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_managed_by_content_type_error_component import (
            ApiV1S3ClustersCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_managed_by_object_id_error_component import (
            ApiV1S3ClustersCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_minio_cluster_capacity_usable_bytes_error_component import (
            ApiV1S3ClustersCreateMinioClusterCapacityUsableBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_minio_cluster_usage_bytes_error_component import (
            ApiV1S3ClustersCreateMinioClusterUsageBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_modified_by_user_error_component import (
            ApiV1S3ClustersCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_name_error_component import ApiV1S3ClustersCreateNameErrorComponent
        from ..models.api_v1s3_clusters_create_namespace_error_component import (
            ApiV1S3ClustersCreateNamespaceErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_non_field_errors_error_component import (
            ApiV1S3ClustersCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_platform_dns_record_created_error_component import (
            ApiV1S3ClustersCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_platform_service_error_component import (
            ApiV1S3ClustersCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_provider_error_component import (
            ApiV1S3ClustersCreateProviderErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_provider_id_error_component import (
            ApiV1S3ClustersCreateProviderIdErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_provider_reference_error_component import (
            ApiV1S3ClustersCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_radosgw_buckets_logical_used_bytes_error_component import (
            ApiV1S3ClustersCreateRadosgwBucketsLogicalUsedBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_reconciliation_enabled_error_component import (
            ApiV1S3ClustersCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_region_error_component import ApiV1S3ClustersCreateRegionErrorComponent
        from ..models.api_v1s3_clusters_create_scope_error_component import ApiV1S3ClustersCreateScopeErrorComponent
        from ..models.api_v1s3_clusters_create_sla_availability_error_component import (
            ApiV1S3ClustersCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_sla_target_error_component import (
            ApiV1S3ClustersCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_sla_window_days_error_component import (
            ApiV1S3ClustersCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_slo_availability_error_component import (
            ApiV1S3ClustersCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_slo_target_error_component import (
            ApiV1S3ClustersCreateSloTargetErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_slo_window_days_error_component import (
            ApiV1S3ClustersCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_slug_error_component import ApiV1S3ClustersCreateSlugErrorComponent
        from ..models.api_v1s3_clusters_create_target_availability_error_component import (
            ApiV1S3ClustersCreateTargetAvailabilityErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1S3ClustersCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateEndpointSecureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateAdminEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateAdminEndpointSecureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateClusterConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateClusterInfoErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateAllowNewBucketsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateIncludeInCostStatementErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateCephOsdClusterTotalBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateRadosgwBucketsLogicalUsedBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateMinioClusterCapacityUsableBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateMinioClusterUsageBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateManagedBucketsUsageKbErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateManagedBucketsObjectCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersCreateK8SClusterErrorComponent):
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
        from ..models.api_v1s3_clusters_create_active_error_component import ApiV1S3ClustersCreateActiveErrorComponent
        from ..models.api_v1s3_clusters_create_actual_availability_error_component import (
            ApiV1S3ClustersCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_admin_endpoint_error_component import (
            ApiV1S3ClustersCreateAdminEndpointErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_admin_endpoint_secure_error_component import (
            ApiV1S3ClustersCreateAdminEndpointSecureErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_alias_error_component import ApiV1S3ClustersCreateAliasErrorComponent
        from ..models.api_v1s3_clusters_create_allow_new_buckets_error_component import (
            ApiV1S3ClustersCreateAllowNewBucketsErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_annotations_error_component import (
            ApiV1S3ClustersCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_archived_at_error_component import (
            ApiV1S3ClustersCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_archived_by_error_component import (
            ApiV1S3ClustersCreateArchivedByErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_archived_error_component import (
            ApiV1S3ClustersCreateArchivedErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_archived_reason_error_component import (
            ApiV1S3ClustersCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_ceph_osd_cluster_total_bytes_error_component import (
            ApiV1S3ClustersCreateCephOsdClusterTotalBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_cluster_config_error_component import (
            ApiV1S3ClustersCreateClusterConfigErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_cluster_info_error_component import (
            ApiV1S3ClustersCreateClusterInfoErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_created_by_component_error_component import (
            ApiV1S3ClustersCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_created_by_user_error_component import (
            ApiV1S3ClustersCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_credential_error_component import (
            ApiV1S3ClustersCreateCredentialErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_criticality_error_component import (
            ApiV1S3ClustersCreateCriticalityErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_debug_mode_error_component import (
            ApiV1S3ClustersCreateDebugModeErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_default_product_error_component import (
            ApiV1S3ClustersCreateDefaultProductErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_description_error_component import (
            ApiV1S3ClustersCreateDescriptionErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_discovery_enabled_error_component import (
            ApiV1S3ClustersCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_display_name_error_component import (
            ApiV1S3ClustersCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_endpoint_error_component import (
            ApiV1S3ClustersCreateEndpointErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_endpoint_secure_error_component import (
            ApiV1S3ClustersCreateEndpointSecureErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_include_in_cost_statement_error_component import (
            ApiV1S3ClustersCreateIncludeInCostStatementErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_k8s_cluster_error_component import (
            ApiV1S3ClustersCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_kind_error_component import ApiV1S3ClustersCreateKindErrorComponent
        from ..models.api_v1s3_clusters_create_labels_error_component import ApiV1S3ClustersCreateLabelsErrorComponent
        from ..models.api_v1s3_clusters_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1S3ClustersCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_managed_buckets_object_count_error_component import (
            ApiV1S3ClustersCreateManagedBucketsObjectCountErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_managed_buckets_usage_kb_error_component import (
            ApiV1S3ClustersCreateManagedBucketsUsageKbErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_managed_by_content_type_error_component import (
            ApiV1S3ClustersCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_managed_by_object_id_error_component import (
            ApiV1S3ClustersCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_minio_cluster_capacity_usable_bytes_error_component import (
            ApiV1S3ClustersCreateMinioClusterCapacityUsableBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_minio_cluster_usage_bytes_error_component import (
            ApiV1S3ClustersCreateMinioClusterUsageBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_modified_by_user_error_component import (
            ApiV1S3ClustersCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_name_error_component import ApiV1S3ClustersCreateNameErrorComponent
        from ..models.api_v1s3_clusters_create_namespace_error_component import (
            ApiV1S3ClustersCreateNamespaceErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_non_field_errors_error_component import (
            ApiV1S3ClustersCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_platform_dns_record_created_error_component import (
            ApiV1S3ClustersCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_platform_service_error_component import (
            ApiV1S3ClustersCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_provider_error_component import (
            ApiV1S3ClustersCreateProviderErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_provider_id_error_component import (
            ApiV1S3ClustersCreateProviderIdErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_provider_reference_error_component import (
            ApiV1S3ClustersCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_radosgw_buckets_logical_used_bytes_error_component import (
            ApiV1S3ClustersCreateRadosgwBucketsLogicalUsedBytesErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_reconciliation_enabled_error_component import (
            ApiV1S3ClustersCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_region_error_component import ApiV1S3ClustersCreateRegionErrorComponent
        from ..models.api_v1s3_clusters_create_scope_error_component import ApiV1S3ClustersCreateScopeErrorComponent
        from ..models.api_v1s3_clusters_create_sla_availability_error_component import (
            ApiV1S3ClustersCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_sla_target_error_component import (
            ApiV1S3ClustersCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_sla_window_days_error_component import (
            ApiV1S3ClustersCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_slo_availability_error_component import (
            ApiV1S3ClustersCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_slo_target_error_component import (
            ApiV1S3ClustersCreateSloTargetErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_slo_window_days_error_component import (
            ApiV1S3ClustersCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1s3_clusters_create_slug_error_component import ApiV1S3ClustersCreateSlugErrorComponent
        from ..models.api_v1s3_clusters_create_target_availability_error_component import (
            ApiV1S3ClustersCreateTargetAvailabilityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1S3ClustersCreateActiveErrorComponent
                | ApiV1S3ClustersCreateActualAvailabilityErrorComponent
                | ApiV1S3ClustersCreateAdminEndpointErrorComponent
                | ApiV1S3ClustersCreateAdminEndpointSecureErrorComponent
                | ApiV1S3ClustersCreateAliasErrorComponent
                | ApiV1S3ClustersCreateAllowNewBucketsErrorComponent
                | ApiV1S3ClustersCreateAnnotationsErrorComponent
                | ApiV1S3ClustersCreateArchivedAtErrorComponent
                | ApiV1S3ClustersCreateArchivedByErrorComponent
                | ApiV1S3ClustersCreateArchivedErrorComponent
                | ApiV1S3ClustersCreateArchivedReasonErrorComponent
                | ApiV1S3ClustersCreateCephOsdClusterTotalBytesErrorComponent
                | ApiV1S3ClustersCreateClusterConfigErrorComponent
                | ApiV1S3ClustersCreateClusterInfoErrorComponent
                | ApiV1S3ClustersCreateCreatedByComponentErrorComponent
                | ApiV1S3ClustersCreateCreatedByUserErrorComponent
                | ApiV1S3ClustersCreateCredentialErrorComponent
                | ApiV1S3ClustersCreateCriticalityErrorComponent
                | ApiV1S3ClustersCreateDebugModeErrorComponent
                | ApiV1S3ClustersCreateDefaultProductErrorComponent
                | ApiV1S3ClustersCreateDescriptionErrorComponent
                | ApiV1S3ClustersCreateDiscoveryEnabledErrorComponent
                | ApiV1S3ClustersCreateDisplayNameErrorComponent
                | ApiV1S3ClustersCreateEndpointErrorComponent
                | ApiV1S3ClustersCreateEndpointSecureErrorComponent
                | ApiV1S3ClustersCreateIncludeInCostStatementErrorComponent
                | ApiV1S3ClustersCreateK8SClusterErrorComponent
                | ApiV1S3ClustersCreateKindErrorComponent
                | ApiV1S3ClustersCreateLabelsErrorComponent
                | ApiV1S3ClustersCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1S3ClustersCreateManagedBucketsObjectCountErrorComponent
                | ApiV1S3ClustersCreateManagedBucketsUsageKbErrorComponent
                | ApiV1S3ClustersCreateManagedByContentTypeErrorComponent
                | ApiV1S3ClustersCreateManagedByObjectIdErrorComponent
                | ApiV1S3ClustersCreateMinioClusterCapacityUsableBytesErrorComponent
                | ApiV1S3ClustersCreateMinioClusterUsageBytesErrorComponent
                | ApiV1S3ClustersCreateModifiedByUserErrorComponent
                | ApiV1S3ClustersCreateNameErrorComponent
                | ApiV1S3ClustersCreateNamespaceErrorComponent
                | ApiV1S3ClustersCreateNonFieldErrorsErrorComponent
                | ApiV1S3ClustersCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1S3ClustersCreatePlatformServiceErrorComponent
                | ApiV1S3ClustersCreateProviderErrorComponent
                | ApiV1S3ClustersCreateProviderIdErrorComponent
                | ApiV1S3ClustersCreateProviderReferenceErrorComponent
                | ApiV1S3ClustersCreateRadosgwBucketsLogicalUsedBytesErrorComponent
                | ApiV1S3ClustersCreateReconciliationEnabledErrorComponent
                | ApiV1S3ClustersCreateRegionErrorComponent
                | ApiV1S3ClustersCreateScopeErrorComponent
                | ApiV1S3ClustersCreateSlaAvailabilityErrorComponent
                | ApiV1S3ClustersCreateSlaTargetErrorComponent
                | ApiV1S3ClustersCreateSlaWindowDaysErrorComponent
                | ApiV1S3ClustersCreateSloAvailabilityErrorComponent
                | ApiV1S3ClustersCreateSloTargetErrorComponent
                | ApiV1S3ClustersCreateSloWindowDaysErrorComponent
                | ApiV1S3ClustersCreateSlugErrorComponent
                | ApiV1S3ClustersCreateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_0 = (
                        ApiV1S3ClustersCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_1 = (
                        ApiV1S3ClustersCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_2 = (
                        ApiV1S3ClustersCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_3 = (
                        ApiV1S3ClustersCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_4 = (
                        ApiV1S3ClustersCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_5 = (
                        ApiV1S3ClustersCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_6 = (
                        ApiV1S3ClustersCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_7 = (
                        ApiV1S3ClustersCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_8 = (
                        ApiV1S3ClustersCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_9 = (
                        ApiV1S3ClustersCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_10 = (
                        ApiV1S3ClustersCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_11 = (
                        ApiV1S3ClustersCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_12 = (
                        ApiV1S3ClustersCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_13 = (
                        ApiV1S3ClustersCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_14 = (
                        ApiV1S3ClustersCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_15 = (
                        ApiV1S3ClustersCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_16 = (
                        ApiV1S3ClustersCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_17 = (
                        ApiV1S3ClustersCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_18 = (
                        ApiV1S3ClustersCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_19 = (
                        ApiV1S3ClustersCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_20 = (
                        ApiV1S3ClustersCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_21 = (
                        ApiV1S3ClustersCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_22 = (
                        ApiV1S3ClustersCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_23 = (
                        ApiV1S3ClustersCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_24 = (
                        ApiV1S3ClustersCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_25 = (
                        ApiV1S3ClustersCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_26 = (
                        ApiV1S3ClustersCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_27 = (
                        ApiV1S3ClustersCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_28 = (
                        ApiV1S3ClustersCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_29 = (
                        ApiV1S3ClustersCreateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_30 = (
                        ApiV1S3ClustersCreateEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_31 = (
                        ApiV1S3ClustersCreateEndpointSecureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_32 = (
                        ApiV1S3ClustersCreateAdminEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_33 = (
                        ApiV1S3ClustersCreateAdminEndpointSecureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_34 = (
                        ApiV1S3ClustersCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_35 = (
                        ApiV1S3ClustersCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_36 = (
                        ApiV1S3ClustersCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_37 = (
                        ApiV1S3ClustersCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_38 = (
                        ApiV1S3ClustersCreateClusterConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_39 = (
                        ApiV1S3ClustersCreateClusterInfoErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_40 = (
                        ApiV1S3ClustersCreateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_41 = (
                        ApiV1S3ClustersCreateRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_42 = (
                        ApiV1S3ClustersCreateAllowNewBucketsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_43 = (
                        ApiV1S3ClustersCreateIncludeInCostStatementErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_44 = (
                        ApiV1S3ClustersCreateCephOsdClusterTotalBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_45 = (
                        ApiV1S3ClustersCreateRadosgwBucketsLogicalUsedBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_46 = (
                        ApiV1S3ClustersCreateMinioClusterCapacityUsableBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_47 = (
                        ApiV1S3ClustersCreateMinioClusterUsageBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_48 = (
                        ApiV1S3ClustersCreateManagedBucketsUsageKbErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_49 = (
                        ApiV1S3ClustersCreateManagedBucketsObjectCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_50 = (
                        ApiV1S3ClustersCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_51 = (
                        ApiV1S3ClustersCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_52 = (
                        ApiV1S3ClustersCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_53 = (
                        ApiV1S3ClustersCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_54 = (
                        ApiV1S3ClustersCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_create_error_type_55 = (
                        ApiV1S3ClustersCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1s3_clusters_create_error_type_56 = (
                    ApiV1S3ClustersCreateDefaultProductErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1s3_clusters_create_error_type_56

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1s3_clusters_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1s3_clusters_create_validation_error.additional_properties = d
        return api_v1s3_clusters_create_validation_error

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
