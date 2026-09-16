from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_clusters_discover_create_active_error_component import (
        ApiV1KubernetesClustersDiscoverCreateActiveErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_actual_availability_error_component import (
        ApiV1KubernetesClustersDiscoverCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_addons_error_component import (
        ApiV1KubernetesClustersDiscoverCreateAddonsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_alias_error_component import (
        ApiV1KubernetesClustersDiscoverCreateAliasErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_annotations_error_component import (
        ApiV1KubernetesClustersDiscoverCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_api_server_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersDiscoverCreateApiServerCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_archived_at_error_component import (
        ApiV1KubernetesClustersDiscoverCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_archived_error_component import (
        ApiV1KubernetesClustersDiscoverCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_archived_reason_error_component import (
        ApiV1KubernetesClustersDiscoverCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_backup_schedules_error_component import (
        ApiV1KubernetesClustersDiscoverCreateBackupSchedulesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_baserow_id_error_component import (
        ApiV1KubernetesClustersDiscoverCreateBaserowIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_credential_error_component import (
        ApiV1KubernetesClustersDiscoverCreateCredentialErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_criticality_error_component import (
        ApiV1KubernetesClustersDiscoverCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_debug_mode_error_component import (
        ApiV1KubernetesClustersDiscoverCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_description_error_component import (
        ApiV1KubernetesClustersDiscoverCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_discovery_enabled_error_component import (
        ApiV1KubernetesClustersDiscoverCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_discovery_ignored_namespaces_error_component import (
        ApiV1KubernetesClustersDiscoverCreateDiscoveryIgnoredNamespacesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_display_name_error_component import (
        ApiV1KubernetesClustersDiscoverCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_gitlab_project_id_error_component import (
        ApiV1KubernetesClustersDiscoverCreateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_installed_error_component import (
        ApiV1KubernetesClustersDiscoverCreateInstalledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_is_host_cluster_error_component import (
        ApiV1KubernetesClustersDiscoverCreateIsHostClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_is_infrastructure_cluster_error_component import (
        ApiV1KubernetesClustersDiscoverCreateIsInfrastructureClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_kind_error_component import (
        ApiV1KubernetesClustersDiscoverCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_kubeconfig_ca_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersDiscoverCreateKubeconfigCaCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_kubeconfig_client_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersDiscoverCreateKubeconfigClientCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_kubernetes_version_error_component import (
        ApiV1KubernetesClustersDiscoverCreateKubernetesVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_labels_error_component import (
        ApiV1KubernetesClustersDiscoverCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_last_backup_import_error_component import (
        ApiV1KubernetesClustersDiscoverCreateLastBackupImportErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_managed_by_content_type_error_component import (
        ApiV1KubernetesClustersDiscoverCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_managed_by_object_id_error_component import (
        ApiV1KubernetesClustersDiscoverCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_name_error_component import (
        ApiV1KubernetesClustersDiscoverCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_non_field_errors_error_component import (
        ApiV1KubernetesClustersDiscoverCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_operator_ignore_namespaces_error_component import (
        ApiV1KubernetesClustersDiscoverCreateOperatorIgnoreNamespacesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_operator_loglevel_error_component import (
        ApiV1KubernetesClustersDiscoverCreateOperatorLoglevelErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_platform_dns_record_created_error_component import (
        ApiV1KubernetesClustersDiscoverCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_platform_service_error_component import (
        ApiV1KubernetesClustersDiscoverCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_provider_error_component import (
        ApiV1KubernetesClustersDiscoverCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_provider_id_error_component import (
        ApiV1KubernetesClustersDiscoverCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_provider_reference_error_component import (
        ApiV1KubernetesClustersDiscoverCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesClustersDiscoverCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_scope_error_component import (
        ApiV1KubernetesClustersDiscoverCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_sla_availability_error_component import (
        ApiV1KubernetesClustersDiscoverCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_sla_target_error_component import (
        ApiV1KubernetesClustersDiscoverCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_slo_availability_error_component import (
        ApiV1KubernetesClustersDiscoverCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_slo_target_error_component import (
        ApiV1KubernetesClustersDiscoverCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_slug_error_component import (
        ApiV1KubernetesClustersDiscoverCreateSlugErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_discover_create_target_availability_error_component import (
        ApiV1KubernetesClustersDiscoverCreateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesClustersDiscoverCreateValidationError")


@_attrs_define
class ApiV1KubernetesClustersDiscoverCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesClustersDiscoverCreateActiveErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateAddonsErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateAliasErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateAnnotationsErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateApiServerCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateArchivedAtErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateArchivedErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateArchivedReasonErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateBackupSchedulesErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateBaserowIdErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateCredentialErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateCriticalityErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateDebugModeErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateDescriptionErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateDiscoveryIgnoredNamespacesErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateDisplayNameErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateGitlabProjectIdErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateInstalledErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateIsHostClusterErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateIsInfrastructureClusterErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateKindErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateKubeconfigCaCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateKubeconfigClientCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateKubernetesVersionErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateLabelsErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateLastBackupImportErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateManagedByContentTypeErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateManagedByObjectIdErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateNameErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateOperatorIgnoreNamespacesErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateOperatorLoglevelErrorComponent |
            ApiV1KubernetesClustersDiscoverCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1KubernetesClustersDiscoverCreatePlatformServiceErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateProviderErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateProviderIdErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateProviderReferenceErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateScopeErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateSlaTargetErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateSloTargetErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateSlugErrorComponent |
            ApiV1KubernetesClustersDiscoverCreateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesClustersDiscoverCreateActiveErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateAddonsErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateAliasErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateAnnotationsErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateApiServerCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateArchivedAtErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateArchivedErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateArchivedReasonErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateBackupSchedulesErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateBaserowIdErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateCredentialErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateCriticalityErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateDebugModeErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateDescriptionErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateDiscoveryIgnoredNamespacesErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateDisplayNameErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateGitlabProjectIdErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateInstalledErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateIsHostClusterErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateIsInfrastructureClusterErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateKindErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateKubeconfigCaCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateKubeconfigClientCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateKubernetesVersionErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateLabelsErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateLastBackupImportErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateManagedByContentTypeErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateManagedByObjectIdErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateNameErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateOperatorIgnoreNamespacesErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateOperatorLoglevelErrorComponent
        | ApiV1KubernetesClustersDiscoverCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1KubernetesClustersDiscoverCreatePlatformServiceErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateProviderErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateProviderIdErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateProviderReferenceErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateScopeErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateSlaTargetErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateSloTargetErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateSlugErrorComponent
        | ApiV1KubernetesClustersDiscoverCreateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_clusters_discover_create_active_error_component import (
            ApiV1KubernetesClustersDiscoverCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_actual_availability_error_component import (
            ApiV1KubernetesClustersDiscoverCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_addons_error_component import (
            ApiV1KubernetesClustersDiscoverCreateAddonsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_alias_error_component import (
            ApiV1KubernetesClustersDiscoverCreateAliasErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_annotations_error_component import (
            ApiV1KubernetesClustersDiscoverCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_api_server_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersDiscoverCreateApiServerCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_archived_at_error_component import (
            ApiV1KubernetesClustersDiscoverCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_archived_error_component import (
            ApiV1KubernetesClustersDiscoverCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_archived_reason_error_component import (
            ApiV1KubernetesClustersDiscoverCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_backup_schedules_error_component import (
            ApiV1KubernetesClustersDiscoverCreateBackupSchedulesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_baserow_id_error_component import (
            ApiV1KubernetesClustersDiscoverCreateBaserowIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_credential_error_component import (
            ApiV1KubernetesClustersDiscoverCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_criticality_error_component import (
            ApiV1KubernetesClustersDiscoverCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_debug_mode_error_component import (
            ApiV1KubernetesClustersDiscoverCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_description_error_component import (
            ApiV1KubernetesClustersDiscoverCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_discovery_enabled_error_component import (
            ApiV1KubernetesClustersDiscoverCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_discovery_ignored_namespaces_error_component import (
            ApiV1KubernetesClustersDiscoverCreateDiscoveryIgnoredNamespacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_display_name_error_component import (
            ApiV1KubernetesClustersDiscoverCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_gitlab_project_id_error_component import (
            ApiV1KubernetesClustersDiscoverCreateGitlabProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_installed_error_component import (
            ApiV1KubernetesClustersDiscoverCreateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_is_host_cluster_error_component import (
            ApiV1KubernetesClustersDiscoverCreateIsHostClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_is_infrastructure_cluster_error_component import (
            ApiV1KubernetesClustersDiscoverCreateIsInfrastructureClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_kind_error_component import (
            ApiV1KubernetesClustersDiscoverCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_kubeconfig_ca_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersDiscoverCreateKubeconfigCaCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_kubeconfig_client_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersDiscoverCreateKubeconfigClientCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_kubernetes_version_error_component import (
            ApiV1KubernetesClustersDiscoverCreateKubernetesVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_labels_error_component import (
            ApiV1KubernetesClustersDiscoverCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_last_backup_import_error_component import (
            ApiV1KubernetesClustersDiscoverCreateLastBackupImportErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_managed_by_content_type_error_component import (
            ApiV1KubernetesClustersDiscoverCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_name_error_component import (
            ApiV1KubernetesClustersDiscoverCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_non_field_errors_error_component import (
            ApiV1KubernetesClustersDiscoverCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_operator_ignore_namespaces_error_component import (
            ApiV1KubernetesClustersDiscoverCreateOperatorIgnoreNamespacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_operator_loglevel_error_component import (
            ApiV1KubernetesClustersDiscoverCreateOperatorLoglevelErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesClustersDiscoverCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_platform_service_error_component import (
            ApiV1KubernetesClustersDiscoverCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_provider_error_component import (
            ApiV1KubernetesClustersDiscoverCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_provider_id_error_component import (
            ApiV1KubernetesClustersDiscoverCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_provider_reference_error_component import (
            ApiV1KubernetesClustersDiscoverCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesClustersDiscoverCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_scope_error_component import (
            ApiV1KubernetesClustersDiscoverCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_sla_availability_error_component import (
            ApiV1KubernetesClustersDiscoverCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_sla_target_error_component import (
            ApiV1KubernetesClustersDiscoverCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_slo_availability_error_component import (
            ApiV1KubernetesClustersDiscoverCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_slo_target_error_component import (
            ApiV1KubernetesClustersDiscoverCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_slug_error_component import (
            ApiV1KubernetesClustersDiscoverCreateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_target_availability_error_component import (
            ApiV1KubernetesClustersDiscoverCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateKubernetesVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateIsHostClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersDiscoverCreateIsInfrastructureClusterErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersDiscoverCreateKubeconfigCaCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersDiscoverCreateKubeconfigClientCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersDiscoverCreateApiServerCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersDiscoverCreateDiscoveryIgnoredNamespacesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateOperatorLoglevelErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersDiscoverCreateOperatorIgnoreNamespacesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateAddonsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateBackupSchedulesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateBaserowIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateLastBackupImportErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersDiscoverCreatePlatformDnsRecordCreatedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersDiscoverCreateManagedByContentTypeErrorComponent):
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
        from ..models.api_v1_kubernetes_clusters_discover_create_active_error_component import (
            ApiV1KubernetesClustersDiscoverCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_actual_availability_error_component import (
            ApiV1KubernetesClustersDiscoverCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_addons_error_component import (
            ApiV1KubernetesClustersDiscoverCreateAddonsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_alias_error_component import (
            ApiV1KubernetesClustersDiscoverCreateAliasErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_annotations_error_component import (
            ApiV1KubernetesClustersDiscoverCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_api_server_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersDiscoverCreateApiServerCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_archived_at_error_component import (
            ApiV1KubernetesClustersDiscoverCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_archived_error_component import (
            ApiV1KubernetesClustersDiscoverCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_archived_reason_error_component import (
            ApiV1KubernetesClustersDiscoverCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_backup_schedules_error_component import (
            ApiV1KubernetesClustersDiscoverCreateBackupSchedulesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_baserow_id_error_component import (
            ApiV1KubernetesClustersDiscoverCreateBaserowIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_credential_error_component import (
            ApiV1KubernetesClustersDiscoverCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_criticality_error_component import (
            ApiV1KubernetesClustersDiscoverCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_debug_mode_error_component import (
            ApiV1KubernetesClustersDiscoverCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_description_error_component import (
            ApiV1KubernetesClustersDiscoverCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_discovery_enabled_error_component import (
            ApiV1KubernetesClustersDiscoverCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_discovery_ignored_namespaces_error_component import (
            ApiV1KubernetesClustersDiscoverCreateDiscoveryIgnoredNamespacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_display_name_error_component import (
            ApiV1KubernetesClustersDiscoverCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_gitlab_project_id_error_component import (
            ApiV1KubernetesClustersDiscoverCreateGitlabProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_installed_error_component import (
            ApiV1KubernetesClustersDiscoverCreateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_is_host_cluster_error_component import (
            ApiV1KubernetesClustersDiscoverCreateIsHostClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_is_infrastructure_cluster_error_component import (
            ApiV1KubernetesClustersDiscoverCreateIsInfrastructureClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_kind_error_component import (
            ApiV1KubernetesClustersDiscoverCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_kubeconfig_ca_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersDiscoverCreateKubeconfigCaCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_kubeconfig_client_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersDiscoverCreateKubeconfigClientCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_kubernetes_version_error_component import (
            ApiV1KubernetesClustersDiscoverCreateKubernetesVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_labels_error_component import (
            ApiV1KubernetesClustersDiscoverCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_last_backup_import_error_component import (
            ApiV1KubernetesClustersDiscoverCreateLastBackupImportErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_managed_by_content_type_error_component import (
            ApiV1KubernetesClustersDiscoverCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_managed_by_object_id_error_component import (
            ApiV1KubernetesClustersDiscoverCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_name_error_component import (
            ApiV1KubernetesClustersDiscoverCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_non_field_errors_error_component import (
            ApiV1KubernetesClustersDiscoverCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_operator_ignore_namespaces_error_component import (
            ApiV1KubernetesClustersDiscoverCreateOperatorIgnoreNamespacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_operator_loglevel_error_component import (
            ApiV1KubernetesClustersDiscoverCreateOperatorLoglevelErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesClustersDiscoverCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_platform_service_error_component import (
            ApiV1KubernetesClustersDiscoverCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_provider_error_component import (
            ApiV1KubernetesClustersDiscoverCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_provider_id_error_component import (
            ApiV1KubernetesClustersDiscoverCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_provider_reference_error_component import (
            ApiV1KubernetesClustersDiscoverCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesClustersDiscoverCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_scope_error_component import (
            ApiV1KubernetesClustersDiscoverCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_sla_availability_error_component import (
            ApiV1KubernetesClustersDiscoverCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_sla_target_error_component import (
            ApiV1KubernetesClustersDiscoverCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_slo_availability_error_component import (
            ApiV1KubernetesClustersDiscoverCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_slo_target_error_component import (
            ApiV1KubernetesClustersDiscoverCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_slug_error_component import (
            ApiV1KubernetesClustersDiscoverCreateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_discover_create_target_availability_error_component import (
            ApiV1KubernetesClustersDiscoverCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesClustersDiscoverCreateActiveErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateAddonsErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateAliasErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateAnnotationsErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateApiServerCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateArchivedAtErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateArchivedErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateArchivedReasonErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateBackupSchedulesErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateBaserowIdErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateCredentialErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateCriticalityErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateDebugModeErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateDescriptionErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateDiscoveryIgnoredNamespacesErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateDisplayNameErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateGitlabProjectIdErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateInstalledErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateIsHostClusterErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateIsInfrastructureClusterErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateKindErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateKubeconfigCaCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateKubeconfigClientCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateKubernetesVersionErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateLabelsErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateLastBackupImportErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateManagedByContentTypeErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateManagedByObjectIdErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateNameErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateOperatorIgnoreNamespacesErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateOperatorLoglevelErrorComponent
                | ApiV1KubernetesClustersDiscoverCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1KubernetesClustersDiscoverCreatePlatformServiceErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateProviderErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateProviderIdErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateProviderReferenceErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateScopeErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateSlaTargetErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateSloTargetErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateSlugErrorComponent
                | ApiV1KubernetesClustersDiscoverCreateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_0 = (
                        ApiV1KubernetesClustersDiscoverCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_1 = (
                        ApiV1KubernetesClustersDiscoverCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_2 = (
                        ApiV1KubernetesClustersDiscoverCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_3 = (
                        ApiV1KubernetesClustersDiscoverCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_4 = (
                        ApiV1KubernetesClustersDiscoverCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_5 = (
                        ApiV1KubernetesClustersDiscoverCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_6 = (
                        ApiV1KubernetesClustersDiscoverCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_7 = (
                        ApiV1KubernetesClustersDiscoverCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_8 = (
                        ApiV1KubernetesClustersDiscoverCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_9 = (
                        ApiV1KubernetesClustersDiscoverCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_10 = (
                        ApiV1KubernetesClustersDiscoverCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_11 = (
                        ApiV1KubernetesClustersDiscoverCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_12 = (
                        ApiV1KubernetesClustersDiscoverCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_13 = (
                        ApiV1KubernetesClustersDiscoverCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_14 = (
                        ApiV1KubernetesClustersDiscoverCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_15 = (
                        ApiV1KubernetesClustersDiscoverCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_16 = (
                        ApiV1KubernetesClustersDiscoverCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_17 = (
                        ApiV1KubernetesClustersDiscoverCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_18 = (
                        ApiV1KubernetesClustersDiscoverCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_19 = (
                        ApiV1KubernetesClustersDiscoverCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_20 = (
                        ApiV1KubernetesClustersDiscoverCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_21 = (
                        ApiV1KubernetesClustersDiscoverCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_22 = (
                        ApiV1KubernetesClustersDiscoverCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_23 = (
                        ApiV1KubernetesClustersDiscoverCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_24 = (
                        ApiV1KubernetesClustersDiscoverCreateKubernetesVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_25 = (
                        ApiV1KubernetesClustersDiscoverCreateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_26 = (
                        ApiV1KubernetesClustersDiscoverCreateIsHostClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_27 = (
                        ApiV1KubernetesClustersDiscoverCreateIsInfrastructureClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_28 = (
                        ApiV1KubernetesClustersDiscoverCreateKubeconfigCaCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_29 = (
                        ApiV1KubernetesClustersDiscoverCreateKubeconfigClientCertExpiryDateErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_30 = (
                        ApiV1KubernetesClustersDiscoverCreateApiServerCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_31 = (
                        ApiV1KubernetesClustersDiscoverCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_32 = (
                        ApiV1KubernetesClustersDiscoverCreateDiscoveryIgnoredNamespacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_33 = (
                        ApiV1KubernetesClustersDiscoverCreateOperatorLoglevelErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_34 = (
                        ApiV1KubernetesClustersDiscoverCreateOperatorIgnoreNamespacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_35 = (
                        ApiV1KubernetesClustersDiscoverCreateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_36 = (
                        ApiV1KubernetesClustersDiscoverCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_37 = (
                        ApiV1KubernetesClustersDiscoverCreateAddonsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_38 = (
                        ApiV1KubernetesClustersDiscoverCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_39 = (
                        ApiV1KubernetesClustersDiscoverCreateBackupSchedulesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_40 = (
                        ApiV1KubernetesClustersDiscoverCreateBaserowIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_41 = (
                        ApiV1KubernetesClustersDiscoverCreateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_42 = (
                        ApiV1KubernetesClustersDiscoverCreateLastBackupImportErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_43 = (
                        ApiV1KubernetesClustersDiscoverCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_44 = (
                        ApiV1KubernetesClustersDiscoverCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_45 = (
                        ApiV1KubernetesClustersDiscoverCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_46 = (
                    ApiV1KubernetesClustersDiscoverCreateManagedByObjectIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_clusters_discover_create_error_type_46

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_clusters_discover_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_clusters_discover_create_validation_error.additional_properties = d
        return api_v1_kubernetes_clusters_discover_create_validation_error

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
