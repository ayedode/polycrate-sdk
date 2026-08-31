from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_endpoints_discover_create_actual_availability_error_component import (
        ApiV1EndpointsDiscoverCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_annotations_error_component import (
        ApiV1EndpointsDiscoverCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_archived_at_error_component import (
        ApiV1EndpointsDiscoverCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_archived_by_error_component import (
        ApiV1EndpointsDiscoverCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_archived_error_component import (
        ApiV1EndpointsDiscoverCreateArchivedErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_archived_reason_error_component import (
        ApiV1EndpointsDiscoverCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_check_result_retention_days_error_component import (
        ApiV1EndpointsDiscoverCreateCheckResultRetentionDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_check_results_error_component import (
        ApiV1EndpointsDiscoverCreateCheckResultsErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_created_by_component_error_component import (
        ApiV1EndpointsDiscoverCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_created_by_user_error_component import (
        ApiV1EndpointsDiscoverCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_criticality_error_component import (
        ApiV1EndpointsDiscoverCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_debug_mode_error_component import (
        ApiV1EndpointsDiscoverCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_discovery_enabled_error_component import (
        ApiV1EndpointsDiscoverCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_display_name_error_component import (
        ApiV1EndpointsDiscoverCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_do_not_monitor_error_component import (
        ApiV1EndpointsDiscoverCreateDoNotMonitorErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_k8s_app_error_component import (
        ApiV1EndpointsDiscoverCreateK8SAppErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_k8s_cluster_error_component import (
        ApiV1EndpointsDiscoverCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_kind_error_component import (
        ApiV1EndpointsDiscoverCreateKindErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_labels_error_component import (
        ApiV1EndpointsDiscoverCreateLabelsErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_last_agent_metrics_error_component import (
        ApiV1EndpointsDiscoverCreateLastAgentMetricsErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1EndpointsDiscoverCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_loadbalancer_instance_error_component import (
        ApiV1EndpointsDiscoverCreateLoadbalancerInstanceErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_managed_by_content_type_error_component import (
        ApiV1EndpointsDiscoverCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_managed_by_object_id_error_component import (
        ApiV1EndpointsDiscoverCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_max_agents_per_endpoint_error_component import (
        ApiV1EndpointsDiscoverCreateMaxAgentsPerEndpointErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_modified_by_user_error_component import (
        ApiV1EndpointsDiscoverCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_name_error_component import (
        ApiV1EndpointsDiscoverCreateNameErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_non_field_errors_error_component import (
        ApiV1EndpointsDiscoverCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_organization_id_error_component import (
        ApiV1EndpointsDiscoverCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_platform_dns_record_created_error_component import (
        ApiV1EndpointsDiscoverCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_platform_service_error_component import (
        ApiV1EndpointsDiscoverCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_pop_endpoint_error_component import (
        ApiV1EndpointsDiscoverCreatePopEndpointErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_provider_error_component import (
        ApiV1EndpointsDiscoverCreateProviderErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_provider_id_error_component import (
        ApiV1EndpointsDiscoverCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_provider_reference_error_component import (
        ApiV1EndpointsDiscoverCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_reconciliation_enabled_error_component import (
        ApiV1EndpointsDiscoverCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_region_error_component import (
        ApiV1EndpointsDiscoverCreateRegionErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_remote_address_error_component import (
        ApiV1EndpointsDiscoverCreateRemoteAddressErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_remote_port_error_component import (
        ApiV1EndpointsDiscoverCreateRemotePortErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_resolved_ip_error_component import (
        ApiV1EndpointsDiscoverCreateResolvedIpErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_s3_cluster_error_component import (
        ApiV1EndpointsDiscoverCreateS3ClusterErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_scope_error_component import (
        ApiV1EndpointsDiscoverCreateScopeErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_sla_availability_error_component import (
        ApiV1EndpointsDiscoverCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_sla_target_error_component import (
        ApiV1EndpointsDiscoverCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_sla_window_days_error_component import (
        ApiV1EndpointsDiscoverCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_slo_availability_error_component import (
        ApiV1EndpointsDiscoverCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_slo_target_error_component import (
        ApiV1EndpointsDiscoverCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_slo_window_days_error_component import (
        ApiV1EndpointsDiscoverCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_spec_error_component import (
        ApiV1EndpointsDiscoverCreateSpecErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_target_availability_error_component import (
        ApiV1EndpointsDiscoverCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_discover_create_workspace_id_error_component import (
        ApiV1EndpointsDiscoverCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1EndpointsDiscoverCreateValidationError")


@_attrs_define
class ApiV1EndpointsDiscoverCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1EndpointsDiscoverCreateActualAvailabilityErrorComponent |
            ApiV1EndpointsDiscoverCreateAnnotationsErrorComponent | ApiV1EndpointsDiscoverCreateArchivedAtErrorComponent |
            ApiV1EndpointsDiscoverCreateArchivedByErrorComponent | ApiV1EndpointsDiscoverCreateArchivedErrorComponent |
            ApiV1EndpointsDiscoverCreateArchivedReasonErrorComponent |
            ApiV1EndpointsDiscoverCreateCheckResultRetentionDaysErrorComponent |
            ApiV1EndpointsDiscoverCreateCheckResultsErrorComponent |
            ApiV1EndpointsDiscoverCreateCreatedByComponentErrorComponent |
            ApiV1EndpointsDiscoverCreateCreatedByUserErrorComponent | ApiV1EndpointsDiscoverCreateCriticalityErrorComponent
            | ApiV1EndpointsDiscoverCreateDebugModeErrorComponent |
            ApiV1EndpointsDiscoverCreateDiscoveryEnabledErrorComponent |
            ApiV1EndpointsDiscoverCreateDisplayNameErrorComponent | ApiV1EndpointsDiscoverCreateDoNotMonitorErrorComponent |
            ApiV1EndpointsDiscoverCreateK8SAppErrorComponent | ApiV1EndpointsDiscoverCreateK8SClusterErrorComponent |
            ApiV1EndpointsDiscoverCreateKindErrorComponent | ApiV1EndpointsDiscoverCreateLabelsErrorComponent |
            ApiV1EndpointsDiscoverCreateLastAgentMetricsErrorComponent |
            ApiV1EndpointsDiscoverCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1EndpointsDiscoverCreateLoadbalancerInstanceErrorComponent |
            ApiV1EndpointsDiscoverCreateManagedByContentTypeErrorComponent |
            ApiV1EndpointsDiscoverCreateManagedByObjectIdErrorComponent |
            ApiV1EndpointsDiscoverCreateMaxAgentsPerEndpointErrorComponent |
            ApiV1EndpointsDiscoverCreateModifiedByUserErrorComponent | ApiV1EndpointsDiscoverCreateNameErrorComponent |
            ApiV1EndpointsDiscoverCreateNonFieldErrorsErrorComponent |
            ApiV1EndpointsDiscoverCreateOrganizationIdErrorComponent |
            ApiV1EndpointsDiscoverCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1EndpointsDiscoverCreatePlatformServiceErrorComponent |
            ApiV1EndpointsDiscoverCreatePopEndpointErrorComponent | ApiV1EndpointsDiscoverCreateProviderErrorComponent |
            ApiV1EndpointsDiscoverCreateProviderIdErrorComponent |
            ApiV1EndpointsDiscoverCreateProviderReferenceErrorComponent |
            ApiV1EndpointsDiscoverCreateReconciliationEnabledErrorComponent |
            ApiV1EndpointsDiscoverCreateRegionErrorComponent | ApiV1EndpointsDiscoverCreateRemoteAddressErrorComponent |
            ApiV1EndpointsDiscoverCreateRemotePortErrorComponent | ApiV1EndpointsDiscoverCreateResolvedIpErrorComponent |
            ApiV1EndpointsDiscoverCreateS3ClusterErrorComponent | ApiV1EndpointsDiscoverCreateScopeErrorComponent |
            ApiV1EndpointsDiscoverCreateSlaAvailabilityErrorComponent | ApiV1EndpointsDiscoverCreateSlaTargetErrorComponent
            | ApiV1EndpointsDiscoverCreateSlaWindowDaysErrorComponent |
            ApiV1EndpointsDiscoverCreateSloAvailabilityErrorComponent | ApiV1EndpointsDiscoverCreateSloTargetErrorComponent
            | ApiV1EndpointsDiscoverCreateSloWindowDaysErrorComponent | ApiV1EndpointsDiscoverCreateSpecErrorComponent |
            ApiV1EndpointsDiscoverCreateTargetAvailabilityErrorComponent |
            ApiV1EndpointsDiscoverCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1EndpointsDiscoverCreateActualAvailabilityErrorComponent
        | ApiV1EndpointsDiscoverCreateAnnotationsErrorComponent
        | ApiV1EndpointsDiscoverCreateArchivedAtErrorComponent
        | ApiV1EndpointsDiscoverCreateArchivedByErrorComponent
        | ApiV1EndpointsDiscoverCreateArchivedErrorComponent
        | ApiV1EndpointsDiscoverCreateArchivedReasonErrorComponent
        | ApiV1EndpointsDiscoverCreateCheckResultRetentionDaysErrorComponent
        | ApiV1EndpointsDiscoverCreateCheckResultsErrorComponent
        | ApiV1EndpointsDiscoverCreateCreatedByComponentErrorComponent
        | ApiV1EndpointsDiscoverCreateCreatedByUserErrorComponent
        | ApiV1EndpointsDiscoverCreateCriticalityErrorComponent
        | ApiV1EndpointsDiscoverCreateDebugModeErrorComponent
        | ApiV1EndpointsDiscoverCreateDiscoveryEnabledErrorComponent
        | ApiV1EndpointsDiscoverCreateDisplayNameErrorComponent
        | ApiV1EndpointsDiscoverCreateDoNotMonitorErrorComponent
        | ApiV1EndpointsDiscoverCreateK8SAppErrorComponent
        | ApiV1EndpointsDiscoverCreateK8SClusterErrorComponent
        | ApiV1EndpointsDiscoverCreateKindErrorComponent
        | ApiV1EndpointsDiscoverCreateLabelsErrorComponent
        | ApiV1EndpointsDiscoverCreateLastAgentMetricsErrorComponent
        | ApiV1EndpointsDiscoverCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1EndpointsDiscoverCreateLoadbalancerInstanceErrorComponent
        | ApiV1EndpointsDiscoverCreateManagedByContentTypeErrorComponent
        | ApiV1EndpointsDiscoverCreateManagedByObjectIdErrorComponent
        | ApiV1EndpointsDiscoverCreateMaxAgentsPerEndpointErrorComponent
        | ApiV1EndpointsDiscoverCreateModifiedByUserErrorComponent
        | ApiV1EndpointsDiscoverCreateNameErrorComponent
        | ApiV1EndpointsDiscoverCreateNonFieldErrorsErrorComponent
        | ApiV1EndpointsDiscoverCreateOrganizationIdErrorComponent
        | ApiV1EndpointsDiscoverCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1EndpointsDiscoverCreatePlatformServiceErrorComponent
        | ApiV1EndpointsDiscoverCreatePopEndpointErrorComponent
        | ApiV1EndpointsDiscoverCreateProviderErrorComponent
        | ApiV1EndpointsDiscoverCreateProviderIdErrorComponent
        | ApiV1EndpointsDiscoverCreateProviderReferenceErrorComponent
        | ApiV1EndpointsDiscoverCreateReconciliationEnabledErrorComponent
        | ApiV1EndpointsDiscoverCreateRegionErrorComponent
        | ApiV1EndpointsDiscoverCreateRemoteAddressErrorComponent
        | ApiV1EndpointsDiscoverCreateRemotePortErrorComponent
        | ApiV1EndpointsDiscoverCreateResolvedIpErrorComponent
        | ApiV1EndpointsDiscoverCreateS3ClusterErrorComponent
        | ApiV1EndpointsDiscoverCreateScopeErrorComponent
        | ApiV1EndpointsDiscoverCreateSlaAvailabilityErrorComponent
        | ApiV1EndpointsDiscoverCreateSlaTargetErrorComponent
        | ApiV1EndpointsDiscoverCreateSlaWindowDaysErrorComponent
        | ApiV1EndpointsDiscoverCreateSloAvailabilityErrorComponent
        | ApiV1EndpointsDiscoverCreateSloTargetErrorComponent
        | ApiV1EndpointsDiscoverCreateSloWindowDaysErrorComponent
        | ApiV1EndpointsDiscoverCreateSpecErrorComponent
        | ApiV1EndpointsDiscoverCreateTargetAvailabilityErrorComponent
        | ApiV1EndpointsDiscoverCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_endpoints_discover_create_actual_availability_error_component import (
            ApiV1EndpointsDiscoverCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_annotations_error_component import (
            ApiV1EndpointsDiscoverCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_archived_at_error_component import (
            ApiV1EndpointsDiscoverCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_archived_by_error_component import (
            ApiV1EndpointsDiscoverCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_archived_error_component import (
            ApiV1EndpointsDiscoverCreateArchivedErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_archived_reason_error_component import (
            ApiV1EndpointsDiscoverCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_check_result_retention_days_error_component import (
            ApiV1EndpointsDiscoverCreateCheckResultRetentionDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_check_results_error_component import (
            ApiV1EndpointsDiscoverCreateCheckResultsErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_created_by_component_error_component import (
            ApiV1EndpointsDiscoverCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_created_by_user_error_component import (
            ApiV1EndpointsDiscoverCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_criticality_error_component import (
            ApiV1EndpointsDiscoverCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_debug_mode_error_component import (
            ApiV1EndpointsDiscoverCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_discovery_enabled_error_component import (
            ApiV1EndpointsDiscoverCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_display_name_error_component import (
            ApiV1EndpointsDiscoverCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_do_not_monitor_error_component import (
            ApiV1EndpointsDiscoverCreateDoNotMonitorErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_k8s_app_error_component import (
            ApiV1EndpointsDiscoverCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_k8s_cluster_error_component import (
            ApiV1EndpointsDiscoverCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_kind_error_component import (
            ApiV1EndpointsDiscoverCreateKindErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_labels_error_component import (
            ApiV1EndpointsDiscoverCreateLabelsErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_last_agent_metrics_error_component import (
            ApiV1EndpointsDiscoverCreateLastAgentMetricsErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1EndpointsDiscoverCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_managed_by_content_type_error_component import (
            ApiV1EndpointsDiscoverCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_managed_by_object_id_error_component import (
            ApiV1EndpointsDiscoverCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_max_agents_per_endpoint_error_component import (
            ApiV1EndpointsDiscoverCreateMaxAgentsPerEndpointErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_modified_by_user_error_component import (
            ApiV1EndpointsDiscoverCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_name_error_component import (
            ApiV1EndpointsDiscoverCreateNameErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_non_field_errors_error_component import (
            ApiV1EndpointsDiscoverCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_organization_id_error_component import (
            ApiV1EndpointsDiscoverCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_platform_dns_record_created_error_component import (
            ApiV1EndpointsDiscoverCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_platform_service_error_component import (
            ApiV1EndpointsDiscoverCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_pop_endpoint_error_component import (
            ApiV1EndpointsDiscoverCreatePopEndpointErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_provider_error_component import (
            ApiV1EndpointsDiscoverCreateProviderErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_provider_id_error_component import (
            ApiV1EndpointsDiscoverCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_provider_reference_error_component import (
            ApiV1EndpointsDiscoverCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_reconciliation_enabled_error_component import (
            ApiV1EndpointsDiscoverCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_region_error_component import (
            ApiV1EndpointsDiscoverCreateRegionErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_remote_address_error_component import (
            ApiV1EndpointsDiscoverCreateRemoteAddressErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_remote_port_error_component import (
            ApiV1EndpointsDiscoverCreateRemotePortErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_resolved_ip_error_component import (
            ApiV1EndpointsDiscoverCreateResolvedIpErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_s3_cluster_error_component import (
            ApiV1EndpointsDiscoverCreateS3ClusterErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_scope_error_component import (
            ApiV1EndpointsDiscoverCreateScopeErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_sla_availability_error_component import (
            ApiV1EndpointsDiscoverCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_sla_target_error_component import (
            ApiV1EndpointsDiscoverCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_sla_window_days_error_component import (
            ApiV1EndpointsDiscoverCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_slo_availability_error_component import (
            ApiV1EndpointsDiscoverCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_slo_target_error_component import (
            ApiV1EndpointsDiscoverCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_slo_window_days_error_component import (
            ApiV1EndpointsDiscoverCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_spec_error_component import (
            ApiV1EndpointsDiscoverCreateSpecErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_target_availability_error_component import (
            ApiV1EndpointsDiscoverCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_workspace_id_error_component import (
            ApiV1EndpointsDiscoverCreateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1EndpointsDiscoverCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateRemoteAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateRemotePortErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateCheckResultsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateDoNotMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreatePopEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateLastAgentMetricsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateResolvedIpErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateMaxAgentsPerEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateCheckResultRetentionDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateS3ClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsDiscoverCreateRegionErrorComponent):
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
        from ..models.api_v1_endpoints_discover_create_actual_availability_error_component import (
            ApiV1EndpointsDiscoverCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_annotations_error_component import (
            ApiV1EndpointsDiscoverCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_archived_at_error_component import (
            ApiV1EndpointsDiscoverCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_archived_by_error_component import (
            ApiV1EndpointsDiscoverCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_archived_error_component import (
            ApiV1EndpointsDiscoverCreateArchivedErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_archived_reason_error_component import (
            ApiV1EndpointsDiscoverCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_check_result_retention_days_error_component import (
            ApiV1EndpointsDiscoverCreateCheckResultRetentionDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_check_results_error_component import (
            ApiV1EndpointsDiscoverCreateCheckResultsErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_created_by_component_error_component import (
            ApiV1EndpointsDiscoverCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_created_by_user_error_component import (
            ApiV1EndpointsDiscoverCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_criticality_error_component import (
            ApiV1EndpointsDiscoverCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_debug_mode_error_component import (
            ApiV1EndpointsDiscoverCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_discovery_enabled_error_component import (
            ApiV1EndpointsDiscoverCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_display_name_error_component import (
            ApiV1EndpointsDiscoverCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_do_not_monitor_error_component import (
            ApiV1EndpointsDiscoverCreateDoNotMonitorErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_k8s_app_error_component import (
            ApiV1EndpointsDiscoverCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_k8s_cluster_error_component import (
            ApiV1EndpointsDiscoverCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_kind_error_component import (
            ApiV1EndpointsDiscoverCreateKindErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_labels_error_component import (
            ApiV1EndpointsDiscoverCreateLabelsErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_last_agent_metrics_error_component import (
            ApiV1EndpointsDiscoverCreateLastAgentMetricsErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1EndpointsDiscoverCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_loadbalancer_instance_error_component import (
            ApiV1EndpointsDiscoverCreateLoadbalancerInstanceErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_managed_by_content_type_error_component import (
            ApiV1EndpointsDiscoverCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_managed_by_object_id_error_component import (
            ApiV1EndpointsDiscoverCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_max_agents_per_endpoint_error_component import (
            ApiV1EndpointsDiscoverCreateMaxAgentsPerEndpointErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_modified_by_user_error_component import (
            ApiV1EndpointsDiscoverCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_name_error_component import (
            ApiV1EndpointsDiscoverCreateNameErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_non_field_errors_error_component import (
            ApiV1EndpointsDiscoverCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_organization_id_error_component import (
            ApiV1EndpointsDiscoverCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_platform_dns_record_created_error_component import (
            ApiV1EndpointsDiscoverCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_platform_service_error_component import (
            ApiV1EndpointsDiscoverCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_pop_endpoint_error_component import (
            ApiV1EndpointsDiscoverCreatePopEndpointErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_provider_error_component import (
            ApiV1EndpointsDiscoverCreateProviderErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_provider_id_error_component import (
            ApiV1EndpointsDiscoverCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_provider_reference_error_component import (
            ApiV1EndpointsDiscoverCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_reconciliation_enabled_error_component import (
            ApiV1EndpointsDiscoverCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_region_error_component import (
            ApiV1EndpointsDiscoverCreateRegionErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_remote_address_error_component import (
            ApiV1EndpointsDiscoverCreateRemoteAddressErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_remote_port_error_component import (
            ApiV1EndpointsDiscoverCreateRemotePortErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_resolved_ip_error_component import (
            ApiV1EndpointsDiscoverCreateResolvedIpErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_s3_cluster_error_component import (
            ApiV1EndpointsDiscoverCreateS3ClusterErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_scope_error_component import (
            ApiV1EndpointsDiscoverCreateScopeErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_sla_availability_error_component import (
            ApiV1EndpointsDiscoverCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_sla_target_error_component import (
            ApiV1EndpointsDiscoverCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_sla_window_days_error_component import (
            ApiV1EndpointsDiscoverCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_slo_availability_error_component import (
            ApiV1EndpointsDiscoverCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_slo_target_error_component import (
            ApiV1EndpointsDiscoverCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_slo_window_days_error_component import (
            ApiV1EndpointsDiscoverCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_spec_error_component import (
            ApiV1EndpointsDiscoverCreateSpecErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_target_availability_error_component import (
            ApiV1EndpointsDiscoverCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_discover_create_workspace_id_error_component import (
            ApiV1EndpointsDiscoverCreateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1EndpointsDiscoverCreateActualAvailabilityErrorComponent
                | ApiV1EndpointsDiscoverCreateAnnotationsErrorComponent
                | ApiV1EndpointsDiscoverCreateArchivedAtErrorComponent
                | ApiV1EndpointsDiscoverCreateArchivedByErrorComponent
                | ApiV1EndpointsDiscoverCreateArchivedErrorComponent
                | ApiV1EndpointsDiscoverCreateArchivedReasonErrorComponent
                | ApiV1EndpointsDiscoverCreateCheckResultRetentionDaysErrorComponent
                | ApiV1EndpointsDiscoverCreateCheckResultsErrorComponent
                | ApiV1EndpointsDiscoverCreateCreatedByComponentErrorComponent
                | ApiV1EndpointsDiscoverCreateCreatedByUserErrorComponent
                | ApiV1EndpointsDiscoverCreateCriticalityErrorComponent
                | ApiV1EndpointsDiscoverCreateDebugModeErrorComponent
                | ApiV1EndpointsDiscoverCreateDiscoveryEnabledErrorComponent
                | ApiV1EndpointsDiscoverCreateDisplayNameErrorComponent
                | ApiV1EndpointsDiscoverCreateDoNotMonitorErrorComponent
                | ApiV1EndpointsDiscoverCreateK8SAppErrorComponent
                | ApiV1EndpointsDiscoverCreateK8SClusterErrorComponent
                | ApiV1EndpointsDiscoverCreateKindErrorComponent
                | ApiV1EndpointsDiscoverCreateLabelsErrorComponent
                | ApiV1EndpointsDiscoverCreateLastAgentMetricsErrorComponent
                | ApiV1EndpointsDiscoverCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1EndpointsDiscoverCreateLoadbalancerInstanceErrorComponent
                | ApiV1EndpointsDiscoverCreateManagedByContentTypeErrorComponent
                | ApiV1EndpointsDiscoverCreateManagedByObjectIdErrorComponent
                | ApiV1EndpointsDiscoverCreateMaxAgentsPerEndpointErrorComponent
                | ApiV1EndpointsDiscoverCreateModifiedByUserErrorComponent
                | ApiV1EndpointsDiscoverCreateNameErrorComponent
                | ApiV1EndpointsDiscoverCreateNonFieldErrorsErrorComponent
                | ApiV1EndpointsDiscoverCreateOrganizationIdErrorComponent
                | ApiV1EndpointsDiscoverCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1EndpointsDiscoverCreatePlatformServiceErrorComponent
                | ApiV1EndpointsDiscoverCreatePopEndpointErrorComponent
                | ApiV1EndpointsDiscoverCreateProviderErrorComponent
                | ApiV1EndpointsDiscoverCreateProviderIdErrorComponent
                | ApiV1EndpointsDiscoverCreateProviderReferenceErrorComponent
                | ApiV1EndpointsDiscoverCreateReconciliationEnabledErrorComponent
                | ApiV1EndpointsDiscoverCreateRegionErrorComponent
                | ApiV1EndpointsDiscoverCreateRemoteAddressErrorComponent
                | ApiV1EndpointsDiscoverCreateRemotePortErrorComponent
                | ApiV1EndpointsDiscoverCreateResolvedIpErrorComponent
                | ApiV1EndpointsDiscoverCreateS3ClusterErrorComponent
                | ApiV1EndpointsDiscoverCreateScopeErrorComponent
                | ApiV1EndpointsDiscoverCreateSlaAvailabilityErrorComponent
                | ApiV1EndpointsDiscoverCreateSlaTargetErrorComponent
                | ApiV1EndpointsDiscoverCreateSlaWindowDaysErrorComponent
                | ApiV1EndpointsDiscoverCreateSloAvailabilityErrorComponent
                | ApiV1EndpointsDiscoverCreateSloTargetErrorComponent
                | ApiV1EndpointsDiscoverCreateSloWindowDaysErrorComponent
                | ApiV1EndpointsDiscoverCreateSpecErrorComponent
                | ApiV1EndpointsDiscoverCreateTargetAvailabilityErrorComponent
                | ApiV1EndpointsDiscoverCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_0 = (
                        ApiV1EndpointsDiscoverCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_1 = (
                        ApiV1EndpointsDiscoverCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_2 = (
                        ApiV1EndpointsDiscoverCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_3 = (
                        ApiV1EndpointsDiscoverCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_4 = (
                        ApiV1EndpointsDiscoverCreateSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_5 = (
                        ApiV1EndpointsDiscoverCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_6 = (
                        ApiV1EndpointsDiscoverCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_7 = (
                        ApiV1EndpointsDiscoverCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_8 = (
                        ApiV1EndpointsDiscoverCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_9 = (
                        ApiV1EndpointsDiscoverCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_10 = (
                        ApiV1EndpointsDiscoverCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_11 = (
                        ApiV1EndpointsDiscoverCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_12 = (
                        ApiV1EndpointsDiscoverCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_13 = (
                        ApiV1EndpointsDiscoverCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_14 = (
                        ApiV1EndpointsDiscoverCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_15 = (
                        ApiV1EndpointsDiscoverCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_16 = (
                        ApiV1EndpointsDiscoverCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_17 = (
                        ApiV1EndpointsDiscoverCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_18 = (
                        ApiV1EndpointsDiscoverCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_19 = (
                        ApiV1EndpointsDiscoverCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_20 = (
                        ApiV1EndpointsDiscoverCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_21 = (
                        ApiV1EndpointsDiscoverCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_22 = (
                        ApiV1EndpointsDiscoverCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_23 = (
                        ApiV1EndpointsDiscoverCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_24 = (
                        ApiV1EndpointsDiscoverCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_25 = (
                        ApiV1EndpointsDiscoverCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_26 = (
                        ApiV1EndpointsDiscoverCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_27 = (
                        ApiV1EndpointsDiscoverCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_28 = (
                        ApiV1EndpointsDiscoverCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_29 = (
                        ApiV1EndpointsDiscoverCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_30 = (
                        ApiV1EndpointsDiscoverCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_31 = (
                        ApiV1EndpointsDiscoverCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_32 = (
                        ApiV1EndpointsDiscoverCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_33 = (
                        ApiV1EndpointsDiscoverCreateRemoteAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_34 = (
                        ApiV1EndpointsDiscoverCreateRemotePortErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_35 = (
                        ApiV1EndpointsDiscoverCreateCheckResultsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_36 = (
                        ApiV1EndpointsDiscoverCreateDoNotMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_37 = (
                        ApiV1EndpointsDiscoverCreatePopEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_38 = (
                        ApiV1EndpointsDiscoverCreateLastAgentMetricsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_39 = (
                        ApiV1EndpointsDiscoverCreateResolvedIpErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_40 = (
                        ApiV1EndpointsDiscoverCreateMaxAgentsPerEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_41 = (
                        ApiV1EndpointsDiscoverCreateCheckResultRetentionDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_42 = (
                        ApiV1EndpointsDiscoverCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_43 = (
                        ApiV1EndpointsDiscoverCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_44 = (
                        ApiV1EndpointsDiscoverCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_45 = (
                        ApiV1EndpointsDiscoverCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_46 = (
                        ApiV1EndpointsDiscoverCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_47 = (
                        ApiV1EndpointsDiscoverCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_48 = (
                        ApiV1EndpointsDiscoverCreateS3ClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_discover_create_error_type_49 = (
                        ApiV1EndpointsDiscoverCreateRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_discover_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_endpoints_discover_create_error_type_50 = (
                    ApiV1EndpointsDiscoverCreateLoadbalancerInstanceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_endpoints_discover_create_error_type_50

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_endpoints_discover_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_endpoints_discover_create_validation_error.additional_properties = d
        return api_v1_endpoints_discover_create_validation_error

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
