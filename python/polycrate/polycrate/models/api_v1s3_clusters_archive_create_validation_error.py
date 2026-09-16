from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1s3_clusters_archive_create_active_error_component import (
        ApiV1S3ClustersArchiveCreateActiveErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_actual_availability_error_component import (
        ApiV1S3ClustersArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_admin_endpoint_error_component import (
        ApiV1S3ClustersArchiveCreateAdminEndpointErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_admin_endpoint_secure_error_component import (
        ApiV1S3ClustersArchiveCreateAdminEndpointSecureErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_alias_error_component import (
        ApiV1S3ClustersArchiveCreateAliasErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_allow_new_buckets_error_component import (
        ApiV1S3ClustersArchiveCreateAllowNewBucketsErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_annotations_error_component import (
        ApiV1S3ClustersArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_archived_at_error_component import (
        ApiV1S3ClustersArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_archived_by_error_component import (
        ApiV1S3ClustersArchiveCreateArchivedByErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_archived_error_component import (
        ApiV1S3ClustersArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_archived_reason_error_component import (
        ApiV1S3ClustersArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_ceph_osd_cluster_total_bytes_error_component import (
        ApiV1S3ClustersArchiveCreateCephOsdClusterTotalBytesErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_cluster_config_error_component import (
        ApiV1S3ClustersArchiveCreateClusterConfigErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_cluster_info_error_component import (
        ApiV1S3ClustersArchiveCreateClusterInfoErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_created_by_component_error_component import (
        ApiV1S3ClustersArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_created_by_user_error_component import (
        ApiV1S3ClustersArchiveCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_credential_error_component import (
        ApiV1S3ClustersArchiveCreateCredentialErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_criticality_error_component import (
        ApiV1S3ClustersArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_debug_mode_error_component import (
        ApiV1S3ClustersArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_default_product_error_component import (
        ApiV1S3ClustersArchiveCreateDefaultProductErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_description_error_component import (
        ApiV1S3ClustersArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_discovery_enabled_error_component import (
        ApiV1S3ClustersArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_display_name_error_component import (
        ApiV1S3ClustersArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_endpoint_error_component import (
        ApiV1S3ClustersArchiveCreateEndpointErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_endpoint_secure_error_component import (
        ApiV1S3ClustersArchiveCreateEndpointSecureErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_include_in_cost_statement_error_component import (
        ApiV1S3ClustersArchiveCreateIncludeInCostStatementErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_k8s_cluster_error_component import (
        ApiV1S3ClustersArchiveCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_kind_error_component import (
        ApiV1S3ClustersArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_labels_error_component import (
        ApiV1S3ClustersArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1S3ClustersArchiveCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_managed_buckets_object_count_error_component import (
        ApiV1S3ClustersArchiveCreateManagedBucketsObjectCountErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_managed_buckets_usage_kb_error_component import (
        ApiV1S3ClustersArchiveCreateManagedBucketsUsageKbErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_managed_by_content_type_error_component import (
        ApiV1S3ClustersArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_managed_by_object_id_error_component import (
        ApiV1S3ClustersArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_minio_cluster_capacity_usable_bytes_error_component import (
        ApiV1S3ClustersArchiveCreateMinioClusterCapacityUsableBytesErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_minio_cluster_usage_bytes_error_component import (
        ApiV1S3ClustersArchiveCreateMinioClusterUsageBytesErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_modified_by_user_error_component import (
        ApiV1S3ClustersArchiveCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_name_error_component import (
        ApiV1S3ClustersArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_namespace_error_component import (
        ApiV1S3ClustersArchiveCreateNamespaceErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_non_field_errors_error_component import (
        ApiV1S3ClustersArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_platform_dns_record_created_error_component import (
        ApiV1S3ClustersArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_platform_service_error_component import (
        ApiV1S3ClustersArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_provider_error_component import (
        ApiV1S3ClustersArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_provider_id_error_component import (
        ApiV1S3ClustersArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_provider_reference_error_component import (
        ApiV1S3ClustersArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_radosgw_buckets_logical_used_bytes_error_component import (
        ApiV1S3ClustersArchiveCreateRadosgwBucketsLogicalUsedBytesErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_reconciliation_enabled_error_component import (
        ApiV1S3ClustersArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_region_error_component import (
        ApiV1S3ClustersArchiveCreateRegionErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_scope_error_component import (
        ApiV1S3ClustersArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_sla_availability_error_component import (
        ApiV1S3ClustersArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_sla_target_error_component import (
        ApiV1S3ClustersArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_sla_window_days_error_component import (
        ApiV1S3ClustersArchiveCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_slo_availability_error_component import (
        ApiV1S3ClustersArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_slo_target_error_component import (
        ApiV1S3ClustersArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_slo_window_days_error_component import (
        ApiV1S3ClustersArchiveCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_slug_error_component import (
        ApiV1S3ClustersArchiveCreateSlugErrorComponent,
    )
    from ..models.api_v1s3_clusters_archive_create_target_availability_error_component import (
        ApiV1S3ClustersArchiveCreateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1S3ClustersArchiveCreateValidationError")


@_attrs_define
class ApiV1S3ClustersArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1S3ClustersArchiveCreateActiveErrorComponent |
            ApiV1S3ClustersArchiveCreateActualAvailabilityErrorComponent |
            ApiV1S3ClustersArchiveCreateAdminEndpointErrorComponent |
            ApiV1S3ClustersArchiveCreateAdminEndpointSecureErrorComponent | ApiV1S3ClustersArchiveCreateAliasErrorComponent
            | ApiV1S3ClustersArchiveCreateAllowNewBucketsErrorComponent |
            ApiV1S3ClustersArchiveCreateAnnotationsErrorComponent | ApiV1S3ClustersArchiveCreateArchivedAtErrorComponent |
            ApiV1S3ClustersArchiveCreateArchivedByErrorComponent | ApiV1S3ClustersArchiveCreateArchivedErrorComponent |
            ApiV1S3ClustersArchiveCreateArchivedReasonErrorComponent |
            ApiV1S3ClustersArchiveCreateCephOsdClusterTotalBytesErrorComponent |
            ApiV1S3ClustersArchiveCreateClusterConfigErrorComponent | ApiV1S3ClustersArchiveCreateClusterInfoErrorComponent
            | ApiV1S3ClustersArchiveCreateCreatedByComponentErrorComponent |
            ApiV1S3ClustersArchiveCreateCreatedByUserErrorComponent | ApiV1S3ClustersArchiveCreateCredentialErrorComponent |
            ApiV1S3ClustersArchiveCreateCriticalityErrorComponent | ApiV1S3ClustersArchiveCreateDebugModeErrorComponent |
            ApiV1S3ClustersArchiveCreateDefaultProductErrorComponent | ApiV1S3ClustersArchiveCreateDescriptionErrorComponent
            | ApiV1S3ClustersArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1S3ClustersArchiveCreateDisplayNameErrorComponent | ApiV1S3ClustersArchiveCreateEndpointErrorComponent |
            ApiV1S3ClustersArchiveCreateEndpointSecureErrorComponent |
            ApiV1S3ClustersArchiveCreateIncludeInCostStatementErrorComponent |
            ApiV1S3ClustersArchiveCreateK8SClusterErrorComponent | ApiV1S3ClustersArchiveCreateKindErrorComponent |
            ApiV1S3ClustersArchiveCreateLabelsErrorComponent |
            ApiV1S3ClustersArchiveCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1S3ClustersArchiveCreateManagedBucketsObjectCountErrorComponent |
            ApiV1S3ClustersArchiveCreateManagedBucketsUsageKbErrorComponent |
            ApiV1S3ClustersArchiveCreateManagedByContentTypeErrorComponent |
            ApiV1S3ClustersArchiveCreateManagedByObjectIdErrorComponent |
            ApiV1S3ClustersArchiveCreateMinioClusterCapacityUsableBytesErrorComponent |
            ApiV1S3ClustersArchiveCreateMinioClusterUsageBytesErrorComponent |
            ApiV1S3ClustersArchiveCreateModifiedByUserErrorComponent | ApiV1S3ClustersArchiveCreateNameErrorComponent |
            ApiV1S3ClustersArchiveCreateNamespaceErrorComponent | ApiV1S3ClustersArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1S3ClustersArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1S3ClustersArchiveCreatePlatformServiceErrorComponent | ApiV1S3ClustersArchiveCreateProviderErrorComponent |
            ApiV1S3ClustersArchiveCreateProviderIdErrorComponent |
            ApiV1S3ClustersArchiveCreateProviderReferenceErrorComponent |
            ApiV1S3ClustersArchiveCreateRadosgwBucketsLogicalUsedBytesErrorComponent |
            ApiV1S3ClustersArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1S3ClustersArchiveCreateRegionErrorComponent | ApiV1S3ClustersArchiveCreateScopeErrorComponent |
            ApiV1S3ClustersArchiveCreateSlaAvailabilityErrorComponent | ApiV1S3ClustersArchiveCreateSlaTargetErrorComponent
            | ApiV1S3ClustersArchiveCreateSlaWindowDaysErrorComponent |
            ApiV1S3ClustersArchiveCreateSloAvailabilityErrorComponent | ApiV1S3ClustersArchiveCreateSloTargetErrorComponent
            | ApiV1S3ClustersArchiveCreateSloWindowDaysErrorComponent | ApiV1S3ClustersArchiveCreateSlugErrorComponent |
            ApiV1S3ClustersArchiveCreateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1S3ClustersArchiveCreateActiveErrorComponent
        | ApiV1S3ClustersArchiveCreateActualAvailabilityErrorComponent
        | ApiV1S3ClustersArchiveCreateAdminEndpointErrorComponent
        | ApiV1S3ClustersArchiveCreateAdminEndpointSecureErrorComponent
        | ApiV1S3ClustersArchiveCreateAliasErrorComponent
        | ApiV1S3ClustersArchiveCreateAllowNewBucketsErrorComponent
        | ApiV1S3ClustersArchiveCreateAnnotationsErrorComponent
        | ApiV1S3ClustersArchiveCreateArchivedAtErrorComponent
        | ApiV1S3ClustersArchiveCreateArchivedByErrorComponent
        | ApiV1S3ClustersArchiveCreateArchivedErrorComponent
        | ApiV1S3ClustersArchiveCreateArchivedReasonErrorComponent
        | ApiV1S3ClustersArchiveCreateCephOsdClusterTotalBytesErrorComponent
        | ApiV1S3ClustersArchiveCreateClusterConfigErrorComponent
        | ApiV1S3ClustersArchiveCreateClusterInfoErrorComponent
        | ApiV1S3ClustersArchiveCreateCreatedByComponentErrorComponent
        | ApiV1S3ClustersArchiveCreateCreatedByUserErrorComponent
        | ApiV1S3ClustersArchiveCreateCredentialErrorComponent
        | ApiV1S3ClustersArchiveCreateCriticalityErrorComponent
        | ApiV1S3ClustersArchiveCreateDebugModeErrorComponent
        | ApiV1S3ClustersArchiveCreateDefaultProductErrorComponent
        | ApiV1S3ClustersArchiveCreateDescriptionErrorComponent
        | ApiV1S3ClustersArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1S3ClustersArchiveCreateDisplayNameErrorComponent
        | ApiV1S3ClustersArchiveCreateEndpointErrorComponent
        | ApiV1S3ClustersArchiveCreateEndpointSecureErrorComponent
        | ApiV1S3ClustersArchiveCreateIncludeInCostStatementErrorComponent
        | ApiV1S3ClustersArchiveCreateK8SClusterErrorComponent
        | ApiV1S3ClustersArchiveCreateKindErrorComponent
        | ApiV1S3ClustersArchiveCreateLabelsErrorComponent
        | ApiV1S3ClustersArchiveCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1S3ClustersArchiveCreateManagedBucketsObjectCountErrorComponent
        | ApiV1S3ClustersArchiveCreateManagedBucketsUsageKbErrorComponent
        | ApiV1S3ClustersArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1S3ClustersArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1S3ClustersArchiveCreateMinioClusterCapacityUsableBytesErrorComponent
        | ApiV1S3ClustersArchiveCreateMinioClusterUsageBytesErrorComponent
        | ApiV1S3ClustersArchiveCreateModifiedByUserErrorComponent
        | ApiV1S3ClustersArchiveCreateNameErrorComponent
        | ApiV1S3ClustersArchiveCreateNamespaceErrorComponent
        | ApiV1S3ClustersArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1S3ClustersArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1S3ClustersArchiveCreatePlatformServiceErrorComponent
        | ApiV1S3ClustersArchiveCreateProviderErrorComponent
        | ApiV1S3ClustersArchiveCreateProviderIdErrorComponent
        | ApiV1S3ClustersArchiveCreateProviderReferenceErrorComponent
        | ApiV1S3ClustersArchiveCreateRadosgwBucketsLogicalUsedBytesErrorComponent
        | ApiV1S3ClustersArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1S3ClustersArchiveCreateRegionErrorComponent
        | ApiV1S3ClustersArchiveCreateScopeErrorComponent
        | ApiV1S3ClustersArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1S3ClustersArchiveCreateSlaTargetErrorComponent
        | ApiV1S3ClustersArchiveCreateSlaWindowDaysErrorComponent
        | ApiV1S3ClustersArchiveCreateSloAvailabilityErrorComponent
        | ApiV1S3ClustersArchiveCreateSloTargetErrorComponent
        | ApiV1S3ClustersArchiveCreateSloWindowDaysErrorComponent
        | ApiV1S3ClustersArchiveCreateSlugErrorComponent
        | ApiV1S3ClustersArchiveCreateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1s3_clusters_archive_create_active_error_component import (
            ApiV1S3ClustersArchiveCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_actual_availability_error_component import (
            ApiV1S3ClustersArchiveCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_admin_endpoint_error_component import (
            ApiV1S3ClustersArchiveCreateAdminEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_admin_endpoint_secure_error_component import (
            ApiV1S3ClustersArchiveCreateAdminEndpointSecureErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_alias_error_component import (
            ApiV1S3ClustersArchiveCreateAliasErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_allow_new_buckets_error_component import (
            ApiV1S3ClustersArchiveCreateAllowNewBucketsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_annotations_error_component import (
            ApiV1S3ClustersArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_archived_at_error_component import (
            ApiV1S3ClustersArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_archived_by_error_component import (
            ApiV1S3ClustersArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_archived_error_component import (
            ApiV1S3ClustersArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_archived_reason_error_component import (
            ApiV1S3ClustersArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_ceph_osd_cluster_total_bytes_error_component import (
            ApiV1S3ClustersArchiveCreateCephOsdClusterTotalBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_cluster_config_error_component import (
            ApiV1S3ClustersArchiveCreateClusterConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_cluster_info_error_component import (
            ApiV1S3ClustersArchiveCreateClusterInfoErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_created_by_component_error_component import (
            ApiV1S3ClustersArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_created_by_user_error_component import (
            ApiV1S3ClustersArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_credential_error_component import (
            ApiV1S3ClustersArchiveCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_criticality_error_component import (
            ApiV1S3ClustersArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_debug_mode_error_component import (
            ApiV1S3ClustersArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_description_error_component import (
            ApiV1S3ClustersArchiveCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_discovery_enabled_error_component import (
            ApiV1S3ClustersArchiveCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_display_name_error_component import (
            ApiV1S3ClustersArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_endpoint_error_component import (
            ApiV1S3ClustersArchiveCreateEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_endpoint_secure_error_component import (
            ApiV1S3ClustersArchiveCreateEndpointSecureErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_include_in_cost_statement_error_component import (
            ApiV1S3ClustersArchiveCreateIncludeInCostStatementErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_k8s_cluster_error_component import (
            ApiV1S3ClustersArchiveCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_kind_error_component import (
            ApiV1S3ClustersArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_labels_error_component import (
            ApiV1S3ClustersArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1S3ClustersArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_managed_buckets_object_count_error_component import (
            ApiV1S3ClustersArchiveCreateManagedBucketsObjectCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_managed_buckets_usage_kb_error_component import (
            ApiV1S3ClustersArchiveCreateManagedBucketsUsageKbErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_managed_by_content_type_error_component import (
            ApiV1S3ClustersArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_managed_by_object_id_error_component import (
            ApiV1S3ClustersArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_minio_cluster_capacity_usable_bytes_error_component import (
            ApiV1S3ClustersArchiveCreateMinioClusterCapacityUsableBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_minio_cluster_usage_bytes_error_component import (
            ApiV1S3ClustersArchiveCreateMinioClusterUsageBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_modified_by_user_error_component import (
            ApiV1S3ClustersArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_name_error_component import (
            ApiV1S3ClustersArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_namespace_error_component import (
            ApiV1S3ClustersArchiveCreateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_non_field_errors_error_component import (
            ApiV1S3ClustersArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_platform_dns_record_created_error_component import (
            ApiV1S3ClustersArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_platform_service_error_component import (
            ApiV1S3ClustersArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_provider_error_component import (
            ApiV1S3ClustersArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_provider_id_error_component import (
            ApiV1S3ClustersArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_provider_reference_error_component import (
            ApiV1S3ClustersArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_radosgw_buckets_logical_used_bytes_error_component import (
            ApiV1S3ClustersArchiveCreateRadosgwBucketsLogicalUsedBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_reconciliation_enabled_error_component import (
            ApiV1S3ClustersArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_region_error_component import (
            ApiV1S3ClustersArchiveCreateRegionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_scope_error_component import (
            ApiV1S3ClustersArchiveCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_sla_availability_error_component import (
            ApiV1S3ClustersArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_sla_target_error_component import (
            ApiV1S3ClustersArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_sla_window_days_error_component import (
            ApiV1S3ClustersArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_slo_availability_error_component import (
            ApiV1S3ClustersArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_slo_target_error_component import (
            ApiV1S3ClustersArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_slo_window_days_error_component import (
            ApiV1S3ClustersArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_slug_error_component import (
            ApiV1S3ClustersArchiveCreateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_target_availability_error_component import (
            ApiV1S3ClustersArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1S3ClustersArchiveCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateEndpointSecureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateAdminEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateAdminEndpointSecureErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateClusterConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateClusterInfoErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateAllowNewBucketsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateIncludeInCostStatementErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateCephOsdClusterTotalBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateRadosgwBucketsLogicalUsedBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1S3ClustersArchiveCreateMinioClusterCapacityUsableBytesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateMinioClusterUsageBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateManagedBucketsUsageKbErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateManagedBucketsObjectCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1S3ClustersArchiveCreateK8SClusterErrorComponent):
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
        from ..models.api_v1s3_clusters_archive_create_active_error_component import (
            ApiV1S3ClustersArchiveCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_actual_availability_error_component import (
            ApiV1S3ClustersArchiveCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_admin_endpoint_error_component import (
            ApiV1S3ClustersArchiveCreateAdminEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_admin_endpoint_secure_error_component import (
            ApiV1S3ClustersArchiveCreateAdminEndpointSecureErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_alias_error_component import (
            ApiV1S3ClustersArchiveCreateAliasErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_allow_new_buckets_error_component import (
            ApiV1S3ClustersArchiveCreateAllowNewBucketsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_annotations_error_component import (
            ApiV1S3ClustersArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_archived_at_error_component import (
            ApiV1S3ClustersArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_archived_by_error_component import (
            ApiV1S3ClustersArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_archived_error_component import (
            ApiV1S3ClustersArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_archived_reason_error_component import (
            ApiV1S3ClustersArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_ceph_osd_cluster_total_bytes_error_component import (
            ApiV1S3ClustersArchiveCreateCephOsdClusterTotalBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_cluster_config_error_component import (
            ApiV1S3ClustersArchiveCreateClusterConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_cluster_info_error_component import (
            ApiV1S3ClustersArchiveCreateClusterInfoErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_created_by_component_error_component import (
            ApiV1S3ClustersArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_created_by_user_error_component import (
            ApiV1S3ClustersArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_credential_error_component import (
            ApiV1S3ClustersArchiveCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_criticality_error_component import (
            ApiV1S3ClustersArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_debug_mode_error_component import (
            ApiV1S3ClustersArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_default_product_error_component import (
            ApiV1S3ClustersArchiveCreateDefaultProductErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_description_error_component import (
            ApiV1S3ClustersArchiveCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_discovery_enabled_error_component import (
            ApiV1S3ClustersArchiveCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_display_name_error_component import (
            ApiV1S3ClustersArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_endpoint_error_component import (
            ApiV1S3ClustersArchiveCreateEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_endpoint_secure_error_component import (
            ApiV1S3ClustersArchiveCreateEndpointSecureErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_include_in_cost_statement_error_component import (
            ApiV1S3ClustersArchiveCreateIncludeInCostStatementErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_k8s_cluster_error_component import (
            ApiV1S3ClustersArchiveCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_kind_error_component import (
            ApiV1S3ClustersArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_labels_error_component import (
            ApiV1S3ClustersArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1S3ClustersArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_managed_buckets_object_count_error_component import (
            ApiV1S3ClustersArchiveCreateManagedBucketsObjectCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_managed_buckets_usage_kb_error_component import (
            ApiV1S3ClustersArchiveCreateManagedBucketsUsageKbErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_managed_by_content_type_error_component import (
            ApiV1S3ClustersArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_managed_by_object_id_error_component import (
            ApiV1S3ClustersArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_minio_cluster_capacity_usable_bytes_error_component import (
            ApiV1S3ClustersArchiveCreateMinioClusterCapacityUsableBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_minio_cluster_usage_bytes_error_component import (
            ApiV1S3ClustersArchiveCreateMinioClusterUsageBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_modified_by_user_error_component import (
            ApiV1S3ClustersArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_name_error_component import (
            ApiV1S3ClustersArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_namespace_error_component import (
            ApiV1S3ClustersArchiveCreateNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_non_field_errors_error_component import (
            ApiV1S3ClustersArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_platform_dns_record_created_error_component import (
            ApiV1S3ClustersArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_platform_service_error_component import (
            ApiV1S3ClustersArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_provider_error_component import (
            ApiV1S3ClustersArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_provider_id_error_component import (
            ApiV1S3ClustersArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_provider_reference_error_component import (
            ApiV1S3ClustersArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_radosgw_buckets_logical_used_bytes_error_component import (
            ApiV1S3ClustersArchiveCreateRadosgwBucketsLogicalUsedBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_reconciliation_enabled_error_component import (
            ApiV1S3ClustersArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_region_error_component import (
            ApiV1S3ClustersArchiveCreateRegionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_scope_error_component import (
            ApiV1S3ClustersArchiveCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_sla_availability_error_component import (
            ApiV1S3ClustersArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_sla_target_error_component import (
            ApiV1S3ClustersArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_sla_window_days_error_component import (
            ApiV1S3ClustersArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_slo_availability_error_component import (
            ApiV1S3ClustersArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_slo_target_error_component import (
            ApiV1S3ClustersArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_slo_window_days_error_component import (
            ApiV1S3ClustersArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_slug_error_component import (
            ApiV1S3ClustersArchiveCreateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1s3_clusters_archive_create_target_availability_error_component import (
            ApiV1S3ClustersArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1S3ClustersArchiveCreateActiveErrorComponent
                | ApiV1S3ClustersArchiveCreateActualAvailabilityErrorComponent
                | ApiV1S3ClustersArchiveCreateAdminEndpointErrorComponent
                | ApiV1S3ClustersArchiveCreateAdminEndpointSecureErrorComponent
                | ApiV1S3ClustersArchiveCreateAliasErrorComponent
                | ApiV1S3ClustersArchiveCreateAllowNewBucketsErrorComponent
                | ApiV1S3ClustersArchiveCreateAnnotationsErrorComponent
                | ApiV1S3ClustersArchiveCreateArchivedAtErrorComponent
                | ApiV1S3ClustersArchiveCreateArchivedByErrorComponent
                | ApiV1S3ClustersArchiveCreateArchivedErrorComponent
                | ApiV1S3ClustersArchiveCreateArchivedReasonErrorComponent
                | ApiV1S3ClustersArchiveCreateCephOsdClusterTotalBytesErrorComponent
                | ApiV1S3ClustersArchiveCreateClusterConfigErrorComponent
                | ApiV1S3ClustersArchiveCreateClusterInfoErrorComponent
                | ApiV1S3ClustersArchiveCreateCreatedByComponentErrorComponent
                | ApiV1S3ClustersArchiveCreateCreatedByUserErrorComponent
                | ApiV1S3ClustersArchiveCreateCredentialErrorComponent
                | ApiV1S3ClustersArchiveCreateCriticalityErrorComponent
                | ApiV1S3ClustersArchiveCreateDebugModeErrorComponent
                | ApiV1S3ClustersArchiveCreateDefaultProductErrorComponent
                | ApiV1S3ClustersArchiveCreateDescriptionErrorComponent
                | ApiV1S3ClustersArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1S3ClustersArchiveCreateDisplayNameErrorComponent
                | ApiV1S3ClustersArchiveCreateEndpointErrorComponent
                | ApiV1S3ClustersArchiveCreateEndpointSecureErrorComponent
                | ApiV1S3ClustersArchiveCreateIncludeInCostStatementErrorComponent
                | ApiV1S3ClustersArchiveCreateK8SClusterErrorComponent
                | ApiV1S3ClustersArchiveCreateKindErrorComponent
                | ApiV1S3ClustersArchiveCreateLabelsErrorComponent
                | ApiV1S3ClustersArchiveCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1S3ClustersArchiveCreateManagedBucketsObjectCountErrorComponent
                | ApiV1S3ClustersArchiveCreateManagedBucketsUsageKbErrorComponent
                | ApiV1S3ClustersArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1S3ClustersArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1S3ClustersArchiveCreateMinioClusterCapacityUsableBytesErrorComponent
                | ApiV1S3ClustersArchiveCreateMinioClusterUsageBytesErrorComponent
                | ApiV1S3ClustersArchiveCreateModifiedByUserErrorComponent
                | ApiV1S3ClustersArchiveCreateNameErrorComponent
                | ApiV1S3ClustersArchiveCreateNamespaceErrorComponent
                | ApiV1S3ClustersArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1S3ClustersArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1S3ClustersArchiveCreatePlatformServiceErrorComponent
                | ApiV1S3ClustersArchiveCreateProviderErrorComponent
                | ApiV1S3ClustersArchiveCreateProviderIdErrorComponent
                | ApiV1S3ClustersArchiveCreateProviderReferenceErrorComponent
                | ApiV1S3ClustersArchiveCreateRadosgwBucketsLogicalUsedBytesErrorComponent
                | ApiV1S3ClustersArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1S3ClustersArchiveCreateRegionErrorComponent
                | ApiV1S3ClustersArchiveCreateScopeErrorComponent
                | ApiV1S3ClustersArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1S3ClustersArchiveCreateSlaTargetErrorComponent
                | ApiV1S3ClustersArchiveCreateSlaWindowDaysErrorComponent
                | ApiV1S3ClustersArchiveCreateSloAvailabilityErrorComponent
                | ApiV1S3ClustersArchiveCreateSloTargetErrorComponent
                | ApiV1S3ClustersArchiveCreateSloWindowDaysErrorComponent
                | ApiV1S3ClustersArchiveCreateSlugErrorComponent
                | ApiV1S3ClustersArchiveCreateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_0 = (
                        ApiV1S3ClustersArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_1 = (
                        ApiV1S3ClustersArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_2 = (
                        ApiV1S3ClustersArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_3 = (
                        ApiV1S3ClustersArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_4 = (
                        ApiV1S3ClustersArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_5 = (
                        ApiV1S3ClustersArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_6 = (
                        ApiV1S3ClustersArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_7 = (
                        ApiV1S3ClustersArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_8 = (
                        ApiV1S3ClustersArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_9 = (
                        ApiV1S3ClustersArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_10 = (
                        ApiV1S3ClustersArchiveCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_11 = (
                        ApiV1S3ClustersArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_12 = (
                        ApiV1S3ClustersArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_13 = (
                        ApiV1S3ClustersArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_14 = (
                        ApiV1S3ClustersArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_15 = (
                        ApiV1S3ClustersArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_16 = (
                        ApiV1S3ClustersArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_17 = (
                        ApiV1S3ClustersArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_18 = (
                        ApiV1S3ClustersArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_19 = (
                        ApiV1S3ClustersArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_20 = (
                        ApiV1S3ClustersArchiveCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_21 = (
                        ApiV1S3ClustersArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_22 = (
                        ApiV1S3ClustersArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_23 = (
                        ApiV1S3ClustersArchiveCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_24 = (
                        ApiV1S3ClustersArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_25 = (
                        ApiV1S3ClustersArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_26 = (
                        ApiV1S3ClustersArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_27 = (
                        ApiV1S3ClustersArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_28 = (
                        ApiV1S3ClustersArchiveCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_29 = (
                        ApiV1S3ClustersArchiveCreateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_30 = (
                        ApiV1S3ClustersArchiveCreateEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_31 = (
                        ApiV1S3ClustersArchiveCreateEndpointSecureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_32 = (
                        ApiV1S3ClustersArchiveCreateAdminEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_33 = (
                        ApiV1S3ClustersArchiveCreateAdminEndpointSecureErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_34 = (
                        ApiV1S3ClustersArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_35 = (
                        ApiV1S3ClustersArchiveCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_36 = (
                        ApiV1S3ClustersArchiveCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_37 = (
                        ApiV1S3ClustersArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_38 = (
                        ApiV1S3ClustersArchiveCreateClusterConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_39 = (
                        ApiV1S3ClustersArchiveCreateClusterInfoErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_40 = (
                        ApiV1S3ClustersArchiveCreateNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_41 = (
                        ApiV1S3ClustersArchiveCreateRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_42 = (
                        ApiV1S3ClustersArchiveCreateAllowNewBucketsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_43 = (
                        ApiV1S3ClustersArchiveCreateIncludeInCostStatementErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_44 = (
                        ApiV1S3ClustersArchiveCreateCephOsdClusterTotalBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_45 = (
                        ApiV1S3ClustersArchiveCreateRadosgwBucketsLogicalUsedBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_46 = (
                        ApiV1S3ClustersArchiveCreateMinioClusterCapacityUsableBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_47 = (
                        ApiV1S3ClustersArchiveCreateMinioClusterUsageBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_48 = (
                        ApiV1S3ClustersArchiveCreateManagedBucketsUsageKbErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_49 = (
                        ApiV1S3ClustersArchiveCreateManagedBucketsObjectCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_50 = (
                        ApiV1S3ClustersArchiveCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_51 = (
                        ApiV1S3ClustersArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_52 = (
                        ApiV1S3ClustersArchiveCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_53 = (
                        ApiV1S3ClustersArchiveCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_54 = (
                        ApiV1S3ClustersArchiveCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1s3_clusters_archive_create_error_type_55 = (
                        ApiV1S3ClustersArchiveCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1s3_clusters_archive_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1s3_clusters_archive_create_error_type_56 = (
                    ApiV1S3ClustersArchiveCreateDefaultProductErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1s3_clusters_archive_create_error_type_56

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1s3_clusters_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1s3_clusters_archive_create_validation_error.additional_properties = d
        return api_v1s3_clusters_archive_create_validation_error

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
