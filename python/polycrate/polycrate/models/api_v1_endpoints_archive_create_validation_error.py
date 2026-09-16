from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_endpoints_archive_create_actual_availability_error_component import (
        ApiV1EndpointsArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_annotations_error_component import (
        ApiV1EndpointsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_archived_at_error_component import (
        ApiV1EndpointsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_archived_by_error_component import (
        ApiV1EndpointsArchiveCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_archived_error_component import (
        ApiV1EndpointsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_archived_reason_error_component import (
        ApiV1EndpointsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_check_result_retention_days_error_component import (
        ApiV1EndpointsArchiveCreateCheckResultRetentionDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_check_results_error_component import (
        ApiV1EndpointsArchiveCreateCheckResultsErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_created_by_component_error_component import (
        ApiV1EndpointsArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_created_by_user_error_component import (
        ApiV1EndpointsArchiveCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_criticality_error_component import (
        ApiV1EndpointsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_debug_mode_error_component import (
        ApiV1EndpointsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_discovery_enabled_error_component import (
        ApiV1EndpointsArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_display_name_error_component import (
        ApiV1EndpointsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_do_not_monitor_error_component import (
        ApiV1EndpointsArchiveCreateDoNotMonitorErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_k8s_app_error_component import (
        ApiV1EndpointsArchiveCreateK8SAppErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_k8s_cluster_error_component import (
        ApiV1EndpointsArchiveCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_kind_error_component import (
        ApiV1EndpointsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_labels_error_component import (
        ApiV1EndpointsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_last_agent_metrics_error_component import (
        ApiV1EndpointsArchiveCreateLastAgentMetricsErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1EndpointsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_loadbalancer_instance_error_component import (
        ApiV1EndpointsArchiveCreateLoadbalancerInstanceErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_managed_by_content_type_error_component import (
        ApiV1EndpointsArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_managed_by_object_id_error_component import (
        ApiV1EndpointsArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_max_agents_per_endpoint_error_component import (
        ApiV1EndpointsArchiveCreateMaxAgentsPerEndpointErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_modified_by_user_error_component import (
        ApiV1EndpointsArchiveCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_name_error_component import (
        ApiV1EndpointsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_non_field_errors_error_component import (
        ApiV1EndpointsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_organization_id_error_component import (
        ApiV1EndpointsArchiveCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_platform_dns_record_created_error_component import (
        ApiV1EndpointsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_platform_service_error_component import (
        ApiV1EndpointsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_pop_endpoint_error_component import (
        ApiV1EndpointsArchiveCreatePopEndpointErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_provider_error_component import (
        ApiV1EndpointsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_provider_id_error_component import (
        ApiV1EndpointsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_provider_reference_error_component import (
        ApiV1EndpointsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_reconciliation_enabled_error_component import (
        ApiV1EndpointsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_region_error_component import (
        ApiV1EndpointsArchiveCreateRegionErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_remote_address_error_component import (
        ApiV1EndpointsArchiveCreateRemoteAddressErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_remote_port_error_component import (
        ApiV1EndpointsArchiveCreateRemotePortErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_resolved_ip_error_component import (
        ApiV1EndpointsArchiveCreateResolvedIpErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_s3_cluster_error_component import (
        ApiV1EndpointsArchiveCreateS3ClusterErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_scope_error_component import (
        ApiV1EndpointsArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_sla_availability_error_component import (
        ApiV1EndpointsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_sla_target_error_component import (
        ApiV1EndpointsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_sla_window_days_error_component import (
        ApiV1EndpointsArchiveCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_slo_availability_error_component import (
        ApiV1EndpointsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_slo_target_error_component import (
        ApiV1EndpointsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_slo_window_days_error_component import (
        ApiV1EndpointsArchiveCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_spec_error_component import (
        ApiV1EndpointsArchiveCreateSpecErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_target_availability_error_component import (
        ApiV1EndpointsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_archive_create_workspace_id_error_component import (
        ApiV1EndpointsArchiveCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1EndpointsArchiveCreateValidationError")


@_attrs_define
class ApiV1EndpointsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1EndpointsArchiveCreateActualAvailabilityErrorComponent |
            ApiV1EndpointsArchiveCreateAnnotationsErrorComponent | ApiV1EndpointsArchiveCreateArchivedAtErrorComponent |
            ApiV1EndpointsArchiveCreateArchivedByErrorComponent | ApiV1EndpointsArchiveCreateArchivedErrorComponent |
            ApiV1EndpointsArchiveCreateArchivedReasonErrorComponent |
            ApiV1EndpointsArchiveCreateCheckResultRetentionDaysErrorComponent |
            ApiV1EndpointsArchiveCreateCheckResultsErrorComponent |
            ApiV1EndpointsArchiveCreateCreatedByComponentErrorComponent |
            ApiV1EndpointsArchiveCreateCreatedByUserErrorComponent | ApiV1EndpointsArchiveCreateCriticalityErrorComponent |
            ApiV1EndpointsArchiveCreateDebugModeErrorComponent | ApiV1EndpointsArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1EndpointsArchiveCreateDisplayNameErrorComponent | ApiV1EndpointsArchiveCreateDoNotMonitorErrorComponent |
            ApiV1EndpointsArchiveCreateK8SAppErrorComponent | ApiV1EndpointsArchiveCreateK8SClusterErrorComponent |
            ApiV1EndpointsArchiveCreateKindErrorComponent | ApiV1EndpointsArchiveCreateLabelsErrorComponent |
            ApiV1EndpointsArchiveCreateLastAgentMetricsErrorComponent |
            ApiV1EndpointsArchiveCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1EndpointsArchiveCreateLoadbalancerInstanceErrorComponent |
            ApiV1EndpointsArchiveCreateManagedByContentTypeErrorComponent |
            ApiV1EndpointsArchiveCreateManagedByObjectIdErrorComponent |
            ApiV1EndpointsArchiveCreateMaxAgentsPerEndpointErrorComponent |
            ApiV1EndpointsArchiveCreateModifiedByUserErrorComponent | ApiV1EndpointsArchiveCreateNameErrorComponent |
            ApiV1EndpointsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1EndpointsArchiveCreateOrganizationIdErrorComponent |
            ApiV1EndpointsArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1EndpointsArchiveCreatePlatformServiceErrorComponent | ApiV1EndpointsArchiveCreatePopEndpointErrorComponent
            | ApiV1EndpointsArchiveCreateProviderErrorComponent | ApiV1EndpointsArchiveCreateProviderIdErrorComponent |
            ApiV1EndpointsArchiveCreateProviderReferenceErrorComponent |
            ApiV1EndpointsArchiveCreateReconciliationEnabledErrorComponent | ApiV1EndpointsArchiveCreateRegionErrorComponent
            | ApiV1EndpointsArchiveCreateRemoteAddressErrorComponent | ApiV1EndpointsArchiveCreateRemotePortErrorComponent |
            ApiV1EndpointsArchiveCreateResolvedIpErrorComponent | ApiV1EndpointsArchiveCreateS3ClusterErrorComponent |
            ApiV1EndpointsArchiveCreateScopeErrorComponent | ApiV1EndpointsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1EndpointsArchiveCreateSlaTargetErrorComponent | ApiV1EndpointsArchiveCreateSlaWindowDaysErrorComponent |
            ApiV1EndpointsArchiveCreateSloAvailabilityErrorComponent | ApiV1EndpointsArchiveCreateSloTargetErrorComponent |
            ApiV1EndpointsArchiveCreateSloWindowDaysErrorComponent | ApiV1EndpointsArchiveCreateSpecErrorComponent |
            ApiV1EndpointsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1EndpointsArchiveCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1EndpointsArchiveCreateActualAvailabilityErrorComponent
        | ApiV1EndpointsArchiveCreateAnnotationsErrorComponent
        | ApiV1EndpointsArchiveCreateArchivedAtErrorComponent
        | ApiV1EndpointsArchiveCreateArchivedByErrorComponent
        | ApiV1EndpointsArchiveCreateArchivedErrorComponent
        | ApiV1EndpointsArchiveCreateArchivedReasonErrorComponent
        | ApiV1EndpointsArchiveCreateCheckResultRetentionDaysErrorComponent
        | ApiV1EndpointsArchiveCreateCheckResultsErrorComponent
        | ApiV1EndpointsArchiveCreateCreatedByComponentErrorComponent
        | ApiV1EndpointsArchiveCreateCreatedByUserErrorComponent
        | ApiV1EndpointsArchiveCreateCriticalityErrorComponent
        | ApiV1EndpointsArchiveCreateDebugModeErrorComponent
        | ApiV1EndpointsArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1EndpointsArchiveCreateDisplayNameErrorComponent
        | ApiV1EndpointsArchiveCreateDoNotMonitorErrorComponent
        | ApiV1EndpointsArchiveCreateK8SAppErrorComponent
        | ApiV1EndpointsArchiveCreateK8SClusterErrorComponent
        | ApiV1EndpointsArchiveCreateKindErrorComponent
        | ApiV1EndpointsArchiveCreateLabelsErrorComponent
        | ApiV1EndpointsArchiveCreateLastAgentMetricsErrorComponent
        | ApiV1EndpointsArchiveCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1EndpointsArchiveCreateLoadbalancerInstanceErrorComponent
        | ApiV1EndpointsArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1EndpointsArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1EndpointsArchiveCreateMaxAgentsPerEndpointErrorComponent
        | ApiV1EndpointsArchiveCreateModifiedByUserErrorComponent
        | ApiV1EndpointsArchiveCreateNameErrorComponent
        | ApiV1EndpointsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1EndpointsArchiveCreateOrganizationIdErrorComponent
        | ApiV1EndpointsArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1EndpointsArchiveCreatePlatformServiceErrorComponent
        | ApiV1EndpointsArchiveCreatePopEndpointErrorComponent
        | ApiV1EndpointsArchiveCreateProviderErrorComponent
        | ApiV1EndpointsArchiveCreateProviderIdErrorComponent
        | ApiV1EndpointsArchiveCreateProviderReferenceErrorComponent
        | ApiV1EndpointsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1EndpointsArchiveCreateRegionErrorComponent
        | ApiV1EndpointsArchiveCreateRemoteAddressErrorComponent
        | ApiV1EndpointsArchiveCreateRemotePortErrorComponent
        | ApiV1EndpointsArchiveCreateResolvedIpErrorComponent
        | ApiV1EndpointsArchiveCreateS3ClusterErrorComponent
        | ApiV1EndpointsArchiveCreateScopeErrorComponent
        | ApiV1EndpointsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1EndpointsArchiveCreateSlaTargetErrorComponent
        | ApiV1EndpointsArchiveCreateSlaWindowDaysErrorComponent
        | ApiV1EndpointsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1EndpointsArchiveCreateSloTargetErrorComponent
        | ApiV1EndpointsArchiveCreateSloWindowDaysErrorComponent
        | ApiV1EndpointsArchiveCreateSpecErrorComponent
        | ApiV1EndpointsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1EndpointsArchiveCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_endpoints_archive_create_actual_availability_error_component import (
            ApiV1EndpointsArchiveCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_annotations_error_component import (
            ApiV1EndpointsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_archived_at_error_component import (
            ApiV1EndpointsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_archived_by_error_component import (
            ApiV1EndpointsArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_archived_error_component import (
            ApiV1EndpointsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_archived_reason_error_component import (
            ApiV1EndpointsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_check_result_retention_days_error_component import (
            ApiV1EndpointsArchiveCreateCheckResultRetentionDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_check_results_error_component import (
            ApiV1EndpointsArchiveCreateCheckResultsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_created_by_component_error_component import (
            ApiV1EndpointsArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_created_by_user_error_component import (
            ApiV1EndpointsArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_criticality_error_component import (
            ApiV1EndpointsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_debug_mode_error_component import (
            ApiV1EndpointsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_discovery_enabled_error_component import (
            ApiV1EndpointsArchiveCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_display_name_error_component import (
            ApiV1EndpointsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_do_not_monitor_error_component import (
            ApiV1EndpointsArchiveCreateDoNotMonitorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_k8s_app_error_component import (
            ApiV1EndpointsArchiveCreateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_k8s_cluster_error_component import (
            ApiV1EndpointsArchiveCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_kind_error_component import (
            ApiV1EndpointsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_labels_error_component import (
            ApiV1EndpointsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_last_agent_metrics_error_component import (
            ApiV1EndpointsArchiveCreateLastAgentMetricsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1EndpointsArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_managed_by_content_type_error_component import (
            ApiV1EndpointsArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_managed_by_object_id_error_component import (
            ApiV1EndpointsArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_max_agents_per_endpoint_error_component import (
            ApiV1EndpointsArchiveCreateMaxAgentsPerEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_modified_by_user_error_component import (
            ApiV1EndpointsArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_name_error_component import (
            ApiV1EndpointsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_non_field_errors_error_component import (
            ApiV1EndpointsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_organization_id_error_component import (
            ApiV1EndpointsArchiveCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_platform_dns_record_created_error_component import (
            ApiV1EndpointsArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_platform_service_error_component import (
            ApiV1EndpointsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_pop_endpoint_error_component import (
            ApiV1EndpointsArchiveCreatePopEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_provider_error_component import (
            ApiV1EndpointsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_provider_id_error_component import (
            ApiV1EndpointsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_provider_reference_error_component import (
            ApiV1EndpointsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_reconciliation_enabled_error_component import (
            ApiV1EndpointsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_region_error_component import (
            ApiV1EndpointsArchiveCreateRegionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_remote_address_error_component import (
            ApiV1EndpointsArchiveCreateRemoteAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_remote_port_error_component import (
            ApiV1EndpointsArchiveCreateRemotePortErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_resolved_ip_error_component import (
            ApiV1EndpointsArchiveCreateResolvedIpErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_s3_cluster_error_component import (
            ApiV1EndpointsArchiveCreateS3ClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_scope_error_component import (
            ApiV1EndpointsArchiveCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_sla_availability_error_component import (
            ApiV1EndpointsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_sla_target_error_component import (
            ApiV1EndpointsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_sla_window_days_error_component import (
            ApiV1EndpointsArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_slo_availability_error_component import (
            ApiV1EndpointsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_slo_target_error_component import (
            ApiV1EndpointsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_slo_window_days_error_component import (
            ApiV1EndpointsArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_spec_error_component import (
            ApiV1EndpointsArchiveCreateSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_target_availability_error_component import (
            ApiV1EndpointsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_workspace_id_error_component import (
            ApiV1EndpointsArchiveCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1EndpointsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1EndpointsArchiveCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateRemoteAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateRemotePortErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateCheckResultsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateDoNotMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreatePopEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateLastAgentMetricsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateResolvedIpErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateMaxAgentsPerEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateCheckResultRetentionDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateS3ClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsArchiveCreateRegionErrorComponent):
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
        from ..models.api_v1_endpoints_archive_create_actual_availability_error_component import (
            ApiV1EndpointsArchiveCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_annotations_error_component import (
            ApiV1EndpointsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_archived_at_error_component import (
            ApiV1EndpointsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_archived_by_error_component import (
            ApiV1EndpointsArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_archived_error_component import (
            ApiV1EndpointsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_archived_reason_error_component import (
            ApiV1EndpointsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_check_result_retention_days_error_component import (
            ApiV1EndpointsArchiveCreateCheckResultRetentionDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_check_results_error_component import (
            ApiV1EndpointsArchiveCreateCheckResultsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_created_by_component_error_component import (
            ApiV1EndpointsArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_created_by_user_error_component import (
            ApiV1EndpointsArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_criticality_error_component import (
            ApiV1EndpointsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_debug_mode_error_component import (
            ApiV1EndpointsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_discovery_enabled_error_component import (
            ApiV1EndpointsArchiveCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_display_name_error_component import (
            ApiV1EndpointsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_do_not_monitor_error_component import (
            ApiV1EndpointsArchiveCreateDoNotMonitorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_k8s_app_error_component import (
            ApiV1EndpointsArchiveCreateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_k8s_cluster_error_component import (
            ApiV1EndpointsArchiveCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_kind_error_component import (
            ApiV1EndpointsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_labels_error_component import (
            ApiV1EndpointsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_last_agent_metrics_error_component import (
            ApiV1EndpointsArchiveCreateLastAgentMetricsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1EndpointsArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_loadbalancer_instance_error_component import (
            ApiV1EndpointsArchiveCreateLoadbalancerInstanceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_managed_by_content_type_error_component import (
            ApiV1EndpointsArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_managed_by_object_id_error_component import (
            ApiV1EndpointsArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_max_agents_per_endpoint_error_component import (
            ApiV1EndpointsArchiveCreateMaxAgentsPerEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_modified_by_user_error_component import (
            ApiV1EndpointsArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_name_error_component import (
            ApiV1EndpointsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_non_field_errors_error_component import (
            ApiV1EndpointsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_organization_id_error_component import (
            ApiV1EndpointsArchiveCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_platform_dns_record_created_error_component import (
            ApiV1EndpointsArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_platform_service_error_component import (
            ApiV1EndpointsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_pop_endpoint_error_component import (
            ApiV1EndpointsArchiveCreatePopEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_provider_error_component import (
            ApiV1EndpointsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_provider_id_error_component import (
            ApiV1EndpointsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_provider_reference_error_component import (
            ApiV1EndpointsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_reconciliation_enabled_error_component import (
            ApiV1EndpointsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_region_error_component import (
            ApiV1EndpointsArchiveCreateRegionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_remote_address_error_component import (
            ApiV1EndpointsArchiveCreateRemoteAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_remote_port_error_component import (
            ApiV1EndpointsArchiveCreateRemotePortErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_resolved_ip_error_component import (
            ApiV1EndpointsArchiveCreateResolvedIpErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_s3_cluster_error_component import (
            ApiV1EndpointsArchiveCreateS3ClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_scope_error_component import (
            ApiV1EndpointsArchiveCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_sla_availability_error_component import (
            ApiV1EndpointsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_sla_target_error_component import (
            ApiV1EndpointsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_sla_window_days_error_component import (
            ApiV1EndpointsArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_slo_availability_error_component import (
            ApiV1EndpointsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_slo_target_error_component import (
            ApiV1EndpointsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_slo_window_days_error_component import (
            ApiV1EndpointsArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_spec_error_component import (
            ApiV1EndpointsArchiveCreateSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_target_availability_error_component import (
            ApiV1EndpointsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_archive_create_workspace_id_error_component import (
            ApiV1EndpointsArchiveCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1EndpointsArchiveCreateActualAvailabilityErrorComponent
                | ApiV1EndpointsArchiveCreateAnnotationsErrorComponent
                | ApiV1EndpointsArchiveCreateArchivedAtErrorComponent
                | ApiV1EndpointsArchiveCreateArchivedByErrorComponent
                | ApiV1EndpointsArchiveCreateArchivedErrorComponent
                | ApiV1EndpointsArchiveCreateArchivedReasonErrorComponent
                | ApiV1EndpointsArchiveCreateCheckResultRetentionDaysErrorComponent
                | ApiV1EndpointsArchiveCreateCheckResultsErrorComponent
                | ApiV1EndpointsArchiveCreateCreatedByComponentErrorComponent
                | ApiV1EndpointsArchiveCreateCreatedByUserErrorComponent
                | ApiV1EndpointsArchiveCreateCriticalityErrorComponent
                | ApiV1EndpointsArchiveCreateDebugModeErrorComponent
                | ApiV1EndpointsArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1EndpointsArchiveCreateDisplayNameErrorComponent
                | ApiV1EndpointsArchiveCreateDoNotMonitorErrorComponent
                | ApiV1EndpointsArchiveCreateK8SAppErrorComponent
                | ApiV1EndpointsArchiveCreateK8SClusterErrorComponent
                | ApiV1EndpointsArchiveCreateKindErrorComponent
                | ApiV1EndpointsArchiveCreateLabelsErrorComponent
                | ApiV1EndpointsArchiveCreateLastAgentMetricsErrorComponent
                | ApiV1EndpointsArchiveCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1EndpointsArchiveCreateLoadbalancerInstanceErrorComponent
                | ApiV1EndpointsArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1EndpointsArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1EndpointsArchiveCreateMaxAgentsPerEndpointErrorComponent
                | ApiV1EndpointsArchiveCreateModifiedByUserErrorComponent
                | ApiV1EndpointsArchiveCreateNameErrorComponent
                | ApiV1EndpointsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1EndpointsArchiveCreateOrganizationIdErrorComponent
                | ApiV1EndpointsArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1EndpointsArchiveCreatePlatformServiceErrorComponent
                | ApiV1EndpointsArchiveCreatePopEndpointErrorComponent
                | ApiV1EndpointsArchiveCreateProviderErrorComponent
                | ApiV1EndpointsArchiveCreateProviderIdErrorComponent
                | ApiV1EndpointsArchiveCreateProviderReferenceErrorComponent
                | ApiV1EndpointsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1EndpointsArchiveCreateRegionErrorComponent
                | ApiV1EndpointsArchiveCreateRemoteAddressErrorComponent
                | ApiV1EndpointsArchiveCreateRemotePortErrorComponent
                | ApiV1EndpointsArchiveCreateResolvedIpErrorComponent
                | ApiV1EndpointsArchiveCreateS3ClusterErrorComponent
                | ApiV1EndpointsArchiveCreateScopeErrorComponent
                | ApiV1EndpointsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1EndpointsArchiveCreateSlaTargetErrorComponent
                | ApiV1EndpointsArchiveCreateSlaWindowDaysErrorComponent
                | ApiV1EndpointsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1EndpointsArchiveCreateSloTargetErrorComponent
                | ApiV1EndpointsArchiveCreateSloWindowDaysErrorComponent
                | ApiV1EndpointsArchiveCreateSpecErrorComponent
                | ApiV1EndpointsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1EndpointsArchiveCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_0 = (
                        ApiV1EndpointsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_1 = (
                        ApiV1EndpointsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_2 = (
                        ApiV1EndpointsArchiveCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_3 = (
                        ApiV1EndpointsArchiveCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_4 = (
                        ApiV1EndpointsArchiveCreateSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_5 = (
                        ApiV1EndpointsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_6 = (
                        ApiV1EndpointsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_7 = (
                        ApiV1EndpointsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_8 = (
                        ApiV1EndpointsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_9 = (
                        ApiV1EndpointsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_10 = (
                        ApiV1EndpointsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_11 = (
                        ApiV1EndpointsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_12 = (
                        ApiV1EndpointsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_13 = (
                        ApiV1EndpointsArchiveCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_14 = (
                        ApiV1EndpointsArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_15 = (
                        ApiV1EndpointsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_16 = (
                        ApiV1EndpointsArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_17 = (
                        ApiV1EndpointsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_18 = (
                        ApiV1EndpointsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_19 = (
                        ApiV1EndpointsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_20 = (
                        ApiV1EndpointsArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_21 = (
                        ApiV1EndpointsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_22 = (
                        ApiV1EndpointsArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_23 = (
                        ApiV1EndpointsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_24 = (
                        ApiV1EndpointsArchiveCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_25 = (
                        ApiV1EndpointsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_26 = (
                        ApiV1EndpointsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_27 = (
                        ApiV1EndpointsArchiveCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_28 = (
                        ApiV1EndpointsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_29 = (
                        ApiV1EndpointsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_30 = (
                        ApiV1EndpointsArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_31 = (
                        ApiV1EndpointsArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_32 = (
                        ApiV1EndpointsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_33 = (
                        ApiV1EndpointsArchiveCreateRemoteAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_34 = (
                        ApiV1EndpointsArchiveCreateRemotePortErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_35 = (
                        ApiV1EndpointsArchiveCreateCheckResultsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_36 = (
                        ApiV1EndpointsArchiveCreateDoNotMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_37 = (
                        ApiV1EndpointsArchiveCreatePopEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_38 = (
                        ApiV1EndpointsArchiveCreateLastAgentMetricsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_39 = (
                        ApiV1EndpointsArchiveCreateResolvedIpErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_40 = (
                        ApiV1EndpointsArchiveCreateMaxAgentsPerEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_41 = (
                        ApiV1EndpointsArchiveCreateCheckResultRetentionDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_42 = (
                        ApiV1EndpointsArchiveCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_43 = (
                        ApiV1EndpointsArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_44 = (
                        ApiV1EndpointsArchiveCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_45 = (
                        ApiV1EndpointsArchiveCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_46 = (
                        ApiV1EndpointsArchiveCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_47 = (
                        ApiV1EndpointsArchiveCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_48 = (
                        ApiV1EndpointsArchiveCreateS3ClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_archive_create_error_type_49 = (
                        ApiV1EndpointsArchiveCreateRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_archive_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_endpoints_archive_create_error_type_50 = (
                    ApiV1EndpointsArchiveCreateLoadbalancerInstanceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_endpoints_archive_create_error_type_50

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_endpoints_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_endpoints_archive_create_validation_error.additional_properties = d
        return api_v1_endpoints_archive_create_validation_error

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
